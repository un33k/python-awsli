import sys
import optparse

class BaseCommand(object):
    def __init__(self, *args, **kwargs):
        self.install_optparse()
        self.add_options()

    def install_optparse(self):
        self.parser = optparse.OptionParser()

    def add_options(self):
        pass

    def print_help(self, message='', usage=''):
        print >> sys.stderr, message
        self.parser.print_help()

    def execute(self):
        self.print_help(message='must overload execute')


if __name__ == '__main__':
    bc = BaseCommand()
    bc.execute()