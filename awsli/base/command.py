import sys, os
import optparse
import json
import cmd

class BaseCommand(object):
    def __init__(self, load_default_options=True, *args, **kwargs):
        self.install_optparse()
        if load_default_options:
            self.set_default_options()
        self.add_options()
        self.options, self.args = {},[]
        #too early to pass inputs here; line interpreter may not be initialized yet
#        self.options, self.arguments = self.parser.parse_args()

    def install_optparse(self):
        #strip .py from filename
        self.parser = optparse.OptionParser(prog = os.path.basename(sys.argv[0])[:-3])
        
    def set_default_options(self):
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
#        #needed for determining cmd interface options from default options
#        self.default_options = self.parser._long_opt.keys()
#        self.default_options.extend(self.parser._short_opt.keys())
        
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
    
    def get_aws_response(self):
        """
        Overide and implement aws command specific actions here 
        and return output
        """
        return 'Options: %s\nArgs: %s\nMessage: Must overload get_response'%(self.options,self.arguments)
    
    def execute(self, args=sys.argv[1:]):
        """
        May be overided as well instead of get_response
        """
        self.options, self.arguments = self.parser.parse_args(args)
        response = self.get_aws_response()
        return self.process_response(response)

if __name__ == '__main__':
    bc = BaseCommand()
    bc.execute()