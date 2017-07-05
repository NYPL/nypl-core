**Suppressed** = record is not displayed in the Discovery interface. Bib records and/or attached item records can be suppressed.

**NYPL-owned bib/item suppression**

This suppression logic is based on NYPL's local implementation of suppression codes/mapping in Sierra/WebPAC/Encore. A full rundown of NYPL bib and item suppression logic will be moved to this file once the related mapping is available in nypl-core.

In the meantime, please see the following doc for additional details: 
https://docs.google.com/document/d/1iswn3DSe96Hy5cw8Sauql9OB88r6OUoBFzRsdx34Xb0/edit

The above doc is also linked to this JIRA ticket:
https://jira.nypl.org/browse/SRCH-87

Only NYPL-owned items (both ReCAP and locally-stored) items will be subject to suppression logic, unless we need to suppress (rather than wholesale-delete) partner-owned ReCAP items that have been removed from the open/shared ReCAP collection or otherwise marked by ReCAP/SCSB as deleted/deaccessioned or permanently unavailable to NYPL. Potential suppression/deletion logic for partner-owned items is in [partnerBibAndItemSuppression](../partnerBibAndItemSuppression)
