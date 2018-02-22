**Suppressed** = record is not displayed in the Discovery interface. Bib records and/or attached item records can be suppressed.

**NYPL-owned bib/item suppression**

This suppression logic is based on NYPL's local implementation of suppression codes/mapping in Sierra/WebPAC/Encore.

**Order of operations for determining NYPL-owned bib/item suppression:**

* Sierra bib record suppression
  * Sierra bib "suppressed" convenience field value
    * If "suppressed" value = "true", suppress bib and all attached items from display.
    * If "suppressed" value = "false", and only Branch or non-Research items are attached to the bib, suppress bib and all attached items from display.
    * If "suppressed" value = "false", and only Research items are attached to the bib, and all attached Research items are suppressed=true according to the below item record suppression logic, suppress bib and all attached items from display.
    * If "suppressed" value = "false", and both Branch and Research items are attached to the bib, and all attached Research items are suppressed=true according to the below item record suppression logic, suppress bib and all attached items from display.
    * NOTE: SCC automatically generates a shadow "item record" to represent the existence of an electronic resource link: if a bib has only suppressed=true/non-Research items attached, but also has an 856 field/electronic resource link, SCC will display the bib by virtue of the shadow electronic resource item record.
* Sierra item record suppression
  * Sierra item record "icode2" fixed field value (aka "item code 2" or fixed field "60" in API response)
    * icode2 mapping to nypl:suppressed=true/false: https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/icode2.csv
    * If icode2 value is mapped to nypl:suppressed=true, suppress item from display.
    * If icode2 value is mapped to nypl:suppressed=false, go to next:
  * Sierra item record "itype" fixed field value (aka item type or fixed field "61" in API response)
    * If type value is mapped to nypl:suppressed=true, suppress item from display.
      * (generally only itype=50 is suppressed -- represents temporary NCIP item records)
    * If itype value is mapped to nypl:suppressed=false, display item record.
* If item is determined as NOT suppressed, apply NYPL-owned item requestability logic: https://github.com/NYPL/nypl-core/blob/master/vocabularies/business-logic/Requestability.md

**Related documentation** 

JIRA ticket:
https://jira.nypl.org/browse/SRCH-87

This file (nyplBibAndItemSuppression) supersedes the earlier Google doc: 
https://docs.google.com/document/d/1iswn3DSe96Hy5cw8Sauql9OB88r6OUoBFzRsdx34Xb0/edit

Potential suppression/deletion logic for partner-owned items is in [partnerBibAndItemSuppression](https://github.com/NYPL/nypl-core/blob/master/vocabularies/business-logic/partnerBibAndItemSuppression.md)
