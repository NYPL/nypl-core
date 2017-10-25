## ReCAP CGD/Use Restriction Rules
### Ordered Logic to Support NYPL's Sierra MARC-in-JSON to SCSBXML Translation Module [(Jira SRCH-302)](https://jira.nypl.org/browse/SRCH-302)

*The below Use Restriction/CGD Rules are applied via the MARC-in-JSON to SCSBXML translation module when NYPL items are newly-accessioned at ReCAP.*  
  
**(0) Default CGD/Use Restriction Profile**  

* *The default profile should be applied to items that are eligible for Accession into ReCAP but cannot derive a CGD/Use Restriction profile from the rules below.*  
* *The default profile is: CGD="Private" and Use Restriction="In Library Use"*  
  
**(I) Determine ReCAP Accession eligibility.**  
1. Check for ReCAP location code in item record  
⋅⋅⋅a. ReCAP item location codes always start with rc. Location codes that start with rc are always ReCAP location codes.  
⋅⋅⋅b. If the item's location code is a ReCAP location code, **go to (II) Determine the item's Use Restriction.**  
⋅⋅⋅c. If the item's location code is not a ReCAP location code, **do not process the item; log an error.**  
⋅⋅⋅⋅⋅⋅i. (Probably best to "error out" instead of applying the default profile because every ReCAP item physically accessioned at ReCAP should already have a ReCAP location code -- presence of a non-ReCAP location code may indicate a larger issue with the item or record, such as incomplete processing. Additionally, the resulting error/exception report could help Heide's team troubleshoot metadata issues or issues with preparatory batch processing.)   

**(II) Determine the item's Use Restriction.**  

1. Check for "Supervised Use" OPAC message  
⋅⋅⋅a. "Supervised Use" OPAC message code = u  
⋅⋅⋅b. If item has a "Supervised use" OPAC Message, the item's Use Restriction="Supervised Use" -- **Go to (III) Determine CGD.**  
⋅⋅⋅c. If item does not have a "Supervised Use" OPAC message, then:  
2. Check for "In Library Use" item type aka itype  
⋅⋅⋅a. "In Library Use" itypes = 2, 3, 4, 5, 6, 7, 25, 26, 32, 33, 34, 35, 42, 43, 52, 53, 60, 61, 65, 67  
⋅⋅⋅b. If item has an "In Library Use" itype, the item's Use Restriction="In Library Use" -- **Go to (III) Determine CGD.**  
⋅⋅⋅c. If item does not have a "Supervised Use" OPAC Message and does not have an "In Library Use" itype, then:  
3. Check for "no restrictions" item type aka itype  
⋅⋅⋅a. "No restrictions" itypes = 55, 57  
⋅⋅⋅b. If item has a "no restrictions" itype, the item's Use Restriction field should be blank (conveys absence of use restrictions) -- **Go to (III) Determine CGD.**  
⋅⋅⋅c. If item has neither a "Supervised Use" OPAC Message, nor an "In Library Use" itype, nor a "no restrictions" itype -- **Assign the default profile: Use Restriction="In Library Use" and CGD="Private". *Check is complete for this item***; *do not go to (x) Determine CGD.*  
  

**(III) Determine the item's CGD.**  
  
1. Check for private icode2 (determines whether item is suppressed from public view)  
⋅⋅⋅a. Private icode2 values = p, s  
⋅⋅⋅b. If icode2 is private, then item's CGD="Private" -- **Check is complete for this item.**  
⋅⋅⋅c. If icode2 is not private, then:  
2. Check for private Customer Code (use SCSB customer code, not Sierra item agency code)  
⋅⋅⋅a. Private customer codes = JO, ND, NL, NN, NO, NP, NQ, NR, NS, NU, NV, NX, NZ  
⋅⋅⋅b. If Customer Code is private, then item's CGD="Private" -- **Check is complete for this item.**  
⋅⋅⋅c. If neither icode2 nor Customer Code is private, then:  
3. Check for private OPAC Message  
⋅⋅⋅a. Private OPAC Message codes = 4, a, p, o  
⋅⋅⋅b. If OPAC Message is private, then item's CGD="Private" -- **Check is complete for this item.**  
⋅⋅⋅c. If neither icode2, Customer Code, nor OPAC Message is private, then:
4. Check for private item type aka itype  
⋅⋅⋅a. Private itypes = 0, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 37, 38, 41, 51, 66, 68  
⋅⋅⋅b. If itype is private, then item's CGD="Private" -- **Check is complete for this item.**  
⋅⋅⋅c. If neither icode2, Customer Code, OPAC Message, nor itype is private, then item's CGD is "Shared" (either Open or Shared, TBD by SCSB matching algorithm) -- **Check is complete for this item.**  
  
### Accepted ReCAP CGD and Use Restriction values  

* **Accepted CGDs** (Collection Group Designations):  
*Note: Initially assigning CGD=Shared to all [Shared OR Open] NYPL items during the translation/designation phase is a legacy/accepted choice. SCSB's matching algorithm processes CGD=Shared items post-Accession. Based on the presence of title matches across partners' collections, the algorithm will change some items with an initial CGD of "Shared" to CGD=Open.*
  * **Shared**: item is lendable to all partners; cost of maintaining item is shared among ReCAP partners; dupes can be discarded.  
  * **Open**: item is lendable to all partners, but it is owned by one specific partner.  
  * **Private**: item lends only to (within) the specific partner that owns it.  

* **Accepted Use Restrictions**:  
  * **Supervised Use**: item must be used only in a supervised reading area of the receiving library; it cannot be lent to patrons for use outside the library.  
  * **In Library Use**: item must be used inside the receiving library; it cannot be lent to patrons for use outside the library.  
  * **[blank value]**: item has no restrictions on use; it can be lent to patrons for use outside the receiving library. Partner items with no restrictions on use are labeled "[Standard NYPL Restrictions Apply]" in Sierra and patron-facing account interfaces.  
  
### Why determine Use Restriction before CGD?  

* The CGD check is guaranteed to return one of two acceptable results. However, the CGD in finalized only upon completion of the Use Restriction check. A failed use Restriction Check will determine a default CGD/Use Restriction combination.  
* A failed Use Restriction check automatically assigns an item the default profile [CGD=Private and Use Restriction=In Library Use"]. The previous directive to [first determine CGD, then determine Use Restriction] could initially assign the item CGD=Shared only to ultimately revert this to the default CGD=Private upon failure of the final Use Restriction check. The (potential) inefficiency of the earlier flow is corrected by checking Use Restriction before checking CGD, as a failed Use Restriction check will determine the default CGD=Private -- thereby negating the need to run a CGD check at all.  
  * It's best to isolate failure as early in the process as possible. An item can fail Use Restriction logic as a given item is not guaranteed to match to one of the 3 acceptable Use Restrictions. Meanwhile, an item cannot fail CGD logic as the CGD logic simply seeks to prove/disprove that an item's CGD=Private (disproving CGD=Private means CGD=Shared). A given item is guaranteed to match to 1 of 2 acceptable CGD results (Private or Shared). 
The proposed logic flow accounts for items that have CGD=Private and Use Restriction = Supervised Use. While about 3k items in SCSB have CGD=Private and Use Restriction=Supervised Use, the "loan rules"/compartmentalized logic documented in the earlier use restrictions spreadsheet does not account for this combination.   
  * Examples of items with CGD=Private and Use Restriction=Supervised Use:
    * Afterall (serial): 33433087868075 (JO, Private, Supervised use)
    * Application des sons harmoniques [...] (monograph): 33433112379767 (NP, Private, Supervised use)
* The above logic is in part based on the original rule categories ("loan rules") mapped in this [spreadsheet](https://docs.google.com/spreadsheets/d/10Cd4cv8W-ijKF6pyp7MQleWn2ExGL2sRXd-tz0BpWpE/edit#gid=462497452).  


