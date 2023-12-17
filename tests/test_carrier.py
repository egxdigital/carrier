"""Test Carrier

This module contains the test case for the Carrier program.

Usage
    python -m unittest tests.test_carrier
"""
import unittest
from carrier.helpers import *
from carrier.carrier import *


class CarrierTest(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser(
            prog='carrier',
            fromfile_prefix_chars='@',
            usage='carrier [options] <command> <arg1>',
            description='<desc>',
            epilog='Build it!')

        # Add arguments here
        parser.add_argument('-d', '--destination',
                            action='store',
                            type=str,
                            required=False,
                            help='')
        parser.add_argument('-m', '--message',
                            action='store_true',
                            required=False,
                            help='modifies something')
        parser.add_argument('-p', '--pdf',
                            action='store_true',
                            required=False,
                            help='modifies something')
        parser.add_argument('-k', '--kaieteur',
                            action='store_true',
                            required=False,
                            help='modifies something')
        parser.add_argument('-s', '--stabroek',
                            action='store_true',
                            required=False,
                            help='modifies something')
        parser.add_argument('-c', '--chronicle',
                            action='store_true',
                            required=False,
                            help='modifies something')
        parser.add_argument('-g', '--guyanatimes',
                        action='store_true',
                        required=False,
                        help='guyana times letter to the editor')
        parser.add_argument('-r', '--subject',
                            action='store',
                            type=str,
                            required=False,
                            help='subject line for email sendout')    
        parser.add_argument('-t', '--tabloid',
                            action='store',
                            nargs='+',
                            type=str,
                            required=False,
                            help='modifies something')
        parser.add_argument('commands',
                            nargs='+',
                            help="use a command eg. init or start")

        self.parser = parser
        self.k_dummy = Path(PurePath(ATTACHMENTS, 'kaieteur-dummy.pdf'))
        self.c_dummy = Path(PurePath(ATTACHMENTS, 'chronicle-dummy.pdf'))

    def tearDown(self):
        for dummy in [self.k_dummy, self.c_dummy]:
            if Path(dummy).is_file():
                Path(dummy).unlink()
    
    def test_generate(self):
        dummy_md = Path(PurePath(TEST_DATA, 'dummy.md'))
        command = argparse.Namespace(
            destination=None,
            message=False,
            pdf=True,
            kaieteur=True,
            stabroek=False,
            chronicle=True,
            guyanatimes=False,
            tabloid=None,
            commands=['generate', dummy_md]
        )
        args = command
        options = vars(args)
        carrier = Carrier(self.parser, options)
        
        dummy_pdf = [
            self.k_dummy,
            self.c_dummy
        ]
        
        for pdf in dummy_pdf:
            self.assertTrue(Path(pdf).is_file())

if __name__ == '__main__':
    unittest.main()
