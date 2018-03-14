# Recap Bib & Item Field Mappings

These mappings register all of the properties we extract from bib & item MARC records. Each property draws one one or more queries into the source MARC record. Thus each mapping registers:
 1. `paths`: Used to query into bib & item MARC documents to extract data.
 2. `pred`: Predicate used to store that data in the Discovery Store.
 3. `indexPropertyName`: Indicates property name holding the data in the current ES index (as written by the [indexer](https://github.com/nypl-discovery/discovery-api-indexer). (If unset, defaults to `jsonLdkey`, since these are typically in sync.)
 3. `jsonLdkey`: The actual property name served by the [Discovery API](https://github.com/nypl-discovery/discovery-api) to the [Discovery Frontend](https://github.com/nypl-discovery/discovery-front-end).
 
In many cases, MARC mappings are straightforward and programatically actionable like this one, which gives 2 very specific MARC "queries" (e.g. marc 130, subfields $a, $b, $f, $n, and $p).:

```js
  "Alternative title": {
    "pred": "dcterms:alternative",
    "jsonLdKey": "titleAlt",
    "paths": [
      {
        "marc": "130",
        "subfields": [ "a", "b", "f", "n", "p" ],
        "description": "Varying Form of Title"
      },
      {
        "marc": "210",
        "subfields": [ "a", "b", "f", "n", "p" ],
        "description": "Varying Form of Title"
      },
      ...
```

Other mappings are included mainly as a formality because the details of their extraction, remediation, and/or storage can not sanely be represented in the language of the mapping file. Electronic Resources are one example:

```js
  "Electronic location": {
    "pred": "bf:electronicLocator",
    "jsonLdKey": "electronicLocator",
    "paths": [
      {
        "notes": "856 (see notes)"
      }
    ]
  },
```

The "notes" here refer to documentation in "MARC > Discovery model mappings" and "Discovery properties" Google sheets, which describe the complex logic by which many subfields in marc 856 are extracted for consideration.

## JsonLdKey & IndexPropertyName Parity 

The `jsonLdKey` property typically governs both 1) the property name used in the Discovery API as well as 2) the property name in the ES index. In some cases it's necessary for them to be different. For example, when the ES mapping for `note` changed fundamentally, we had to add a new mapping `noteV2` to store the new mapping type. We didn't want the `jsonLdKey` to change, but by specifying `indexPropertyName: "noteV2"`, the indexer knows what property to store the value in and the DiscoveryAPI knows that `noteV2` should override `note`.
