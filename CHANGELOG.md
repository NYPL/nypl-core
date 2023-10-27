# CHANGELOG

### v2.8
 - Add customer code AS to M2 Customer codes with scholar room deliverableTo codes

### v2.7
 - Make mas82 and mab88 requestable to mab
 - m2 codes XS only deliverable to AA and XP only deliverable to AM
 
### v2.6
 - Make mal82 requestable
 - Fix location CSV & serialization issues [documented here](https://github.com/NYPL/nypl-core/pull/127)

### v2.5
 - first round of M1 locations marked requestable: mab82,maf82,mag82,mai82,map82
 - mai removed as delivery location for all location codes

### v2.4
 - remove deliverableTo from M2 items
 - add deliverableToResolution to m2 and recap locations.csv entries
 - update serializer to accomodate new property

### v2.03
 - Split LPA `my*` location codes into `lp*` and `pa*` codes, representing Circulating and Research locations.

### v2.02
 - remove trailing whitespace from status label

### v2.0
 - ROM-COM v1.0 release
 - Add m2CustomerCode csv, json-ld, and serializer script
 - Add associated m2 customer codes to locations
 - Update m2 locations requestability to 'true'

### v1.74
 - add location mab01

### v1.73
 - Add locations bur51 and bu, add catalogItemType 39

### v1.72
 - Remove (ReCAP) qualifier from status:na
 - Change id for Supervised Use status from s to su for uniqueness

### v1.71
 - Add missing M2 locations: mal98, mal99

### v1.70
 - Change associated sierra location for customer code NX from 'max' to 'ls'

### v1.69
 - Add OL recap customer code

### v1.68
 - Add formatLiteral to item field mapping

### v1.67
 - Change location label for 'map' to reflect its reopening.

### v1.66
 - Add new bib field mapping for OCLC numbers in marc 001

### v1.65
 - Add item.dueDate to field mapping

### v1.64
 - Make customer code NS ineligible for EDD

### v1.63
 - Add Aeon properties to field-mapping

### v1.62
 - replace PF customer codes with new spreadsheet values

### v1.61
 - add missing customer codes from spreadsheet to customer code PF

### v1.60
 - add volume raw, volume range, format, type, date raw, and date range properties to item field mapping

### v1.56
 - Rename parallelPublisher to parallelPublisherLiteral in field-mapping-bib to
   match convention.

### v1.55
 - Ensure all entries in field-mapping-bib that have "parallel" field
   counterparts are configured either with explicit `subfields` or
   `excludedSubfields`

### v1.54
 - Reconfigure how parallels are related in field-mapping-bib using isParallelFor

### v1.53
- Temporarily change the label for "map" to "Schwarzman Building -  Map
  Division (Temporary Service in Room 121)" to ensure RC considers it as open

### v1.52
- Fix mistake in field-mapping-bib.json SubjectLiteral -> parallelSubjectLiteral

### v1.51
- fix map08 typo

### v1.49
- Add ReCAP Customer Code to item field mapping

### v1.48
- Add Edition Statement
- Add Parallel Fields

### v1.47
- Add mapp8, mapp9, map32, map42
- Update other map locations

### v1.46
- Remove NF Customer Code
- Add map08 location code

### v1.45
- Add new field mapping for OCLC number

### v1.44
- Add new field mappings for Added Titles

### v1.43
- Remove "fancy" hyphens (U+0096) from 5 locations

### v1.42
- Update labels for microform rooms

### v1.41
- Add new ptype 75 for Schomburg Scholar

### v1.40
- Add missing HL Customer Code HV

### v1.39
- Change to label for location mab82
- Add HL Customer Codes

### v1.38
- Remove BPSE from locations

### v1.37
 - Add nypl-source-mapping.json

### v1.36
 - Add Harvard to orgs

### v1.35
 - Add unrequestable ReCAP location rcx28

### v1.34
 - Add five new ReCAP locations

### v1.33
 - Remove outdated locations in csv and json-ld

### v1.32
 - Update locations csv and json with new location codes

### v1.31
 - Changes `recapCustomerCode:JS` > `nypl:eddRequestable` to `true`

### v1.30
 - Adds `ptype:120`, `ptype:121` for Easy Borrowing

### v1.29
 - Adds Scholar Rm 217 as `nyplLocation:mal17`, `recapCustomerCodes:0D`
 - Adds `ptype:76` for Scholar Room 217

### v1.28
 - Adds pTypes 93, 94, and 95

### v1.27
 - Adds catalogItemType:221 "J Tablet - LaunchPads"

### v1.26
 - Adds lsc-oi suppressed location

### v1.25
 - Adds catalogItemType:155 (Read-Along Book)

### v1.24
 - Adds new "Standard Number" mappings to Bib field mapping

### v1.23
 - Adds the new Cullman Scholar entry to the patronTypes vocabulary (as CSV & JSON-LD)
 - Adds a vocabularies/scripts/setup.py to assist dependency install
 - Changes CSV & JSON path in all serialize scripts so that updates can be made in-place, without copying files around.
 - Updates vocabularies/scripts/README.md to clarify use

### v1.22
 - Removes Shoichi Noma room, as it is being shutdown due to SASB renovation.

### v1.21
 - Adds updated field-mapping-bib mapping for 'Contents', new mapping for 'Contents title'

### v1.20
 - Adds parallel field mappings to field-mapping-bib.json

### v1.19
 - Updates to `recapCustomerCodes` for Schomburg
 - Field-mapper-bib change: Retires temporary noteV2 field

### v1.18
 - Field-mapper-bib change: Adds catalogBibLocation prop to bib mapping

### v1.17
 - Adds rebuilt Bib Notes mappings with updated types

### v1.16
 - Field-mapper-bib change: add 720 to "Contributor literal"

### v1.15
 - Updates to bib mapping, including:
   - Remove 590
   - Change Note predicate from skos:note to bf:note
   - First use of indexPropertyName in bib field mapping to support
     divergent index properties and json-ld keys (for re-mapped note
     field)
   - New mappings/recap-discovery/README.md to document rationale and
     usage of bib and item field mapping documents

### v1.12
 - Updates to `recapCustomerCodes` to allow delivery to Schomburg for partner items.

### v1.11
 - Adds publicationStatement to bib mapping.

### v1.10
 - Adds serialPublicationDate to bib mapping.

### v1.9
 - Change to Schomburg `sc` label in `locations` (adds "Research and Reference Division")
 - Adds "Branch" to `ia` code in `locations` in addition to "Research" for `nypl:collectionType`
 - Remove several delivery mappings from `LQ` code in `recapCustomerCodes`

### v1.8
 - Updates to `recapCustomerCodes` to allow delivery to LPA for partner items

### v1.7
 - Update to Requestability.md
 - Updates `ia` code to "Research" instead of "Branch"

### v1.6
 - Updates to `recapCustomerCodes` to allow delivery to SIBL for partner items

### v1.5
 - Updates `notes`/`toc` content mapping
 - Fix mis-aligned Notes labels

### v1.4
 - Adds field mappings for Genre/Form literal.

### v1.3
 - not used

### v1.2
 - Adds MARC field 264 for place of publication.

### v1.1
 - Restricts MARC subfields for titleDisplay serialization.

### v1.0
 - Initial stable release of nypl-core mappings, vocabularies and serialization scripts.
