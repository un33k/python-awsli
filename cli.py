#!/usr/bin/env python

import subprocess
from awsli.base import BaseCommand
import os, sys, cmd, shlex

#activate tab completion on mac or linux
try:
    import readline
    import rlcompleter
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
except ImportError:
    pass
    
class AmazonWebServicesLineInterpreter(BaseCommand, cmd.Cmd):
    doc_header = "Available Console commands (type help <topic>):"
    aws_header = "AWS Commands (type help <command>):"
    
    def __init__(self, *args, **kwargs):
        super(AmazonWebServicesLineInterpreter, self).__init__(load_default_options=False, *args, **kwargs)
        cmd.Cmd.__init__(self) #for some reason Cmd doesn't get initialised by the above line
        self.prompt = "(cli) "
        self.intro  = "Welcome to AWSLI console!"  
        self.parser.usage = '[cli_options] <command> [command_options]'
        self.cmds_path = os.path.abspath(os.path.normpath(
                            os.path.join(os.path.dirname(__file__), 'awsli', 'commands'))) 
        self.commands = []
        
    def set_cmd_options(self):
        """
        Keep track of any added options so they can be stripped before invoking aws commands
        
        Called in add_options after new options are added
        """
        self.added_options = self.parser._long_opt.keys()
        self.added_options.extend(self.parser._short_opt.keys())
        
    def add_options(self):
        self.parser.add_option(
                "-q", "--quiet",
                action="store_true",
                dest="quiet",
                default=False,
                help="don't print output"
        )
        self.set_cmd_options()
        self.parser.disable_interspersed_args()

    def get_cmd_list(self, with_prepend=True):
        """
        Search awsli/commands/ and pull in all implemented commands stripping off .py
        and prepending ws_
        """
        commands = []
        if self.commands: 
            commands = self.commands
        else:
            commands = os.listdir(self.cmds_path)
            commands = ['ws_'+c.strip('.py') 
                    for c in commands if (c.endswith('.py') and not (c.startswith('_') or c.startswith('.')))
                    ]
        self.commands = commands
        return commands if with_prepend else [c.replace('ws_','',1) for c in commands]
    
    def get_names(self):
        """
        Overides Cmd.get_names in order to pull in awsli commands
        """
        # This method used to pull in base class attributes
        # at a time dir() didn't do it yet.
        attrs = dir(self.__class__)
        attrs.extend(self.get_cmd_list())
        return attrs

    def do_list(self, command):
        """Get command(s) lis
           'list' or 'ls' with no arguments prints the available commands list
        """
        self.print_cmd_list()

    def do_help(self, command):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        cmds = self.get_cmd_list(with_prepend=False)
        
        if command in cmds:
            cmd_str = '%s.py'%os.path.join(self.cmds_path,command) 
            self.execute(cmd_str, '-h', None, quiet=False)
            return
    
        #Display default help from docstrings in do_ methods
        cmd.Cmd.do_help(self, command)
        #Display all implemented aws commands
        self.stdout.write("%s\n"%str(self.doc_leader))
        self.print_topics(self.aws_header, cmds,   15,80)
        
    def get_cli_cmds(self, with_prepend=False):
        """
        Fetch all commands prepended with 'do_'
        """
        cmds = []
        for c in self.get_names():
            if c.startswith('do_'):
                if getattr(self, c).__doc__:
                    cmds.append(c)
        return cmds if with_prepend else [c.replace('do_','',1) for c in cmds]
        
    def complete_help(self, text, line, start_index, end_index):
        """
        Perform tab completion for all commands with doc string or help info
        """
        cmds = self.get_cmd_list(with_prepend=False)
        cmds.extend(self.get_cli_cmds(with_prepend=False))
        
        if text:
            return [
                c for c in cmds
                if c.startswith(text)
            ]
        else:
            return cmds
        
    def do_exit(self,args):
        """
        Quit Console
        """
        sys.exit('Bye!')
        
    def do_usage(self, args=''):
        """
        Display Interactive Commandline Usage
        """
        self.stdout.write(self.parser.format_help())
        
    def completenames(self, text, *ignored):
        """
        Overides Cmd.completenames 
        """
        dotext = 'do_'+text
        wstext = 'ws_'+text
        return [a[3:] for a in self.get_names() if (a.startswith(dotext) or a.startswith(wstext))]    
    
    def onecmd(self, line):
        """
        Overide Comd.onecmd.
        Interpret the argument as though it had been typed in response
        to the prompt.

        This may be overridden, but should not normally need to be;
        see the precmd() and postcmd() methods for useful execution hooks.
        The return value is a flag indicating whether interpretation of
        commands by the interpreter should stop.
        
        """        
        cmd, arg, line = self.parseline(line)
        commands = self.get_cmd_list()
        if cmd and 'ws_'+cmd in commands:
            fmt_cmd = '%s.py '%os.path.join(self.cmds_path,cmd) 
            return self.execute(fmt_cmd, arg, line)
        elif(not line):
            return 
        else:
            super(AmazonWebServicesLineInterpreter, self).onecmd(line)
        
    def precmd(self, line):             
        """Called on an input line to pre-process line.
           In our case we are going to just check if an option is passed in to Cmd interface and strip it off
        """
        try:
            self.options, self.args = self.parser.parse_args(shlex.split(line.strip()))
            #Perform any cli options here and return to prompt
            if not self.args:
                if self.options.list:
                    self.print_cmd_list()
                elif self.options.quiet:
                    self.do_usage()
                return ''
        except:
            return ''
        #strip all options from the line preceding aws commands. e.g '--quiet node_list -key=somekey' =>'node_list -key=somekey' 
        for o in self.added_options:
            if o in line:
                line = line.replace(o, '', 1).lstrip()
        return line
    
    def print_cmd_list(self):
        l = [c.replace('ws_','',1) for c in self.get_cmd_list()]
        self.stdout.write('  '.join(l)+'\n')
            
    def execute(self, cmd, args, line, **options):
        """
        Perform system call: e.g python awsli/commands/<cmd>.py args
        """
        if not cmd: return
        
        popenargs = ['python', cmd]
        
        if self.is_string(args):
            popenargs.extend(shlex.split(args))
        elif self.is_list(args):
            popenargs.extend(args)
            
        if options.get('quiet',self.options.quiet):
            return subprocess.call(popenargs, stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
        else:
            return subprocess.call(popenargs)
        
if __name__ == '__main__':
    aws = AmazonWebServicesLineInterpreter()
    aws.cmdloop()





