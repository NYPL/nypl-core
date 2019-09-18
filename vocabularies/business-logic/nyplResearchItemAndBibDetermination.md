# Calculating "Is-Research" For Items and Bibs

We have a mixed catalog consisting of bibs that belong informally to the "Research" side of the house or the "Circulating" side (and a [diminishing set of bibs that belong to both](https://github.com/NYPL/sync-item-metadata-to-scsb-listener/blob/qa/data/mixed-bibs.csv)). Items also belong to either "Research" or "Circulating" (never both). Many components have a need to make this calculation (e.g. to populate the [SCC](https://www.nypl.org/research/collections/shared-collection-catalog/)). The method for determining whether a bib & item "is research" is not straightforward.

## Calculating Is-Research for Items

This is how "is-research" is determined for items in DiscoveryStorePoster:

https://github.com/NYPL-discovery/discovery-store-poster/blob/bed0d736c42613d54324f05e8d77351eeb8757a8/lib/models/item-sierra-record.js#L29-L62

 - holding location's collectionType is 'Research' (and only 'Research') OR
 - item type (aka itype, catalogItemType) collectionType includes 'Research' OR
 - is partner record (determined by nyplSource) OR
 - is electronic resource*

\* For the needs of a service that deals exclusively with items that exist in the ItemService, we can drop the electronic resource check.

## Calculating Is-Research for Bibs

This is how "is-research" is determined for bibs in DiscoveryStoreModels (which is used by [DiscoveryApiIndexer](https://github.com/NYPL-discovery/discovery-api-indexer)):

https://github.com/NYPL-discovery/discovery-store-models/blob/09653683bbfc9d0c316729b7d3dea328a13d0598/lib/models/bib.js#L16-L32

 - is partner record OR
 - has 0 items (because only a research record would exist in that state) OR
 - has at least ONE research item (as determined for items above) OR
 - its items are ALL electronic AND it has at least one location whose collectionType includes 'Research'*

\* Again, for the needs of a service that looks exclusively at bibs in the BibService, we can drop the electronic item check, so the final clause above is not relevant.

### Related: Calculating whether or not to sync items to SCSB

A similar set of checks is made by our SyncItemMetadataToSCSBListener component to determine whether or not to sync metadata to SCSB. That determination mostly matches the "is-research" determination documented above but skips the partner record check (because we don't sync partner records to SCSB) and electronic resource check (because electronic resources don't exist in ReCAP). It also leverages [a "mixed bib" CSV](https://github.com/NYPL/sync-item-metadata-to-scsb-listener/blob/qa/data/mixed-bibs.csv) to expedite* the "has at least ONE research item" check. This work is noted because it performs many similar checks to those above, but in Ruby.

https://github.com/NYPL/sync-item-metadata-to-scsb-listener/blob/0c7470aa39cd4c53313c3d70fa074f5688f4c34c/lib/bib_handler.rb#L19-L63

 - is "mixed bib" (one of the diminishing few bibs that are known [by CSV](https://github.com/NYPL/sync-item-metadata-to-scsb-listener/blob/qa/data/mixed-bibs.csv) to have both research and circulating items) OR
 - first item is research (by catalogItemType and location check, as documented above)

\* To determine whether a bib "has at least one research item", one needs to either:
 1. Calculate "is-research" for each item assocated with a bib until one is found to be research. This is the mechanism used by the DiscoveryApiIndexer because it has ready access to all items for a given bib.
 2. Determine if a bib is a "mixed bib" by checking for its id in [a CSV of known mixed bibs](https://github.com/NYPL/sync-item-metadata-to-scsb-listener/blob/qa/data/mixed-bibs.csv). If a bib is a "mixed bib", it clearly has at least one research item. If it is not a "mixed bib", then it suffices to check the *first* item associated with the bib and calculate "is-research" for that item alone.
