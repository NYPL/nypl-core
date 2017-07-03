**Partner-owned record suppression (or deletion from Discovery):**
Currently, Discovery is only ingesting/indexing Shared and Open partner-owned items. If a partner-owned item's collection group designation (aka CGD) changes from Shared or Open to Private, the item is not available to NYPL and should be suppressed or deleted from Discovery.

**Mapping:**
Collection group designation is recorded in MARCXML field 876$x or SCSBXML field 900$a. SCSB can export either of these schemas -- see [https://htcrecap.atlassian.net/wiki/pages/viewpage.action?pageId=18939906].

**TBD: implementation of this logic in Discovery may not be for MVP; ReCAP may offer a separate suppression/deletion flag.**

Once finalized, **Partner-owned** record suppression logic will be documented in this file (partnerBibAndItemSuppression.md).
**NYPL-owned** record suppression logic will be documented in [nyplBibAndItemSuppression] (../nyplBibAndItemSuppression.md)

In the meantime, please see the following doc for additional details (also contains NYPL bib/item suppression logic): 
https://docs.google.com/document/d/1iswn3DSe96Hy5cw8Sauql9OB88r6OUoBFzRsdx34Xb0/edit

The above doc is also linked to this JIRA ticket (also contains NYPL bib/item mapping):
https://jira.nypl.org/browse/SRCH-87
