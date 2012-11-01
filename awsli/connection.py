from decorator import decorator
from boto.ec2.connection import EC2Connection

from command import BaseCommand


class AmazonWebServicesConnection(BaseCommand):
    """ Handles various type of connections to Amazon Web Services """
    def __init__(self, *args, **kwargs):
        super(AmazonWebServicesConnection, self).__init__(*args, **kwargs)

    @property
    def conn(self):
        return EC2Connection()

    def cmd_list_regions(self):
        """ Get AWS regions """
        self.parser.add_option(
                "-l", "--list",
                action="store_true",
                dest="list",
                default=False,
                help="show list of commands and exit"
        )
        
        regions = self.conn.get_all_regions()
        print regions


if __name__ == '__main__':
    bc = AmazonWebServicesConnection()
    bc.execute()


