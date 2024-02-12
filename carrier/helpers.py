"""Carrier Helpers

This module contains the helper function definitions for the Carrier program.
"""
import textwrap
from datetime import datetime
from pathlib import Path, PurePath
from decimal import Decimal, ROUND_HALF_UP

from weasyprint import HTML, CSS
from weasyprint.document import Document

import yagmail

from carrier.config import *
from carrier.fragments import *


def decimal_quantize(amt: str) -> Decimal:
    """Takes a currency amount as a string and returns a Decimal value stored to two decimal places

    Args:
        amt (str): dollar amount

    Returns:
        Decimal: value to two decimal places
    """
    return Decimal(amt).quantize(
        Decimal('0.01'),
        rounding=ROUND_HALF_UP
    )

def first_letters(inp: str, ref: str):
    return inp == ref[0:len(inp)]

def convert_markdown_to_pdf_letter(styles, md, tabloid, loc=ATTACHMENTS):
    """Takes a path to the PDF stylesheet, path to the source markdown file, the tabloid as a string, 
    a path to the destination for the PDF and creates the PDF at destination."""
    try:
        with open(md, 'r') as md_reader:
            md_text = md_reader.read()
            content = make_html_paragraphs(md_text.strip())
            letter = letter_to_editor.format(
                my_address=(addresses['engineer']),
                date=datetime.now().strftime("%Y-%m-%d"),
                tabloid_address=addresses[tabloid],
                message=content
            )
            letter_html = replace_newlines(letter)
            doc = HTML(string=letter_html)
    except Exception as e:
        print(f"{type(e)}: {e}")
    else:
        pdf_name = f"{tabloid}-" + return_file_name_without_suffix(md, '.pdf')
        dest = Path(PurePath(loc, pdf_name))
        layout = doc.render(stylesheets=[CSS(styles)])
        pdf = layout.write_pdf(target=dest)
        return dest

def return_file_name_without_suffix(path, ext=''):
    return Path(path).name.replace(Path(path).suffix, ext)

def replace_newlines(st, rep='<br>'):
    return st.replace('\n', rep)

def indent_paragraphs(st: str):
    paragraphs = st.split('\n\n')
    result = ""
    for p_no, p in enumerate(paragraphs):
        newline = "\n"        
        if p_no != len(paragraphs)-1:
            newline += "\n"
        result += textwrap.fill(
            p,
            initial_indent=' ' * 4,
            drop_whitespace=False,
            replace_whitespace=False,
            width=9999
        ) + newline
    
    return result

def make_html_paragraphs(st: str):
    paragraphs = st.split('\n\n')
    result = ""
    for p in paragraphs:
        result += f"<p class='indent'>{p}</p>"
    return result

def send_email(message:str, recipient:str, subject:str, attachment: Path):
    try:
        yag = yagmail.SMTP(EMAIL, oauth2_file=OAUTH2)
        yag.send(
            to=recipient,
            subject=subject,
            contents=message,
            attachments=attachment,
        )
    except Exception as e:
        print(type(e).__name__, e)
    else:
        print(colors.BOLD + f"Letter sent to {recipient}:" + colors.ENDC, Path(attachment).stem)
        return True