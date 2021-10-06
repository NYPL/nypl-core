# CHANGELOG

### v1.43
- Add new field mappings for Added Titles

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
