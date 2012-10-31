# -*- coding: utf-8 -*-

import unittest
import sys
import logging

class TestAWSLIFunctions(unittest.TestCase):

    def setUp(self):
        self.log= logging.getLogger( "TestAWSLIFunctions" )


    def test_manager(self):
        pass

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestAWSLIFunctions" ).setLevel( logging.DEBUG )
    unittest.main()


