##CGD/Use Restriction Check
###Ordered Logic to Support NYPL's Sierra MARC-in-JSON to SCSBXML [Translation Module](https://jira.nypl.org/browse/SRCH-302)

(I) Determine ReCAP Accession eligibility
1. Check for ReCAP item location code
   a. ReCAP item location codes always start with rc. The inverse is true; location codes that start with rc are always ReCAP location codes.
   b. If the item's location code is not a ReCAP location code, do not process the item. 
      i. (Probably best to "error out" here because every ReCAP item physically accessioned at ReCAP should already have a ReCAP location code -- presence of a non-ReCAP location code may indicate a larger issue with the item or record. Additionally, the resulting error/exception report could help Heide's team troubleshoot metadata issues or issues with preparatory batch processing.)
   c. If the item's location code is a ReCAP location code, proceed to (II) Determine the item's CGD.

(II) First, determine the item's CGD:
2. Check for private Customer Code (use SCSB customer code, not Sierra item agency)
   a. Private customer codes = JO, ND, NL, NN, NO, NP, NQ, NR, NS, NU, NV, NX, NZ
   b. If Customer Code is private, then item's  CGD="Private" and item has Use Restriction="In Library Use" -- check is complete for this item.
   c. If Customer Code is not private, then:
3. Check for private OPAC Message
   a. Private OPAC Message codes = 4, a, p, o
   b. If OPAC Message is private, then item's  CGD="Private" and item has Use Restriction="In Library Use" -- check is complete for this item.
   c. If neither Customer Code nor OPAC Message is private, then:
4. Check for private item type aka itype
   a. Private itypes = 0, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 37, 38, 41, 51, 66, 68
   b. If itype is private, then item's  CGD="Private" and item has Use Restriction="In Library Use" -- check is complete for this item.
   c. If neither Customer Code, OPAC Message, nor itype is Private, then item is shareable (either Open or Shared, TBD by matching algorithm)

**NOTE**: everything that has CGD="Private" also has Use Restriction="in library use". There is no need to apply the below Use Restriction logic to CGD=Private items.

(III) After determining CGD is shareable (Open or Shared), determine Use Restriction.
5. Check for "supervised use" OPAC message
   a. Currently, the only "supervised use" OPAC message code = u
   b. If item has a "supervised use" OPAC Message, the item's Use Restriction="Supervised Use" -- check is complete for this item.
   c. If item does not have a "supervised use" OPAC message, then:
6. Check for "in library use" item type aka itype
   a. "In Library Use" itypes = 2, 3, 4, 5, 6, 7, 25, 26, 32, 33, 34, 35, 42, 43, 52, 53, 60, 61, 65, 67
   b. If item has an "In Library Use" itype, the item's Use Restriction="In Library Use" -- check is complete for this item.
   c. If item does not have a "supervised use" OPAC Message and does not have an "In Library Use" itype, then:
7. Check for "no restrictions" item type aka itype
   a. "No restrictions" itypes = 55, 57
   b. If item has a "no restrictions" itype, the item's Use Restriction field should be blank (conveys absence of any use restrictions.
   c. If item has neither a "supervised use" OPAC Message, nor an "In Library Use" itype, nor a "No restrictions" itype, assign the default profile: CGD="Private" and Use Restriction="In Library Use"
