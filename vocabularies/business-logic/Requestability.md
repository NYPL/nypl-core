### Intro to Requestability

* **Requestability** = presence of "place request" ("place hold") button under a given item in the Discovery interface. Suppressed items are not visible and are therefore not requestable; suppression logic is covered in separate documents linked below.
* Not to be confused with **"EDD requestability,"** which is a mapped delivery option available for an item only if the item is determined to be "requestable" after applying the below business logic.

### Partner-owned itms: Order of operations for determining partner-owned ReCAP item requestability

*Item must not be suppressed - unless superseded by another suppression/deletion method, apply partner-owned bib/item suppression logic first: [partnerBibAndItemSuppression.md](https://github.com/NYPL/nypl-core/blob/master/vocabularies/business-logic/partnerBibAndItemSuppression.md)*

* ReCAP SCSB item status
  * If item is "not available" in SCSB, item is not requestable (do not display "place request" button).
  * If "available," item is requestable -- show "place request" button.
 
 
### NYPL-owned items: Order of operations for determining NYPL-owned ReCAP item requestability

*Item must not be suppressed - apply NYPL-owned bib/item suppression logic first: [nyplBibAndItemSuppression.md](https://github.com/NYPL/nypl-core/blob/master/vocabularies/business-logic/nyplBibAndItemSuppression.md)*

* ReCAP SCSB item status
  * If item is not found in SCSB, item is not requestable (do not display "place request" button).
  * If "not available," item is not requestable (do not display "place request" button).
  * If "available," item might be requestable -- go to next determiner:
* Sierra item location code [(locations.csv -- warning: large file)](https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/locations.csv)
  * If nypl:requestable=false, item is not requestable (do not display "place request" button).
  * If nypl:requestable=true, item might be requestable -- go to next determiner:
* Sierra item status (fixed field "88") [(statuses.csv)](https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/statuses.csv)
  * If nypl:requestable=false, item is not requestable (do not display "place request" button).
  * If nypl:requestable=true, item is requestable -- show "place request" button.
 
Change notes: current MVP directive for NYPL-owned ReCAP items is to mirror WebPAC requestability, which is based on an item's Sierra item location code and Sierra item status code.
 
### Post-MVP requestability logic

[Not MVP but logic TBA soon: Order of operations for determining NYPL-owned, locally-stored item requestability] 
 
