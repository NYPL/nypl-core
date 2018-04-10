# Update Note labels

This script generates marc mappings for Bib Notes fields from MARC Discovery Model Mappings Google sheet ("Notes" tab).

## Usage

Export the Notes tab to, say, "my-csv-export-of-the-notes-tab.csv". Then:

```
npm i
node parse my-csv-export-of-the-notes-tab.csv
```

This will print the new Notes mapping to stdout, which should be folded into field-mapping-bib.json.

The script takes an optional `--save` flag to update field-mapping-bib.json for you, but that may generate a lot more git diff noise that you like because it reformats the json (using `JSON.stringify` with 2-character indent).
