import os
from dotenv import load_dotenv
from pathlib import Path, PurePath

load_dotenv()

DESCRIPTION = 'A tool for generating and sending letters to the editor'

ROOT = Path(__file__).resolve().parent.parent
STATIC = Path(PurePath(ROOT, 'static'))
TESTS = Path(PurePath(ROOT, 'tests'))
TEST_DATA = Path(PurePath(TESTS, 'data'))
STYLES = Path(PurePath(STATIC, 'basic.css'))

SOURCE = os.getenv('LETTERS')
ATTACHMENTS = os.getenv('ATTACHMENTS')
OAUTH2 = Path(os.getenv('OAUTH2'))
EMAIL = os.getenv('EMAIL')


class colors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ERROR():
    bad_command = 'invalid command!'
    bad_directory = 'invalid destination directory!'
    bad_file = 'invalid input file'
    bad_source_file_name = 'invalid source file name'
    too_many_arguments='too many arguments'
    no_such_file = 'file does not exist'
    no_tabloids = 'no tabloid selected!'
