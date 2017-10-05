## ReCAP CGD/Use Restriction Rules
### Ordered Logic to Support NYPL's Sierra MARC-in-JSON to SCSBXML Translation Module [(Jira SRCH-302)](https://jira.nypl.org/browse/SRCH-302)

*The below CGD/Use Restriction Rules are applied via the MARC-in-JSON to SCSBXML translation module when NYPL items are newly-accessioned at ReCAP.*  
  
**(0) Default CGD/Use Restriction Profile**  

* *The default profile should be applied to items that are eligible for Accession into ReCAP but cannot derive a CGD/Use Restriction profile from the rules below.*  
* *The default profile is: CGD="Private" and Use Restriction="In Library Use"*  
  
**(I) Determine ReCAP Accession eligibility.**  
1. Check for ReCAP location code in item record  
⋅⋅⋅a. ReCAP item location codes always start with rc. The inverse is true; location codes that start with rc are always ReCAP location codes.  
⋅⋅⋅b. If the item's location code is not a ReCAP location code, do not process the item.  
⋅⋅⋅⋅⋅⋅i. (Probably best to "error out" instead of applying the default profile because every ReCAP item physically accessioned at ReCAP should already have a ReCAP location code -- presence of a non-ReCAP location code may indicate a larger issue with the item or record. Additionally, the resulting error/exception report could help Heide's team troubleshoot metadata issues or issues with preparatory batch processing.)  
⋅⋅⋅c. If the item's location code is a ReCAP location code, proceed to (II) Determine the item's CGD.  

**(II) Determine the item's CGD.**  
  
2. Check for private Customer Code (use SCSB customer code, not Sierra item agency)  
⋅⋅⋅a. Private customer codes = JO, ND, NL, NN, NO, NP, NQ, NR, NS, NU, NV, NX, NZ  
⋅⋅⋅b. If Customer Code is private, then item's  CGD="Private" and item has Use Restriction="In Library Use" -- **check is complete for this item.**  
⋅⋅⋅c. If Customer Code is not private, then:  
3. Check for private OPAC Message  
⋅⋅⋅a. Private OPAC Message codes = 4, a, p, o  
⋅⋅⋅b. If OPAC Message is private, then item's  CGD="Private" and item has Use Restriction="In Library Use" -- **check is complete for this item.**  
⋅⋅⋅c. If neither Customer Code nor OPAC Message is private, then:  
4. Check for private item type aka itype  
⋅⋅⋅a. Private itypes = 0, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 37, 38, 41, 51, 66, 68  
⋅⋅⋅b. If itype is private, then item's  CGD="Private" and item has Use Restriction="In Library Use" -- **check is complete for this item.**  
⋅⋅⋅c. If neither Customer Code, OPAC Message, nor itype is Private, then item is shareable (either Open or Shared, TBD by matching algorithm)  

**NOTE**: every item assigned CGD="Private" also has Use Restriction="In Library Use". There is no need to apply the below Use Restriction check to CGD="Private" items.

**(III) After determining CGD is shareable (Open or Shared), determine Use Restriction.**  
  
5. Check for "Supervised Use" OPAC message  
⋅⋅⋅a. Currently, the only "Supervised Use" OPAC message code = u  
⋅⋅⋅b. If item has a "Supervised use" OPAC Message, the item's Use Restriction="Supervised Use" -- **check is complete for this item.**  
⋅⋅⋅c. If item does not have a "Supervised Use" OPAC message, then:  
6. Check for "In Library Use" item type aka itype  
⋅⋅⋅a. "In Library Use" itypes = 2, 3, 4, 5, 6, 7, 25, 26, 32, 33, 34, 35, 42, 43, 52, 53, 60, 61, 65, 67  
⋅⋅⋅b. If item has an "In Library Use" itype, the item's Use Restriction="In Library Use" -- **check is complete for this item.**  
⋅⋅⋅c. If item does not have a "Supervised Use" OPAC Message and does not have an "In Library Use" itype, then:  
7. Check for "no restrictions" item type aka itype  
⋅⋅⋅a. "No restrictions" itypes = 55, 57  
⋅⋅⋅b. If item has a "no restrictions" itype, the item's Use Restriction field should be blank (conveys absence of use restrictions) -- **check is complete for this item.**  
⋅⋅⋅c. If item has neither a "Supervised Use" OPAC Message, nor an "In Library Use" itype, nor a "no restrictions" itype, assign the default profile: CGD="Private" and Use Restriction="In Library Use"  
  
### Accepted ReCAP CGD and Use Restriction values  

* Accepted CGDs (Collection Group Designations):  
  * **Shared**: item is lendable to all partners; cost of maintaining item is shared among ReCAP partners; dupes can be discarded.  
  * **Open**: item is lendable to all partners, but it is owned by one specific partner.  
  * **Private**: item lends only to (within) the specific partner that owns it.  

* Accepted Use Restrictions:  
  * **Supervised Use**: item must be used only in a supervised reading area of the receiving library; it cannot be lent to patrons for use outside the library.  
  * **In Library Use**: item must be used inside the receiving library; it cannot be lent to patrons for use outside the library.  
  * **[blank value]**: item has no restrictions on use; it can be lent to patrons for use outside the receiving library. Partner items with no restrictions on use are labeled "[Standard NYPL Restrictions Apply]" in Sierra and patron-facing account interfaces.  
