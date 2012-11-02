import sys
import optparse
import json

class BaseCommand(object):
    def __init__(self, *args, **kwargs):
        self.install_optparse()
        self.parser.set_defaults(
            config_file='~/.awsli',
            public_key='~/.ssh/id_rsa.pub'
        )
        self.parser.add_option(
                "-k", "--key",
                dest="key",
                help="amazon web services access key id. aka: aws_access_key_id"
        )
        self.parser.add_option(
                "-s", "--secret",
                dest="secret",
                help="amazon web services secret access key. aka: aws_secret_access_key"
        )
        self.parser.add_option(
                "-j", "--json",
                action="store_true",
                dest="json",
                default=False,
                help="print output as json when possible"
        )
        self.parser.add_option(
                "-r", "--raw",
                action="store_true",
                dest="raw",
                default=False,
                help="print output raw - as is"
        )

        self.add_options()
        self.options, self.arguments = self.parser.parse_args()

    def install_optparse(self):
        self.parser = optparse.OptionParser()

    def is_iterable(self, obj):
        try:
            iter(obj)
        except TypeError:
            return False
        return True
    
    def is_string(self, obj):
        return isinstance(obj, basestring)

    def is_dict(self, obj):
        return isinstance(obj, dict)

    def is_list(self, obj):
        return isinstance(obj, list)

    def add_options(self):
        pass

    def print_help(self, message='', usage=''):
        print >> sys.stderr, message
        self.parser.print_help()

    def print_output(self, output):
        if output:
            if self.options.raw:
                print output
            elif self.options.json:
                print json.dumps(output, indent=2, sort_keys=True)
            elif self.is_iterable(output):
                for i in output:
                    print i
            else:
                print output

    def get_formatted_item(self, item):
        return item

    def get_output(self, response):
        data = []
        if self.options.raw:
            data = response
        elif self.is_string(response):
            data = [response]
        elif self.is_dict(response):
            data = [response]
        elif self.is_list(response):
            for i in response:
                data.append(self.get_formatted_item(i))

        return data

    def process_response(self, response):
        output = self.get_output(response)
        return self.print_output(output)

    def execute(self):
        response = 'must overload execut'
        return process_response(response)

if __name__ == '__main__':
    bc = BaseCommand()
    bc.execute()