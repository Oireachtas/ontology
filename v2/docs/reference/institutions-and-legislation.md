# Institutions and legislation

**Status:** describes current OWL terms; consult the linked modules for exact
axioms.

## Institutions

`agents:ParliamentaryBody` is the class of enduring parliamentary institutions.
The Oireachtas, Dáil and Seanad are represented by individuals; `agents:House`
denotes an enduring House, while `agents:HouseTerm` denotes a bounded numbered
parliamentary term. A House and its terms are related with `agents:hasTerm` /
`agents:termOf`. Do not treat a term as the continuing institution.

The constitutional `agents:Government` is distinct from the generic Government
Bill submitter concept. The model also distinguishes Members as people from
roles and participation in events. These distinctions are defined in
[`agents.owl.ttl`](../../ontology/agents.owl.ttl) and
[`members.owl.ttl`](../../ontology/members.owl.ttl).

## Legislative documents

The legislation module reuses ELI and ELI-DL resource and process classes rather
than parallel local Bill Work/Expression/Format classes. Bill processes,
versions, statuses and amendment-list types are described in
[`legislation.owl.ttl`](../../ontology/legislation.owl.ttl). Events and
controlled stage values are in [`events.owl.ttl`](../../ontology/events.owl.ttl).

Current ministerial office and administrative-unit concepts are in
`members.owl`; accepted identities come from reviewed sources and are not
minted from labels alone. Department lifecycle and historical-name concepts
should not be inferred from legacy draft material.
