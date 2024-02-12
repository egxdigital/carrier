"""Carrier

This module contains the main function definitions for the Carrier program.

Usage
    carrier generate content.md -t k s c
    carrier generate content.md -t=ksc
    carrier generate content.md -ksc
    carrier generate content.md --kaieteur --stabroek --chronicle
    carrier generate content.md -t kaieteur stabroek chronicle
    carrier generate -p content.md -k -s -c
    carrier generate content.md -p -ksc
    carrier send content.md -e -r="This is a test email to see if the send command works"

    carrier generate -l=content.md -t=ksc
    carrier generate-invoice --for=GUYSOL --date=02-01-2024 --items "Monthly Progress Report for Period Jan 1 - 31, 2024"=225000
    carrier send-invoice --for=GUYSOL --date=02-01-2024 --items "Monthly Progress Report for Period Jan 1 - 31, 2024"=225000
    carrier send --invoice to=GUYSOL "Monthly Progress Report for Period Jan 1 - 31, 2024"=225000 number=GS002 contract=C2-003
    carrier send --invoice to=GUYSOL number=GS002 --items="Monthly Progress Report for Period Feb 1 - 29, 2024"=225000
    
"""
import inspect
import argparse
from pprint import pprint
from typing import List
from datetime import datetime
from decimal import Decimal
from carrier.config import *
from carrier.helpers import *
from carrier.fragments import *


class Carrier():
    """
    A class used to represent an instance of the Carrier program.

    Attributes
    ----------
    parser : argparse.ArgumentParser
        Object for parsing command line strings into Python objects.
    options : dict
        Dictionay containing arguments passed to Carrier object.        

    Methods
    -------
    generate()
        Takes a markdown file and generates a PDF email attachment.
    send()
        Sends the email attachments and a message to the selected recipients.
    """
    def __init__(self, parser, options):
        self.valid_commands = {
            'generate': self.generate,
            'send': self.send
        }

        self.standard_attribute_types = {
            'invoices': {
                'from': 'string',
                'to': 'string',
                'number': 'string',
                'accept_in': 'string'
            }
        }

        self.parser = parser
        self.options = options
        self.command = ''

        self.payload = []

        self._validate_command()
        self._validate_arguments_and_prepare_payload()
        self.valid_commands[self.command]()

    def __repr__(self):
        return (
            f'command: {self.command}\n'
            f'options: {self.options}\n'
            f'payload: {self.payload}\n'
            )
    
    def __str__(self):
        return (
            f"carrier {self.command}"
        )
    
    def _validate_command(self):
        if self.options['commands'][0] not in self.valid_commands:
            self.parser.error('bad command!')
        self.command=self.options['commands'][0]
    
    def _validate_arguments_and_prepare_payload(self):
        invoices = self.options.get('invoices')
        letters = self.options.get('letters')
        receipts = self.options.get('receipts')

        if invoices:
            #print('Hit')
            for invoice in self.options['invoices']:
                invoice_dict = {
                    'type': 'invoice',
                    'line-items': []
                }
                for attr_str in invoice:
                    attr_name, attr_val = attr_str.split('=')
                    full_attr_name = self.__validate_attr_name(attr_name, 'invoices')
                    attr_type = self.standard_attribute_types['invoices'].get(full_attr_name)
                
                    if attr_type:
                        # If attribute is one of the standard attributes
                        interpreted_value = self.__interpret_value(full_attr_name, attr_val, attr_type)
                        invoice_dict[full_attr_name] = interpreted_value
                    else:
                        # Attribute is an invoice line-item
                        invoice_dict['line-items'].append({full_attr_name: self.__interpret_value(full_attr_name, attr_val, Decimal)})
                
                self.payload.append(invoice_dict)
            
            self.__validate_and_prepare_payload_before_processing()

    def __validate_attr_name(self, attr_name, document):
        for full_name in self.standard_attribute_types[document]:
            if full_name.startswith(attr_name):
                return full_name
        return attr_name

    def __interpret_value(self, attr_name, attr_value, attr_type):
        try:
            if attr_type == 'string':
                return str(attr_value)
            elif attr_type == 'integer':
                return int(attr_value)
            elif attr_type == 'float':
                return float(attr_value)
            elif attr_type == Decimal:
                return decimal_quantize(attr_value)
            else:
                return attr_value
        except Exception as e:
            raise self.parser.error(
                f"Error interpreting attribute: {e}\n"
                f"Attribute `{attr_name}` value `{attr_value}` cannot be coerced to type: {attr_type}"
            )
    
    def __validate_and_prepare_payload_before_processing(self):
        for document in self.payload:
            if document['type'] == 'invoice':
                sender, recipient = self.___interpret_sender_recipient(document)
                document['from'] = sender
                document['to'] = recipient
                

    def ___interpret_sender_recipient(self, document):
        sender = document.get('from')
        recipient = document.get('to')
        
        if sender in ['me', 'emille'] or sender == None:
            sender = {
                'name': SENDER,
                'address': ADDRESS,
                'phone': PHONE
            }

        if recipient in ['GPL', 'GUYSOL']:
            recipient = {
                'name': GUYSOL_PC,
                'title': GUYSOL_PC_TITLE,
                'address': GUYSOL_ADDRESS,
                'phone': GUYSOL_TELEPHONE
            }
        
        return sender, recipient

    @classmethod
    def generate(self):
        pass

    @classmethod
    def send(self):
        pass
