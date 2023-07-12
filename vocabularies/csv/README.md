# CSV vocabularies

Human-readable versions of vocabularies, termlists, and codelists.

## Locations
There are three different sources of truth for determining deliverableTo: Sierra, Recap, and the M2 ILS. 
locations.csv contains Sierra locations, which includes M2 locations. However, these location codes are governed by 
different deliverability rules than other onsite materials. These have no deliverableTo listed in locations.csv because 
their deliverableTo is instead maintained in `m2CustomerCodes.csv`. To make it explicit where deliverableTo should be 
resolved, we have a property per code called deliverableToResolution, which indicates if that information 
should be found in locations, m2CustomerCodes, or recapCustomerCodes csvs. 