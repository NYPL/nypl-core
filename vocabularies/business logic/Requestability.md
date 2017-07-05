### Order of operations for determining partner-owned ReCAP item requestability

*Item must not be suppressed - unless superseded by another suppression/deletion method, apply partner-owned bib/item suppression logic first: [partnerBibAndItemSuppression.md](https://github.com/NYPL/nypl-core/blob/master/vocabularies/business%20logic/partnerBibAndItemSuppression.md)*

* ReCAP SCSB item status
  * If "not available," item is not requestable (do not display "place request" button).
  * If "available," item is requestable -- show "place request" button.
 
 
### Order of operations for determining NYPL-owned ReCAP item requestability

*Item must not be suppressed - apply NYPL-owned bib/item suppression logic first: [nyplBibAndItemSuppression.md](https://github.com/NYPL/nypl-core/blob/master/vocabularies/business%20logic/nyplBibAndItemSuppression.md)*

* ReCAP SCSB item status
  * If "not available," item is not requestable (do not display "place request" button).
  * If "available," item might be requestable -- go to next determiner:
* Sierra item location code [(locations.csv -- warning: large file)](https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/locations.csv)
  * If nypl:requestable=false, item is not requestable (do not display "place request" button).
  * If nypl:requestable=true, item might be requestable -- go to next determiner:
* Sierra item type [(catalogItemTypes.csv)](https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/catalogItemTypes.csv)
  * If nypl:requestable=false, item is not requestable (do not display "place request" button).
  * If nypl:requestable=true, item might be requestable -- go to next determiner:
* Sierra item OPAC/Access Message [(accessMessages.csv)](https://github.com/NYPL/nypl-core/blob/master/vocabularies/csv/accessMessages.csv)
  * If nypl:requestable=false, item is not requestable (do not display "place request" button).
  * If nypl:requestable=true, item is requestable -- show "place request" button.
 
 
### Post-MVP requestability logic

[Not MVP but logic TBA soon: Order of operations for determining NYPL-owned, locally-stored item requestability] 

