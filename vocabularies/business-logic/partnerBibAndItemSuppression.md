**Suppressed** = record is not displayed in the Discovery interface. Bib records and/or attached item records can be suppressed.

**Partner-owned record suppression (or deletion from Discovery)**

Currently, Discovery is only ingesting/indexing Shared and Open partner-owned items. If a partner-owned item's collection group designation (aka CGD) changes from Shared or Open to Private, the item is not available to NYPL and should be suppressed or deleted from Discovery.

**Mapping**

Collection group designation is recorded in MARCXML field 876$x or SCSBXML field 900$a. SCSB can export either of these schemas -- see [https://htcrecap.atlassian.net/wiki/pages/viewpage.action?pageId=18939906].

**If 876$x or 900$a = "Private", the partner-owned item should be suppressed or deleted from Discovery.**

TBD: Does ReCAP SCSB  offer a separate suppression/deletion flag?

** Related documentation**

JIRA ticket: https://jira.nypl.org/browse/SRCH-87

NYPL-owned record suppression logic is documented in [nyplBibAndItemSuppression] (https://github.com/NYPL/nypl-core/blob/master/vocabularies/business-logic/nyplBibAndItemSuppression.md)

This file (partnerBibAndItemSuppression) and nyplBibAndItemSuppression supersede the earlier Google doc: https://docs.google.com/document/d/1iswn3DSe96Hy5cw8Sauql9OB88r6OUoBFzRsdx34Xb0/edit
