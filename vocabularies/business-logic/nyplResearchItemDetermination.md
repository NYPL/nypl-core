**The following boolean OR logic determines whether a given item record will be ingested into Discovery (SCC).**

An item is determined to be Research and is ingested into Discovery (SCC) if:

* itype <= 100 (or, as an exception, has an RFVC itype: 132, 133, 134, 135, 142) (see [catalogitemtypes.csv](https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/catalogItemTypes.csv))OR
* it's a partner record OR
* it's an e-resource OR
* it holding-location (item location code) collectionType is 'Research' ([see locations.csv](https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/locations.csv))

**Non-research items are suppressed.**
