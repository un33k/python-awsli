#!/usr/bin/env python

from boto.ec2.connection import EC2Connection
from command import BaseCommand

class AWSConnectionMixin(object):
    connection = None

    @property
    def conn(self):
        if not self.connection:
            if self.options.key and self.options.secret:
                self.connection = EC2Connection(self.options.key, self.options.secret)
            else:
                self.connection = EC2Connection()
        return self.connection






