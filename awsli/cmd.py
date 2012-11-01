
import sys
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
        options, arguments = self.parser.parse_args()
        if not arguments and options.help:
            self.parser.print_help()
            sys.exit(0)
        else:
            self.parser.remove_option("-h")


class BaseCommand(OptParseMixin):
    """ Base class to handle commands """
    CMD_PREFIX = 'cmd_'
    
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
        self.print_help(message='Error: command not found')


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





