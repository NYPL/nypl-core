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
 - has at least ONE research item OR
 - its items are ALL electronic AND it has at least one location whose collectionType includes 'Research'*

\* Again, for the needs of a service that looks exclusively at bibs in the BibService, we can drop the electronic item check, so the final clause above is not relevant.

The same set of checks is made by our SyncItemMetadataToSCSBListener component:

https://github.com/NYPL/sync-item-metadata-to-scsb-listener/blob/0c7470aa39cd4c53313c3d70fa074f5688f4c34c/lib/bib_handler.rb#L19-L63

 - is "mixed bib" (one of the diminishing few bibs that are known [by CSV](https://github.com/NYPL/sync-item-metadata-to-scsb-listener/blob/qa/data/mixed-bibs.csv) to have both research and circulating items) OR
 - first item is research (by catalogItemType and location check, as documented above)
