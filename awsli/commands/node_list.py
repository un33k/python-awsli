#!/usr/bin/env python

from awsli.base import BaseCommand, AWSConnectionMixin


class AWSNodeList(BaseCommand, AWSConnectionMixin):

    def get_formatted_item(self, item):
        formatted = {}
        for i in item.instances:
            formatted['id']              = i.id
            formatted['instance_type']   = i.instance_type
            formatted['image_id']        = i.image_id
            formatted['state']           = i.state
            formatted['ip_address']      = i.ip_address
            formatted['public_ips']      = i.private_ip_address
            formatted['region']          = str(i._placement)[:-1]
            formatted['zone']            = str(i._placement)
            return formatted
        
    def get_aws_response(self):
        """
        Added stub for prototyping
        """
        class Items(object):
            def __init__(self, instances=[]):
                self.instances = instances
        class Item(object):
            id = 1
            instance_type = str
            image_id = 'img1'
            state = 'On'
            ip_address = '1.1.1.1'
            private_ip_address = '1.0.1.0'
            _placement = [0,1,2,3]
            
        nodes = [Items([Item()])] #self.conn.get_all_instances()
        return nodes
#    def execute(self):
#        nodes = self.conn.get_all_instances()
#        return self.process_response(nodes)


if __name__ == '__main__':
    bc = AWSNodeList()
    bc.execute()
