# External vocabularies and dependencies

The Oireachtas ontology modules reuse established vocabularies. This page
records the exact versions used, where they come from, how they are resolved
locally, and the licensing under which they are included here. No network
access is needed to parse the seven Oireachtas modules; the vendored copies
below exist so that the pinned ELI and ELI-DL versions resolve locally and
reproducibly.

## Vendored dependencies

Both files below are included in [`ontology/external/`](../ontology/external/ELI-OWL/eli-1.5.rdf)
and verified by SHA-256 checksum.

| Vocabulary | Version | Local copy | Source | SHA-256 |
|---|---|---|---|---|
| ELI | 1.5 | [`ontology/external/ELI-OWL/eli-1.5.rdf`](../ontology/external/ELI-OWL/eli-1.5.rdf) | <https://data.europa.eu/eli/ontology#> | `35bba63a0945e089817ddeb25512d31bfa101344282a4dfbce58e92ad756111c` |
| ELI-DL | 3.0 | [`ontology/external/ELI-DL-OWL/eli-dl.ttl`](../ontology/external/ELI-DL-OWL/eli-dl.ttl) | ELI-DL 3.0 distribution on the Interoperable Europe Portal | `5ec2d7a0bb176e1432e39fee3e4150c3f651dafaef52976428259be4f9eabb62` |

The `owl:imports` IRIs `http://data.europa.eu/eli/ontology#` and
`http://data.europa.eu/eli/eli-draft-legislation-ontology#` resolve to the
*current* published version at data.europa.eu, which may differ from the
pinned versions. To resolve imports deterministically, use the bundled
[Protégé catalog](../ontology/catalog-v001.xml), which maps both import IRIs
to the vendored pinned copies.

### Licensing and attribution

Both files are publications of the European Union and are reused here under
the European Commission's reuse policy (Commission Decision 2011/833/EU of
12 December 2011), which authorises reuse under the Creative Commons
Attribution 4.0 International (CC BY 4.0) licence with attribution. When
redistributing or adapting these files, attribute them to the European
Commission / Publications Office of the European Union via the
Interoperable Europe Portal, state the licence (CC BY 4.0), and indicate the
versions above. The files are included unmodified.

## Dependencies resolved from their published IRIs

| Vocabulary | Import IRI | Notes |
|---|---|---|
| W3C Organization Ontology | `http://www.w3.org/ns/org#` | Imported by `agents.owl.ttl` and `members.owl.ttl`; resolves from its namespace IRI |
| FOAF | `http://xmlns.com/foaf/0.1/` | Imported by `members.owl.ttl`; resolves from its namespace IRI |

Both are stable, publicly resolvable vocabularies; no pinned copy is bundled.

## Transitive dependencies of ELI-DL (not vendored)

The ELI-DL 3.0 file itself imports:

- **CIDOC CRM** — `http://www.cidoc-crm.org/cidoc-crm/`, encoded as
  `cidoc_crm_v6.2.1-2018April.rdf` (a draft RDFS encoding created by
  FORTH-ICS).
- **FRBRoo** — `http://iflastandards.info/ns/fr/frbr/frbroo/`, encoded as
  `FRBR2.4-draft.rdf` (FRBRoo v2.4 draft, harmonised with CIDOC CRM v6.2.1,
  by the International Working Group on FRBR/CIDOC CRM Harmonisation, ICS-FORTH).

These encodings are part of the ELI-DL distribution on the Interoperable
Europe Portal and are **not** redistributed here. They are only needed for
the full transitive import closure of ELI-DL itself: the Oireachtas modules
use ELI-DL terms directly and do not define terms in CIDOC CRM or FRBRoo. To
obtain them, download the ELI-DL 3.0 ontology bundle from the Interoperable
Europe Portal (<https://interoperable-europe.ec.europa.eu/>), which includes
the `cidoc_crm_v6.2.1` and `FRBR2.4-draft` RDF files and a matching
catalog, or resolve both namespace IRIs online.

## Relationship to the Oireachtas modules

- `agents.owl.ttl`, `events.owl.ttl`, `legislation.owl.ttl`,
  `members.owl.ttl` and `debates.owl.ttl` reuse ELI/ELI-DL classes and
  properties; `legislation.owl.ttl` additionally annotates reused ELI/ELI-DL
  terms for Oireachtas usage.
- The Oireachtas ontology does not modify, rename or re-declare imported
  external terms; ELI and ELI-DL remain authoritative for their own terms.
