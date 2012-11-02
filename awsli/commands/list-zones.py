#!/usr/bin/env python

import os
import sys
import types
import optparse
import subprocess
from boto.ec2.connection import EC2Connection
from awsli.base import *


class AWSListZones(BaseCommand, AWSCredentialsMixin, AWSConnectionMixin):

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
        regions = self.conn.get_all_regions()
        reglist = []
        for r in regions:
            # print >> sys.stderr, '{name: %s, endpoint: %s}' % (r.name, r.endpoint)
            reglist.append('{name: %s, endpoint: %s}' % (r.name, r.endpoint))
        import json
        print json.dumps(reglist, indent=2, sort_keys=True)

if __name__ == '__main__':
    bc = AWSListZones()
    bc.execute()





