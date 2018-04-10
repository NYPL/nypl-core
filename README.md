# NYPL Core

Models, mappings, and vocabularies for the NYPL Core ontology.

## Deployment Process

A suggested workflow for the `discovery-api` Beanstalk application.
Deploying other apps that depend on `nypl-core` will resemble
these steps in spirit.

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
* Change environment variables for `discovery-api-dev` (Elastic Beanstalk)
* Apply the changes which will trigger an application restart
* If no changes to variables are detected, a restart will not take
  place. One must force a restart to clear caches and pull in changes.
  For discovery-api, use the 'Restart App Server(s)' option in the Actions
  dropdown.
* Test the changes on our QA server
* Make adjustments to the mapping as needed
* Force update the tag via `git tag -f vX.Xa`
* Restart the `discovery-api-dev` application
* Re-test

#### Multiple Pre-release Tags:
If so desired, pre-release tags could be incremented by their trailing letter
when working with multiple features for the same release.
* Create a new pre-release tag vX.Xb when incorporating a secondary feature
  for the same release
* Follow the same restart, re-test, update loop for changes

#### For Production:

* Create a pull request against master for your branch's changes
* Submit for approval
* Once approved, merge changes to master
* Delete working branch
* Add a release tag vX.X (without the trailing letter) based on the new
  merge and commit
* Add an entry to [CHANGELOG.md](CHANGELOG.md) summarizing the changes and push to master. Add release notes at https://github.com/NYPL/nypl-core/tags .
* Restart the `discovery-api` application to clear the cache and pick up the
  changes via the 'Restart App Server(s)' option in the Actions dropdown.


### Responsibilities

Contributors make changes, commit and submit pull requests. Approvals
are performed by contributors other than the owners of pull requests.
Owners of pull requests merge their changes upon approval.
