# Bills and events

**Status:** vocabulary orientation. Exact terms and axioms are in the linked
OWL modules.

A Bill is represented with ELI/ELI-DL work and process resources. Its process
status, process type, submitting agent, latest activity and concrete lifecycle
activities are different facts. Controlled stage, event and status values are
not occurrences. The local `legislation.owl` module annotates reused ELI/ELI-DL
terms for Oireachtas usage; `events.owl` defines Oireachtas event concepts.

The existing `oir:BillDelivery` introduction/presentation activity links to
its Bill Work with `eli-dl:created_a_realization_of` and to its process with
`eli-dl:forms_part_of`. Use this explicit two-edge relationship for Bill
status and sponsorship; named-graph co-ownership is not a substitute for it.

The Bill Work is an `eli-dl:DraftLegislationWork`, not an `eli:LegalResource`.
It uses `eli:work_type :Bill` (`:Bill` is in `eli:WorkTypeTable`), `dct:title`,
`dct:alternative` and `dct:identifier`. This avoids ELI properties whose domains
would classify the Work as a LegalResource or Expression. Enacted Acts remain
separate `eli:LegalResource`s.

Amendment documents and amendment activities are distinct resources. A source
status or controlled stage value does not by itself assert that a particular
event occurred.

- [Legislation module](../../ontology/legislation.owl.ttl)
- [Events module](../../ontology/events.owl.ttl)
- [Agents module](../../ontology/agents.owl.ttl)
