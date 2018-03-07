# CHANGELOG

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
