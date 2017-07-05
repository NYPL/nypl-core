**Suppressed** = record is not displayed in the Discovery interface. Bib records and/or attached item records can be suppressed.

**NYPL-owned bib/item suppression**

This suppression logic is based on NYPL's local implementation of suppression codes/mapping in Sierra/WebPAC/Encore.

**Order of operations for determining NYPL-owned bib/item suppression:**

* Sierra bib record suppression
  * Sierra bib "suppressed" convenience field value
    * If "suppressed" value = "true", suppress bib and all attached items from display.
    * If "suppressed" value = "false", display bib and apply item suppression rules for each attached item:
* Sierra item record suppression
  * Sierra item record "icode2" fixed field value (aka "item code 2" or fixed field "60" in API response)
    * If icode2 value is mapped to nypl:suppressed=true, suppress item from display.
    * If icode2 value is mapped to nypl:suppressed=false, display item
    * icode2 mapping to nypl:suppressed=true/false: https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/icode2.csv
* If item is determined as NOT suppressed, apply NYPL-owned item requestability logic (link TBA)

** Related documentation** 

JIRA ticket:
https://jira.nypl.org/browse/SRCH-87

This file (nyplBibAndItemSuppression) supersedes the earlier Google doc: 
https://docs.google.com/document/d/1iswn3DSe96Hy5cw8Sauql9OB88r6OUoBFzRsdx34Xb0/edit

Potential suppression/deletion logic for partner-owned items is in [partnerBibAndItemSuppression](https://github.com/NYPL/nypl-core/blob/master/vocabularies/business%20logic/partnerBibAndItemSuppression.md)
