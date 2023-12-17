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
"""
import inspect
import argparse
from pprint import pprint
from typing import List
from datetime import datetime
from carrier.config import *
from carrier.helpers import *
from carrier.fragments import *
from carrier.exceptions import *


class Carrier():
    """
    An class used to represent an instance of the Carrier program.

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

        self.tabloids = {
            'kaieteur': False,
            'stabroek': False,
            'chronicle': False,
            'guyanatimes': False,
            'inewsgy': False,
            'demwaves': False,
            'newsroom': False,
            'oilnow': False,
            'village_voice': False,
            'engineer': False
        }

        self.parser = parser
        self.options = options
        self.command = ''
        self.attachments: List[Path] = []
        self.payload = {
            'kaieteur': dict(),
            'stabroek': dict(),
            'chronicle': dict(),
            'guyanatimes': dict(),
            'inewsgy': dict(),
            'demwaves': dict(),
            'newsroom': dict(),
            'oilnow': dict(),
            'village_voice': dict(),
            'engineer': dict()
        }
        self.attachment_source = ATTACHMENTS

        self._validate_command()
        self._validate_attachments()
        self._parse_options()
        
        handle_command = self.valid_commands[self.command]
        handle_command()

    def __str__(self):
        return (
            'command: {}\n'
            'options: {}\n'
            'tabloids: {}\n'
            'content: {}\n'
        ).format(
            self.command,
            self.options,
            self.tabloids,
            self.attachments,
        )

    def _validate_tabloids(self):
        all_tabloids = set(list(self.tabloids.values()))
        if all_tabloids == {False}:
            self.parser.error(ERROR.no_tabloids)
    
    def _validate_command(self):
        if self.options['commands'][0] not in self.valid_commands:
            self.parser.error('bad command!')
        self.command=self.options['commands'][0]
    
    def _validate_attachments(self):
        """Check whether the referenced markdown file exists. Either the name of the file or the absolute path
        to the file can be used as a reference to the file.
        """
        arguments = self.options['commands'][1:]
    
        if len(arguments) > 1:
            self.parser.error(ERROR.too_many_arguments)
        
        for arg in arguments:
            if Path(arg).is_file():
                if Path(arg).suffix in ['.md']:
                    self.attachments += [arg]
                else:
                    self.parser.error(ERROR.bad_file + ": " + str(Path(arg)))
            if not Path(arg).is_file():
                source_markdown = Path(PurePath(SOURCE, f"{arg}.md"))
                if Path(source_markdown).is_file():
                    self.attachments += [source_markdown]
                else:
                    self.parser.error(ERROR.bad_source_file_name + ": " + arg)
    
    def _parse_options(self):
        tabloid = self.options['tabloid']
        destination = self.options['destination']
        
        if destination != None:
            if Path(destination).is_dir():
                self.attachment_source = destination
            self.parser.error(ERROR.bad_directory)
        
        if tabloid != None:
            if len(tabloid) == 1:
                if ',' in tabloid[0]:
                    chosen_tabloids = tabloid[0].split(',')
                    for t in chosen_tabloids:
                        for t_name in self.tabloids:
                            if first_letters(t, t_name):
                                self.tabloids[t_name] = True
                if ',' not in tabloid[0]:
                    for t_name in self.tabloids:
                        if first_letters(tabloid[0], t_name):
                            self.tabloids[t_name] = True
            if len(tabloid) > 1:
                for inp in tabloid:
                    for t_name in self.tabloids.keys():
                        if first_letters(inp, t_name):
                            self.tabloids[t_name] = True
        
        for name in self.tabloids:
            if self.options[name]:
                self.tabloids[name] = True
    
    def generate(self):
        self._validate_tabloids()

        for it in self.attachments:
            for tabloid, yes in self.tabloids.items():
                if yes:            
                    pdf_file = convert_markdown_to_pdf_letter(
                        styles=STYLES,
                        md=it,
                        tabloid=tabloid,
                        loc=ATTACHMENTS)
                    self.payload[tabloid]['pdf'] = pdf_file

                    print(
                        colors.BOLD + 
                        f"Letter PDF titled '{Path(it).stem}' created for {tabloid}" + 
                        colors.ENDC + " @ " + 
                        f"{self.payload[tabloid]['pdf']}"
                    )
    
    def send(self):
        self._validate_tabloids()

        for tabloid, yes in self.tabloids.items():
            if yes:
                # Send the latest version
                # Generate a new PDF before send
                # TODO: Check file timestamps
                self.generate()
                letter_pdf = self.payload[tabloid]['pdf']
                if Path(letter_pdf).is_file():
                    send_email(
                        message=email_message_to_editor_with_credentials.format(
                            Month=datetime.now().strftime("%B"),
                            day=datetime.now().strftime("%d")
                        ),
                        recipient=emails[tabloid],
                        subject=f"Letter to the editor: {self.options['subject']}",
                        attachment=letter_pdf,
                    )

def main():
    parser = argparse.ArgumentParser(
        prog='carrier',
        fromfile_prefix_chars='@',
        usage='carrier [COMMAND] <arg1>[ ...<arg>n] [OPTIONS]',
        description=DESCRIPTION,
        epilog='Write it!')

    parser.add_argument('-d', '--destination',
                        action='store',
                        type=str,
                        required=False,
                        help='')
    parser.add_argument('-e', '--engineer',
                        action='store_true',
                        required=False,
                        help='engineer letter to the engineer')  
    parser.add_argument('-k', '--kaieteur',
                        action='store_true',
                        required=False,
                        help='kaieteur letter to the editor')
    parser.add_argument('-s', '--stabroek',
                        action='store_true',
                        required=False,
                        help='stabroek letter to the editor')
    parser.add_argument('-c', '--chronicle',
                        action='store_true',
                        required=False,
                        help='chronicle letter to the editor')
    parser.add_argument('-g', '--guyanatimes',
                        action='store_true',
                        required=False,
                        help='guyana times letter to the editor')
    parser.add_argument('-i', '--inewsgy',
                        action='store_true',
                        required=False,
                        help='inewsgy letter to the editor')
    parser.add_argument('-w', '--demwaves',
                        action='store_true',
                        required=False,
                        help='demwaves letter to the editor')
    parser.add_argument('-n', '--newsroom',
                        action='store_true',
                        required=False,
                        help='newsroom letter to the editor')
    parser.add_argument('-o', '--oilnow',
                        action='store_true',
                        required=False,
                        help='oilnow letter to the editor')
    parser.add_argument('-v', '--village-voice',
                        action='store_true',
                        required=False,
                        help='village voice letter to the editor')
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
                        help='tabloid names partial or full eg. "k" or "kaie"')
    parser.add_argument('commands',
                           nargs='+',
                           help="carrier [COMMAND] <arg1>[ ...<arg>n] [OPTIONS]")

    args = parser.parse_args()

    options = vars(args)

    carrier = Carrier(parser, options)
