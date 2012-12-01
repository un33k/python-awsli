#!/usr/bin/env python

from awsli.base import *
import sys


class AWSZonesList(BaseCommand, AWSConnectionMixin):

    def get_formatted_item(self, item):
        formatted = {}
        formatted['name']        = item.name
        formatted['endpoint']    = item.endpoint
        return formatted
    
    def get_aws_response(self):
        regions = self.conn.get_all_regions()
        return regions
    
#    def execute(self, args=sys.argv[1:]):
#        self.options, self.arguments = self.parser.parse_args([args])
#        regions = self.conn.get_all_regions()
#        return self.process_response(regions)

if __name__ == '__main__':
    bc = AWSZonesList()
    bc.execute()





