# NYPL Core

Models, mappings, and vocabularies for the NYPL Core ontology.

### Current Version

v1.46

## Contributing

NYPL-Core contains vocabularies and mappings that control many different components across the Library Services Platform. It's important to follow these guidelines to reduce risk of unintended effects downstream.

### 1. Propose your change

1. Cut a feature branch from `master` with your intended change.
2. If modifying `./vocabularies`, make your edits to the CSVs and then update the JSON-LD files using the included [`./vocabularies/scripts`](./vocabularies/scripts)
3. (If modifying `./mappings`, you can just edit the JSONs directly.)
4. Update [README.md](README.md#current-version) with the new version number (e.g. "v1.33")
5. Add an entry to [CHANGELOG.md](CHANGELOG.md) summarizing the changes
6. Commit your changes.
7. Create a pre-release tag using the next logical version number (e.g. `v1.33a`. See [Working with Git tags](#working-with-git-tags))
8. Git push and create a PR

### 2. Consider downstream effects

Think about what components are affected by the change. For changes to `./mappings`, you should consider the impact on components in the Discovery data pipeline. (Presumably you're making changes specifically for that pipeline.) For some `./vocabularies` changes (e.g. changes to `locations.json` or `recapCustomerCodes.json`) the components impacted are too many to independently test. At a minimum, you should check the following components:

1. Verify that [nypl-core-objects](https://github.com/NYPL/nypl-core-objects) is able to parse your changes (e.g. to build local mappings files based on your pre-release tag of 1.33a, run `NYPL_CORE_VERSION=v1.33a npm run build-mappings` inside that repo)
2. Verify that the specific component(s) for which you're making the change pick up the change...

The method by which you verify an NYPL-Core change in an app depends on how the app includes NYPL-Core.
* _For Node apps using `nypl-core-objects`_, you should be able to set `NYPL_CORE_VERSION=v1.33a` to tell it to use your pre-release version.
* For (typically non-Node) _components that draw on S3-hosted lookup files_ (e.g. [by_sierra_location.json](https://s3.amazonaws.com/nypl-core-objects-mapping-production/by_sierra_location.json), you may test your change by first [deploying your pre-release vocab to the QA S3 bucket](https://github.com/NYPL/nypl-core-objects#pushing-to-s3) and then using the QA version of the S3-hosted file to verify your changes.

Note that beanstalk apps may need to be "Restart"ed to pick up env config changes.

### 3. Publish changes

After 1) PR signoff and 2) confirming that your changes don't create trouble for [nypl-core-objects](https://github.com/NYPL/nypl-core-objects) or other immediately impacted apps, proceed to publish.

1. Merge your PR and delete feature branch.
2. Commit your changes
3. Add a release tag (e.g. `v1.33`. See [Working with Git tags](#working-with-git-tags))
4. Push to master
5. If you made changes to `./vocabularies`:
   - Follow the instructions in [nypl-core-objects "Pushing to S3"](https://github.com/NYPL/nypl-core-objects#pushing-to-s3) to push updated JSONs to S3 (for use by non-Node apps).
   - If there are Node apps that need your update, update their `NYPL_CORE_VERSION` to your new version (e.g. `v1.33`)

## Appendix

### Working with Git tags

We [tend to tag version numbers starting with "v1.0.0"](https://github.com/NYPL/engineering-general/blob/master/standards/versioning.md). NYPL-Core diverges from that by only specifying major and minor precision (e.g. v1.33).

To create a tag:

```
git tag -a v1.33
```

To create a "pre-release tag" (i.e. an unofficial version number tag published for the purpose of testing):

```
git tag -a v1.33a
```

After creating a pre-release tag (or any other tag), if you want to add additional commits to the tag (essentially reassign what the tag is an alias for), you'll need to force it:

```
git tag -a v1.33a -f
```

All tags you create must be pushed to origin after pushing your commits:

```
git push --tags
```

If you recently reassigned a pre-release tag, you'll need to force push:

```
git push --tags -f
```

Sometimes multiple features are vying for the next release version. If, when creating your pre-release tag, another active PR has already pushed code using that pre-release tag, you may create a second pre-release tag (e.g. `v1.33b`). You may arrange to eventually merge both features into the final release. Or only one feature may be rolled out under the version number and the other feature will have to take the next logical version number.
