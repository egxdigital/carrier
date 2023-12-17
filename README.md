# carrier

A tool for generating and sending letters to the editor.

## Installation
### 1. Download
```bash
git clone https://github.com/egxdigital/carrier.git
```

### 2. Add environment variables
#### Linux
Create a .env file with the following fields

```bash
EMAIL=youremail@emails.com
OAUTH2=/path/to/google/api/oauth2/credentials.json
SOURCE=/path/to/source/markdown/files
ATTACHMENTS=/path/to/attachment/output
```

### 3. Install
Create a virtual environment for the project

```bash
python3.10 -m virtualenv env
```
Activate the environment, install the requirements and run the build command

```bash
source env/bin/activate
pip install requirements.txt
python -m build
deactivate
```
Deactivate the environment

```bash
deactivate
```
Install

```bash
python3.10 -m pip install --editable .
```
or install an editable build if you want to customize and develop

```bash
python3.10 -m pip install --editable .
```