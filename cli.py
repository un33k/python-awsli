#!/usr/bin/env python

import os
import sys
import types
import optparse
import subprocess
import awsli
from awsli.base import BaseCommand


class AmazonWebServicesLineInterpreter(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(AmazonWebServicesLineInterpreter, self).__init__(*args, **kwargs)
        self.parser.usage = '%prog [options] <command> [options]'

    def add_options(self):
        self.parser.add_option(
                "-l", "--list",
                action="store_true",
                dest="list",
                default=False,
                help="list available commands and exit"
        )
        self.parser.add_option(
                "-q", "--quiet",
                action="store_true",
                dest="quiet",
                default=False,
                help="don't print output"
        )
        self.parser.disable_interspersed_args()

    def get_cmd_list(self):
        pass

    def print_cmd_list(self):
        print "cmd1\ncmd2\ncmd3\n"
            
    def execute(self):
        opts, args = self.parser.parse_args()
        if opts.list:
            self.print_cmd_list()
            sys.exit(0)
        
        if not args:
            self.parser.print_help()
            sys.exit(1)

        if opts.quiet:
            ret = subprocess.call(args, stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
        else:
            ret = subprocess.call(args)


if __name__ == '__main__':
    bc = AmazonWebServicesLineInterpreter()
    bc.execute()





