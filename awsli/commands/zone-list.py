#!/usr/bin/env python

import os
import sys
import types
import optparse
import subprocess
from boto.ec2.connection import EC2Connection
from awsli.base import *


class AWSZonesList(BaseCommand, AWSConnectionMixin):

    def get_formatted_item(self, item):
        return '{name: %s, endpoint: %s}' % (item.name, item.endpoint)

    def execute(self):
        regions = self.conn.get_all_regions()
        return self.process_response(regions)

if __name__ == '__main__':
    bc = AWSZonesList()
    bc.execute()





