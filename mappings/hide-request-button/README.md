# Re-Suppress Request Buttons

## Description

In order to implement item-level holds in Sierra, we were required to change existing "requestable" business logic. This resulted in the _Request_ button appearing in unintended records in WebPAC and Encore.
  
After contacting Innovative and confirming:

> there is no way to have the system suppress the request button unless the item/bib is not requestable

We decided to pursue hiding the _Request_ button via JavaScript. This repo contains the mappings used to hide the button.

For more information, see JIRA ticket [DIS-79](https://jira.nypl.org/browse/DIS-79).

## Examples

These bibs are examples where the _Request_ button should be hidden:

- https://nypl-sierra-test.iii.com/record=b10087932
  - https://nypl-encore-test.iii.com/iii/encore/record/C__Rb10087932
- https://nypl-sierra-test.iii.com/record=b10114570
  - https://nypl-encore-test.iii.com/iii/encore/record/C__Rb10114570
- https://nypl-sierra-test.iii.com/record=b10128739
  - https://nypl-encore-test.iii.com/iii/encore/record/C__Rb10128739
- https://nypl-sierra-test.iii.com/record=b10139869
  - https://nypl-encore-test.iii.com/iii/encore/record/C__Rb10139869
- https://nypl-sierra-test.iii.com/record=b101515480
  - https://nypl-encore-test.iii.com/iii/encore/record/C__Rb101515480
- https://nypl-sierra-test.iii.com/record=b10040821
  - https://nypl-encore-test.iii.com/iii/encore/record/C__Rb10040821
- https://nypl-sierra-test.iii.com/record=b10032439
  - https://nypl-encore-test.iii.com/iii/encore/record/C__Rb10032439

For more examples, see the testing [Google Sheet](https://docs.google.com/spreadsheets/d/1tKlxQCIBhwHfZI-A_v3aZGO3bHfo4Al6S_gxtty0zIE/edit#gid=412932731).

## Mappings

- [masterHideLocations.json](matchingLocations.json): locations in WebPAC and Encore will be matched against the `text` value in this list and hidden if found. 
- [encoreHideLocations.json](encoreMatchingLocations.json): in addition to the "master" list, locations in Encore will be substring matched against the `text` value in this list and hidden if found. 
