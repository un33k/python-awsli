#!/usr/bin/env python

from awsli.base import *


class AWSZonesList(BaseCommand, AWSConnectionMixin):

    def get_formatted_item(self, item):
        formatted = {}
        formatted['name']        = item.name
        formatted['endpoint']    = item.endpoint
        return formatted

    def execute(self):
        regions = self.conn.get_all_regions()
        return self.process_response(regions)

if __name__ == '__main__':
    bc = AWSZonesList()
    bc.execute()





