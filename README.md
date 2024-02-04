# carrier

A tool for generating and sending letters to the editor.

## Installation
### 1. Download
```bash
git clone https://github.com/egxdigital/carrier.git Carrier
```

### 2. Add environment variables
#### Linux
Create a .env file with the following fields

```bash
EMAIL=example@example.com
OAUTH2=/path/to/google/api/oauth2/credentials.json
SOURCE=/path/to/source/markdown/files
ATTACHMENTS=/path/to/attachment/output
```

### 3. Install
Ensure that your user is the owner of the project root and all of its contents

```bash
sudo chown -R /path/to/repository/root
```

Create a virtual environment for the project

```bash
python3.10 -m virtualenv env
```

Install editable build (in development mode)

```bash
./install.sh
```