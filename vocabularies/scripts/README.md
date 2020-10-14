# Scripts

Python 3.4+ scripts for converting CSV vocabulary file to JSON-LD.

## Installation

Run the following to install dependencies:

``` bash
cd vocabularies/scripts
pip install -r requirements.txt
```

## Running

Serialize scripts expect to be run from within this directory.

For example, this will rebuild ../json-ld/accessMessages.json from ../csv/accessMessages.csv:

``` bash
python serialize-accessMessages.py
```
