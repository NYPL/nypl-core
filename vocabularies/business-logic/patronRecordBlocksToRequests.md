(Updated 20171027)

NYPL's ILS-oriented circulation rules are fully encoded and documented only in Sierra. NYPL services currently rely on Sierra (via the Sierra REST API) to automatically apply circulation rules (loan rules, patron blocks, etc.) to the following transactions:  
* all ReCAP requests placed via SCC (EDD requests require only a valid NYPL login)  
* all ReCAP requests that are assigned for delivery to a patron-facing (non-"suppressed") delivery/stop code when placed via SCSB.  

Sierra circulation rules are not initially applied to ReCAP requests that are completely mediated by staff. ReCAP requests that are completely mediated by staff are assigned for delivery to a "suppressed" delivery/stop code when placed via SCSB. NYPL services do not contact the Sierra REST API for ReCAP requests to "suppressed" delivery codes.  

ReCAP requests to "suppressed" delivery codes initially bypass Sierra circulation rules and are not initially/automatically recorded in Sierra. "Suppressed" delivery codes exist to allow NYPL staff full control over the circulation of suppressed or otherwise sensitive items; staff are expected to request and circulate these items according to local access policies and procedures. 

Staff-mediated requests that involve "suppressed" delivery codes generally align with NYPL's pre-SCSB ReCAP request/circulation processes.

Early work towards implementing circulation rules natively in NYPL services/outside of Sierra is recorded in [this "patronRecordBlocksToRequests" Google doc](https://docs.google.com/document/d/1bfmGOMoqqsXFy9FGezfQyfDEIiTv7JgYHkizOxNSKNc/edit), last edited on June 28, 2017.
