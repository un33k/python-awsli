#!/usr/bin/env python

import os
import sys
import types
import optparse
import subprocess
from boto.ec2.connection import EC2Connection
from awsli.base import BaseCommand
from awsli.base import AWSConnectionMixin
import json

class AWSListNodes(BaseCommand, AWSCredentialsMixin, AWSConnectionMixin):

    def execute(self):
        regions = self.conn.get_all_regions()
        reglist = []
        for r in regions:
            reglist.append('{name: %s, endpoint: %s}' % (r.name, r.endpoint))
            # print json.dumps(reglist, indent=2)

if __name__ == '__main__':
    bc = AWSListZones()
    bc.execute()





