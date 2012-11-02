#!/usr/bin/env python

import os
from collections import OrderedDict
from awsli.base import *


class AWSNodeList(BaseCommand, AWSConnectionMixin):

    def get_formatted_item(self, item):
        node = {}
        for i in item.instances:
            node['id']              = i.id
            node['instance_type']   = i.instance_type
            node['image_id']        = i.image_id
            node['state']           = i.state
            node['ip_address']      = i.ip_address
            node['public_ips']      = i.private_ip_address
            node['region']          = str(i._placement)[:-1]
            node['zone']            = str(i._placement)
            return node

    def execute(self):
        nodes = self.conn.get_all_instances()
        return self.process_response(nodes)


if __name__ == '__main__':
    bc = AWSNodeList()
    bc.execute()
