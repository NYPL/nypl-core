# NYPL Core

Models, mappings, and vocabularies for the NYPL Core ontology.

## Deployment Process

### General Workflow for Changes

* Create a new branch from master
* Change the CSV file(s) with the intended changes
* Serialize changes via the appropriate script(s)
* Commit changes
* Create a pre-release tag in the form vX.Xa, i.e. v1.1a

#### For QA:

* Test the pre-release tag on AWS nypl-sandbox by setting the
  NYPL_CORE_VERSION variable to vX.Xa for applications that need to test
  the changes
* Change environment variables for discovery-api (Elastic Beanstalk)
* Apply the changes which will trigger an application restart
* If no changes to variables are detected, a restart will not take
  place. One must force a restart to clear caches and pull in changes
* Test the changes on our QA server
* Make adjustments to the mapping as needed
* Create a new tag vX.Xb
* Change the NYPL_CORE_VERSION variaable
* Restart the applications
* Re-test

#### For Production:

* Create a pull request against master for your branch's changes
* Submit for approval
* Once approved, merge changes to master
* Add a release tag vX.X (without the trailing letter) and commit
* Restart discovery-api application to clear the cache and pick up the
  changes


### Responsibilities

Contributors make changes, commit and submit pull requests. Approvals
are performed by contributors other than the owners of pull requests.
Owners of pull requests merge their changes upon approval.
