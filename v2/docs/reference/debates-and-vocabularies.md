# Debates and controlled vocabularies

**Status:** current ontology design reference. Vocabulary support is not proof
that a source record has been loaded into any dataset.

## Debates

`debates:DebateRecord` represents the documentary work; a language-specific
`debates:DebateExpression` and a `debates:DebateSitting` are distinct concepts.
A written-answer record does not, by itself, establish a sitting. Debate
sections may contain speeches, summaries, questions, subsections and divisions.
Transcript text is not represented as RDF. Unresolved source references do not
create placeholder identities.

`debates:Division` is an ELI-DL Vote. Tá, Níl and Staon counts/votes are separate
properties. Only source outcomes explicitly mapped as carried or lost establish
those outcomes; an indeterminate declared outcome is not guessed. Committee
roll-call attendance is not a division. See
[`debates.owl.ttl`](../../ontology/debates.owl.ttl).

## Controlled vocabularies

[`vocabulary.owl.ttl`](../../ontology/vocabulary.owl.ttl) declares SKOS concept
schemes. Their members are generally defined in the subject modules and
connected with `skos:inScheme`; inspect those files for current membership and
typing.
