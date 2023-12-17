"""Carrier Test Helpers

This module contains the test case for the Carrier helpers module.

Usage
    python -m unittest tests.test_helpers
"""
import unittest
from pprint import pprint
from carrier.helpers import *
from carrier.config import *
from carrier.fragments import *


class CarrierHelpersTest(unittest.TestCase):
    def setUp(self):
        self.dummy_md = Path(PurePath(TEST_DATA, 'dummy.md'))
        self.dummy_attachment = Path(
            PurePath(TEST_DATA, 'dummy-attachment.pdf'))
        self.dummy_pdf = Path(PurePath(TEST_DATA, 'dummytabloid-dummy.pdf'))
        self.indented = (
            "    Opinions about solar power have surfaced lately and though many writers have contributed considerably, I believe that the key ideas have barely had any time under the sun. Persons keeping up with developments in the solar energy space may know that we are right now going through a paradigm shift in terms of the way we view the electrical grid - the new grid looks more like the Internet.\n"
            "\n"
            "    We may tend to think of the Internet by now, as a kind of stream, 'piped' to users from a central 'source'. There is no such source. Briefly put, people create networks for themselves. These networks appear as organically, as rapidly and as pervasively as human settlements do. ISP’s eventually appear when users of these networks start to demand more bandwidth or as networks grow and become complicated.\n"
            "\n"
            "    Editor, Australia has embraced the battery network. Homes and businesses in South Australia together produce so much electricity from rooftop solar, that they are considered one of the largest generators on Australia's world-renowned interconnected grid! Thanks to batteries, solar is now a baseline power source.\n"
            "\n"
            "    Senate Bill 99: The Community Energy and Resiliency Act of 2021 authored by Senator Bill Dodd of California, was heard on the senate floor and has passed through the first house of the legislature. The idea behind this Act is that local government, with the assistance of the energy commision and the experts they qualify, would conduct community-based participatory processes to identify threats and opportunities in energy resiliency. These processes would elicit a set of projects that are specific enough to receive support when infrastructure funding starts coming.\n"
            "\n"
            "    Editor, solar free-market possibilities are too numerous to mention. First-movers in Guyana already know that self-generating is not selfish and the old adage, 'the more the merrier' rings true, as it does for the Internet. Do we want a cheaper, more resilient supply of electricity in Guyana? Perhaps it is time to take rooftop solar more seriously.\n"
        )

    def tearDown(self):
        if Path(self.dummy_pdf).is_file():
            Path(self.dummy_pdf).unlink()
    
    def test_first_letters(self):
        cases = [
            "kaieteur",
            "chronicle"
        ]
        a = first_letters('ka', cases[0])
        b = first_letters('kait', cases[0])
        c = first_letters('kai', cases[0])
        d = first_letters('kaie', cases[0])
        e = first_letters('kaieteur', cases[0])
        
        self.assertTrue(a)
        self.assertFalse(b)
        self.assertTrue(c)
        self.assertTrue(d)
    
    def test_convert_markdown_to_pdf_letter(self):
        self.assertTrue(Path(self.dummy_md).is_file())        
        self.assertTrue(Path(STYLES).is_file())
        pdf = convert_markdown_to_pdf_letter(STYLES, self.dummy_md, 'dummytabloid', TEST_DATA)
        self.assertTrue(Path(pdf).is_file())
        
    def test_return_file_name_without_suffix(self):
        self.assertTrue(Path(self.dummy_md).is_file())

        a = return_file_name_without_suffix(self.dummy_md)
        self.assertEqual(a, 'dummy')

        b = return_file_name_without_suffix('content.pdf')
        self.assertEqual(b, 'content')
    
    def test_replace_newlines(self):
        a = replace_newlines(my_address)
        self.assertEqual(
            a, "**Emille Giddings**<br>938 Section A Block X Great Diamond<br>East Bank Demerara<br>(592) 647-5005<br>")

    def test_indent_paragraphs(self):
        md_text = (
            "Opinions about solar power have surfaced lately and though many writers have contributed considerably, I believe that the key ideas have barely had any time under the sun. Persons keeping up with developments in the solar energy space may know that we are right now going through a paradigm shift in terms of the way we view the electrical grid - the new grid looks more like the Internet.\n"
            "\n"
            "We may tend to think of the Internet by now, as a kind of stream, 'piped' to users from a central 'source'. There is no such source. Briefly put, people create networks for themselves. These networks appear as organically, as rapidly and as pervasively as human settlements do. ISP’s eventually appear when users of these networks start to demand more bandwidth or as networks grow and become complicated.\n"
            "\n"
            "Editor, Australia has embraced the battery network. Homes and businesses in South Australia together produce so much electricity from rooftop solar, that they are considered one of the largest generators on Australia's world-renowned interconnected grid! Thanks to batteries, solar is now a baseline power source.\n"
            "\n"
            "Senate Bill 99: The Community Energy and Resiliency Act of 2021 authored by Senator Bill Dodd of California, was heard on the senate floor and has passed through the first house of the legislature. The idea behind this Act is that local government, with the assistance of the energy commision and the experts they qualify, would conduct community-based participatory processes to identify threats and opportunities in energy resiliency. These processes would elicit a set of projects that are specific enough to receive support when infrastructure funding starts coming.\n"
            "\n"
            "Editor, solar free-market possibilities are too numerous to mention. First-movers in Guyana already know that self-generating is not selfish and the old adage, 'the more the merrier' rings true, as it does for the Internet. Do we want a cheaper, more resilient supply of electricity in Guyana? Perhaps it is time to take rooftop solar more seriously."
        )
        r = indent_paragraphs(md_text)
        self.assertEqual(r, self.indented)

    def test_make_html_paragraphs(self):
        case = "Opinions about solar power have surfaced lately and though many writers have contributed considerably, I believe that the key ideas have barely had any time under the sun. Persons keeping up with developments in the solar energy space may know that we are right now going through a paradigm shift in terms of the way we view the electrical grid - the new grid looks more like the Internet."
        correct = "<p class='indent'>Opinions about solar power have surfaced lately and though many writers have contributed considerably, I believe that the key ideas have barely had any time under the sun. Persons keeping up with developments in the solar energy space may know that we are right now going through a paradigm shift in terms of the way we view the electrical grid - the new grid looks more like the Internet.</p>"
        self.assertEqual(make_html_paragraphs(case), correct)
    
    def test_send_email(self):
        msg = email_message_to_editor.format(Month='October', day="28")
        sent = send_email(msg, EMAIL, "Delete me. This is an authorized test.", self.dummy_attachment)
        self.assertTrue(sent)


if __name__ == '__main__':
   unittest.main()
