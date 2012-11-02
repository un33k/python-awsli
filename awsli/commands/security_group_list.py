#!/usr/bin/env python

from awsli.base import *

class AWSSecurityGroupList(BaseCommand, AWSConnectionMixin):

    def execute(self):
        groups = {}
        regions = self.conn.get_all_regions()
        for i in regions:
            region_conn = i.connect()
            sg = region_conn.get_all_security_groups()
            groups[i.name] = {}
            for j in sg:
                groups[i.name][j.name] = {}
                groups[i.name][j.name]['id'] = j.id
                sec_rules = []
                for r in j.rules:
                    rule_dict = {}
                    rule_dict['ip_protocol'] = r.ip_protocol
                    rule_dict['port_range'] = '{0}-{1}'.format(r.from_port, r.to_port)
                    rule_dict['ipRanges'] = r.ipRanges.strip()
                    sec_rules.append(rule_dict)
                groups[i.name][j.name]['rules'] = sec_rules
        return self.process_response(groups)

if __name__ == '__main__':
    bc = AWSSecurityGroupList()
    bc.execute()

