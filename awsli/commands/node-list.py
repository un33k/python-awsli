#!/usr/bin/env python

import os
import sys
import types
import optparse
import subprocess
from boto.ec2.connection import EC2Connection
from awsli.base import *
import json

class AWSNodeList(
        BaseCommand,
        AWSDefaultMixin,
        AWSCredentialMixin,
        AWSConnectionMixin
    ):

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

    def execute(self):
        nodes = self.conn.get_all_instances()
        print nodes
        print dir(nodes)
        # nodelist = []
        # for i in nodes:
            # nodelist.append('{name: %s}' % (i.name))
        # print json.dumps(reglist, indent=2, sort_keys=True)

if __name__ == '__main__':
    bc = AWSNodeList()
    bc.execute()





