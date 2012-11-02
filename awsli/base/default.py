#!/usr/bin/env python

from command import BaseCommand

class AWSDefaultMixin(object):

    def __init__(self, *args, **kwargs):
        self.parser.set_defaults(config_file='~/.awsli', public_key='~/.ssh/id_rsa.pub')



