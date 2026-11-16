# Oireachtas Ontology v2

This directory contains the current revised ontology for the Houses of the
Oireachtas. It describes parliamentary institutions and terms, Members and
their memberships, parties and offices, legislation, legislative and journal
events, and the structure of the Official Report, in OWL 2 Turtle modules
that reuse established European and W3C vocabularies.

This publication adds the revised ontology alongside the repository's
original ontology, which remains in the existing directories for historical
reference. v2 does not modify, migrate or replace the original model.

## Purpose and scope

The ontology defines the vocabulary (classes, properties, individuals and
annotations) for describing:

- **Parliamentary institutions and terms** — the Oireachtas, Dáil Éireann
  and Seanad Éireann as enduring bodies, and their bounded numbered terms.
- **Members, memberships, parties and offices** — persons, dated service in
  a House or committee, term-scoped parliamentary collections, ministerial
  offices and office-holding.
- **Legislation** — Bills as ELI/ELI-DL works and processes, versions,
  statuses, sponsorship and amendment material.
- **Events** — journal events, Bill stage activities and procedural
  outcomes.
- **Debates** — the structure of the Official Report: records, expressions,
  sittings, sections, speeches, questions and divisions. Transcript text is
  not represented as RDF.
- **Controlled vocabularies** — SKOS concept schemes for parliamentary
  categories.

The ontology describes what the model *can* represent. A class or property
being defined does not mean that instance data for it is available; datasets
are published separately from this schema.

## Module structure

| Module | Ontology IRI | Subject |
|---|---|---|
| [oireachtas.owl.ttl](ontology/oireachtas.owl.ttl) | `https://data.oireachtas.ie/ontology` | Umbrella ontology; imports all modules |
| [agents.owl.ttl](ontology/agents.owl.ttl) | `https://data.oireachtas.ie/ontology/agents` | Parliamentary institutions, persons, roles and organisations |
| [events.owl.ttl](ontology/events.owl.ttl) | `https://data.oireachtas.ie/ontology/events` | Journal events, Bill stages and procedural outcomes |
| [legislation.owl.ttl](ontology/legislation.owl.ttl) | `https://data.oireachtas.ie/ontology/legislation` | Legislative works, processes, versions and statuses |
| [members.owl.ttl](ontology/members.owl.ttl) | `https://data.oireachtas.ie/ontology/members` | Membership, parliamentary collections, roles and offices |
| [vocabulary.owl.ttl](ontology/vocabulary.owl.ttl) | `https://data.oireachtas.ie/ontology/vocabulary` | SKOS concept-scheme declarations |
| [debates.owl.ttl](ontology/debates.owl.ttl) | `https://data.oireachtas.ie/ontology/debates` | Official Report structure, questions, speeches and votes |

The shared Oireachtas term namespace is `https://data.oireachtas.ie/ontology#`
(used by the agents, events, legislation, vocabulary and debates modules).
The members module defines its own term namespace,
`https://data.oireachtas.ie/ontology/members#`. Classes conventionally use
UpperCamelCase and properties lowerCamelCase; the IRIs and axioms in the OWL
files are authoritative.

## How the modules relate

`oireachtas.owl.ttl` is the root: it imports the six subject modules, so
loading it brings in the whole model. The subject modules import one another
where they depend on shared concepts:

```text
oireachtas ── imports ──► agents, events, legislation, vocabulary, debates, members
vocabulary ──► events, legislation
legislation ──► events, ELI, ELI-DL
debates ──► events, agents, members, ELI-DL
events ──► agents, ELI-DL
members ──► agents, ELI-DL, ORG, FOAF
agents ──► ELI, ELI-DL, ORG
```

Import declarations are recorded in each Turtle file and remain
authoritative.

## External dependencies

Imported vocabularies and their status in this release:

| Vocabulary | Import IRI | Version | Status |
|---|---|---|---|
| ELI (European Legislation Identifier) | `http://data.europa.eu/eli/ontology#` | 1.5 | Vendored pinned copy at [ontology/external/ELI-OWL/eli-1.5.rdf](ontology/external/ELI-OWL/eli-1.5.rdf) |
| ELI-DL (ELI Draft Legislation Ontology) | `http://data.europa.eu/eli/eli-draft-legislation-ontology#` | 3.0 | Vendored pinned copy at [ontology/external/ELI-DL-OWL/eli-dl.ttl](ontology/external/ELI-DL-OWL/eli-dl.ttl) |
| W3C Organization Ontology | `http://www.w3.org/ns/org#` | current published version | Resolved from its published namespace IRI |
| FOAF | `http://xmlns.com/foaf/0.1/` | 0.99 / current | Resolved from its published namespace IRI |
| CIDOC CRM | `http://www.cidoc-crm.org/cidoc-crm/` | 6.2.1 (draft encoding) | Not vendored; transitive dependency of ELI-DL |
| FRBRoo | `http://iflastandards.info/ns/fr/frbr/frbroo/` | 2.4 draft | Not vendored; transitive dependency of ELI-DL |

Pinned versions, source locations, SHA-256 checksums, licensing and
attribution for every dependency are documented in
[docs/external-vocabularies.md](docs/external-vocabularies.md). The CIDOC
CRM and FRBRoo encodings are only needed for the full transitive closure of
ELI-DL's own imports; no Oireachtas module defines terms in those
vocabularies.

## Loading and using the ontology

All seven modules parse as Turtle with any RDF library, for example:

```python
from rdflib import Graph

graph = Graph()
graph.parse("v2/ontology/oireachtas.owl.ttl", format="turtle")
```

Note that `owl:imports` declarations are not automatically followed by most
tools. Two ways to assemble the complete model:

1. **Parse the root module plus the six subject modules together** (they
   import one another but each file stands alone as syntax).
2. **In Protégé**, open `v2/ontology/` — the bundled
   [catalog](ontology/catalog-v001.xml) maps the ELI and ELI-DL import IRIs
   to the vendored copies, so imports resolve locally.

The modules were validated for OWL consistency with the HermiT reasoner over
the combined Oireachtas terms; the `xsd:date` range used for date-only API
values is outside HermiT's OWL 2 datatype map and is syntax-checked rather
than reasoned over.

## Documentation

- [Understanding the Oireachtas ontology](docs/ontology-guide.md) — a plain-language guide to the model.
- [Institutions and legislation](docs/reference/institutions-and-legislation.md)
- [Membership, parties and offices](docs/reference/membership-parties-offices.md)
- [Bills and events](docs/reference/bills-and-events.md)
- [Debates and controlled vocabularies](docs/reference/debates-and-vocabularies.md)
- [External vocabularies](docs/external-vocabularies.md) — versions, sources, checksums and licensing.

## Modelling limitations

- A defined class is not populated data: coverage depends on separately
  published datasets, not on this schema.
- Term-scoped resources (numbered House terms, constituencies, panels,
  parliamentary party collections) are distinct per term even when labels
  repeat; do not merge them by name.
- The ontology does not model a President resource, and does not store
  Official Report transcript text.
- Some members-module declarations are retained as deprecated for
  compatibility with the original ontology; consult the module annotations
  rather than a deprecated term.

## Licence and attribution

The Oireachtas ontology in this directory is © Houses of the Oireachtas and
is released under the repository's [Creative Commons Attribution 4.0
International](../LICENSE) licence. The bundled ELI and ELI-DL files are ©
European Union, reused under the European Commission's reuse policy
(Commission Decision 2011/833/EU, CC BY 4.0) with attribution to the source
portal; see [docs/external-vocabularies.md](docs/external-vocabularies.md)
for the exact attribution of each vendored file.
