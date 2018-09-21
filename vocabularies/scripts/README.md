# Scripts

Python 2.7 (not tested with Python 3) scripts for converting CSV vocabulary file to JSON-LD.

## Installation

Run the following to install dependencies:

```
cd vocabularies/scripts
python setup.py develop
```

## Running

Serialize scripts expect to be run from within this directory.

For example, this will rebuild ../json-ld/accessMessages.json from ../csv/accessMessages.csv:

```
python serialize-accessMessages.py
```
