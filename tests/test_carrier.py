"""Test Carrier

This module contains the test case for the Carrier program.

Usage
    python -m pytest tests.test_carrier
"""
import pytest
import argparse
from typing import List
from decimal import Decimal

from carrier.config import *
from carrier.helpers import *
from carrier.carrier import Carrier
from carrier.arg_parser import create_parser
from tests.utils.helpers import *

@pytest.fixture
def carrier_parser():
    return create_parser()

def run_command(parser: argparse.ArgumentParser, command: List[str]) -> Carrier:
    args = parser.parse_args(command)
    options = vars(args)
    carrier = Carrier(parser, options)
    return carrier

def test_carrier_send_invoice_for_validated_payload_with_partial_input(carrier_parser):
    command = [
       "send",
       "--invoice", 
        "t=GPL", 
        "n=GS002", 
        "Monthly Progress Report=225000"
    ]

    payload = [
        {
            'type': 'invoice',
            'from': 'me', 
            'to': 'GPL', 
            'number': 'GS002',
            'line-items': [{'Monthly Progress Report': Decimal('225000.00')}]
        }
    ]

    carrier = run_command(carrier_parser, command)
    result = carrier.payload
    assert result == payload

def test_carrier_send_invoice_for_validated_payload_with_short_form_attr_nanes(carrier_parser):
    command = [
       "send",
       "--invoice", 
        "fr=me", 
        "t=GPL", 
        "n=GS002", 
        "Monthly Progress Report=225000"
    ]

    payload = [
        {
            'type': 'invoice',
            'from': 'me', 
            'to': 'GPL', 
            'number': 'GS002',
            'line-items': [{'Monthly Progress Report': Decimal('225000.00')}]
        }
    ]

    carrier = run_command(carrier_parser, command)
    result = carrier.payload
    assert result == payload