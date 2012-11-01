
import sys
import types
import optparse
from decorator import decorator


class OptParseMixin(object):
    """ Mixin to handle help options at program vs. command level """
    def __init__(self, *args, **kwargs):
        self.parser = optparse.OptionParser()
        self.parser.remove_option("-h")
        self.parser.usage = '%prog <command> [options]'
        self.parser.add_option(
                "-h", "--help",
                action="store_true",
                dest="help",
                default=False,
                help="show this help message and exit"
        )
        self.parser.add_option(
                "-l", "--list",
                action="store_true",
                dest="list",
                default=False,
                help="list available commands and exit"
        )
        opts, args = self.parser.parse_args()
        if not args and opts.help:
            self.parser.print_help()
            sys.exit(0)
        elif not args and opts.list:
            self.cmd_list()
            sys.exit(0)
        else:
            self.parser.remove_option("-h")
            self.parser.remove_option("-l")


class BaseCommand(OptParseMixin):
    """ Base class to handle commands """
    CMD_PREFIX = 'cmd_'
    hidden_cmds = ['cmd_empty', 'cmd_unknown', 'cmd_list']
    def __init__(self, *args, **kwargs):
        super(BaseCommand, self).__init__(*args, **kwargs)
        self.parser.add_option(
                "-h", "--help",
                action="store_true",
                dest="help",
                default=False,
                help="show this help message and exit"
        )

    def print_help(self, usage='%prog <command> [options]', message=''):
        """ Prints help """
        print >> sys.stderr, message
        self.parser.usage = usage
        self.parser.print_help()


    def cmd_empty(self):
        """ Handles empty command """
        self.print_help(message='Error: missing command')


    def cmd_unknown(self):
        """ Handles known commands """
        self.parser.add_option(
                "-l", "--list",
                action="store_true",
                dest="list",
                default=False,
                help="list available commands and exit"
        )
        self.print_help(message='Error: command not found')


    def cmd_list(self):
        """ List available commands """
        commands = [m.strip(self.CMD_PREFIX).replace('_', '-') for m in dir(self)
                        if m.startswith(self.CMD_PREFIX) and not m in self.hidden_cmds]
        
        for c in commands:
            print >> sys.stderr, c


    def execute(self):
        """ Execute a command if the method exists """
        opts, args = self.parser.parse_args()
        try:
            cmd_name = args[0]
        except:
            cmd_name = "empty"
        cmd_func = self.get_command(cmd_name)
        if cmd_func and callable(cmd_func):
            return cmd_func()
        else:
            self.cmd_unknown()


    def get_command(self, command='unknown'):
        """ Returns a command method if command exists and is executable """
        return getattr(self, self.CMD_PREFIX + command.replace('-', '_'), None)



if __name__ == '__main__':
    bc = BaseCommand()
    bc.execute()





