"""Carrier Main

This module contains the entry point code for the Carrier program.
"""
from carrier.arg_parser import create_parser
from carrier.carrier import Carrier

def main():
    parser = create_parser()
    
    args = parser.parse_args()
    
    options = vars(args)
    
    carrier = Carrier(parser, options)
    
    print(repr(carrier))

    return carrier 


if __name__ == '__main__':
    main()