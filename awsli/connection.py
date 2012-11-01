
from boto.ec2.connection import EC2Connection

from command import BaseCommand


class AmazonWebServicesConnection(BaseCommand):
    """ Handles various type of connections to Amazon Web Services """
    def __init__(self, *args, **kwargs):
        super(AmazonWebServicesConnection, self).__init__(*args, **kwargs)
        self._conn = None

    @property
    def conn(self):
        if self._conn:
            return self._conn

        self.parser.add_option(
                "--key",
                dest="key",
                help="aws access key id"
        )
        self.parser.add_option(
                "--secret",
                dest="secret",
                help="aws access secret key"
        )
        opts, args = self.parser.parse_args()
        if opts.key and opts.secret:
            self._conn = EC2Connection(opts.key, opts.secret)
        else:
            self._conn = EC2Connection()
        return self._conn


    def cmd_list_regions(self):
        """
        Get AWS regions
        
        Usage: %prog {0} [options]
        """
        
        regions = self.conn.get_all_regions()
        print regions


if __name__ == '__main__':
    bc = AmazonWebServicesConnection()
    bc.execute()


