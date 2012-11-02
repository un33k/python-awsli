#!/usr/bin/env python

from command import BaseCommand

class AWSCredentialsMixin(object):

    def add_options(self):
        self.parser.add_option(
                "-k", "--key",
                dest="key",
                help="amazon web services access key id. aka: aws_access_key_id"
        )
        self.parser.add_option(
                "-s", "--secret",
                dest="secret",
                help="amazon web services secret access key. aka: aws_secret_access_key"
        )





