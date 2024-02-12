import argparse
from carrier.config import DESCRIPTION, KEY_VALUE_ARGUMENT_HELP

def create_parser():
    parser = argparse.ArgumentParser(
        prog='carrier',
        fromfile_prefix_chars='@',
        usage='carrier [COMMAND] <arg1>[ ...<arg>n] [OPTIONS]',
        description=DESCRIPTION,
        epilog='Write it!')

    parser.add_argument("-i", "--invoices",
                        metavar="KEY=VALUE",
                        action='append',
                        nargs='+',
                        help=KEY_VALUE_ARGUMENT_HELP)
    
    parser.add_argument("-l", "--letters",
                        metavar="KEY=VALUE",
                        action='append',
                        nargs='+',
                        help=KEY_VALUE_ARGUMENT_HELP)
    
    parser.add_argument("-r", "--receipts",
                        metavar="KEY=VALUE",
                        action='append',
                        nargs='+',
                        help=KEY_VALUE_ARGUMENT_HELP)

    parser.add_argument('commands',
                           nargs='+',
                           help="carrier [COMMAND] <arg1>[ ...<arg>n] [OPTIONS]")
    
    return parser