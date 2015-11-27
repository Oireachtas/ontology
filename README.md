
## Houses of the Oireachtas Ontology

*Draft 1 - Bills*

### Introduction

The Houses of the Oireachtas ontology attempts to describe the business processes and publications produced by the Houses of the Oireachtas within a formal vocabulary that allows documents, legislative events and entities to be linked programmatically.

The ontology is being developed using the [web ontology language  (OWL)](http://www.w3.org/TR/owl-features/) and reuses other ontology schema wherever possible. These are listed in the [Referenced Schema](referenced-schema) section. The Oireachtas ontology extensively reuses the [European Legislative Identifier  (ELI)](http://publications.europa.eu/mdr/eli/documentation/) ontology and [CEN-Metalex](http://www.metalex.eu/), as well as the [Akoma Ntoso](http://www.akomantoso.org/) schema, all of which were designed for legislation and the legislative process.

It is envisaged that the ontology will ultimately describe the following datasets from the Houses of the Oireachtas:
- Bills and other legislation, including motions and amendments
- Sub-units of the Houses of the Oireachtas, such as the Dáil, the Seanad and committees
- the Official Report (debates), including parliamentary questions
- Members
- Departments and other relevant bodies, including political parties
- Roles within the Houses of the Oireachtas (eg, Ministers or Chairs)
- Order papers and journals, including voting records
- Documents laid before the Houses
- Committee reports and submissions

This document deals only with the aspects of the ontology relating to Bills. Things from other datasets may be referenced but have not yet been formally defined.

One of the core functions of any Parliament is to decide on the legal basis for the creation and dissolution of State bodies, and to set the scope of their functions. Where relevant (and feasible) the descriptions of Departments, roles and offices in this ontology will include a link to the decision of the Oireachtas on their creation, modification or dissolution, thereby allowing the Oireachtas dataset to be used as an authority vocabulary for Departments and Ministerial roles.

#### [Terms used](#terms-used)

As the Houses of the Oireachtas can be understand as different things depending on the context, it is useful to clarify at the outset to define how certain terms are being used in this document, as follows:
- A ``thing`` refers to the top level category in the ontology. Every object in the ontology is a thing. A thing might also refer to entities existing outside of the Oireachtas ontology, purely for convenience.
-  The ``Oireachtas`` refers to the Houses of the Oireachtas as a legislative body or parliament.
- The ``Service`` refers to the administrative functions that support the Oireachtas, as set out by the Houses of the Oireachtas Commission Act 2003.
- The ``Houses of the Oireachtas`` refer to the Oireachtas and Service collectively.
- The ``Houses`` refer to the Dáil and Seanad collectively, while individual houses are referred to as ``House``, ``Dáil`` or ``Seanad`` depending on the context.
- A ``committee`` is a subset of one or both Houses given delegated powers either by direction of a House, under Standing Orders of a House or by law.
- A ``chamber`` refers to either a House (ie, the Dáil or Seanad) or a committee of one or both of the Houses
- A ``Member`` is an elected Member of the Oireachtas, a ``Deputy`` is a Member of the Dáil and a ``Senator`` is a Member of the Seanad.

#### [OWL and RDF syntax](#syntax)

OWL uses the [resource description framework (RDF)](http://www.w3.org/RDF/) syntax. The RDF syntax describes data as a series of three-part statements linking things to other things.

The three parts of the statement are called the subject, predicate and object, with the predicate expressing the relationship that the subject has with the object. Thus the sentence ``Enda Kenny holds the office of Taoiseach`` could be expressed in pseudo-rdf as ``<Enda Kenny><holds><office of Taoiseach``, with ``<Enda Kenny>`` as the object of the statement, ``<holds>`` as predicate and ``<office of the Taoiseach>`` as object.

The predicate expresses the relationship from the subject to the object unidirectionally, so the statement cannot be reversed. In other words, one cannot state ``<office of Taoiseach><holds><Enda Kenny>`` but must instead use a new predicate: ``<office of Taoiseach><is held by><Enda Kenny>`` subject-object relations. This statement demonstrates that subjects and objects are mutable, that is, the object of one statement can become the subject of another. Indeed predicates can also be subjects or objects, as with the OWL property ``inverseOf``, which describes two predicates as the inverse of each other: ``<holds><owl:inverseOf><is held by>``.

Each element in an RDF statement is either a [Internationalised resource identifier (IRI)] (http://www.w3.org/Addressing/#background) (an IRI is a generalisation of URIs which permit a wider range of characters) or a literal (or a blank node but these are not important in this discussion). An IRI is a string of characters which can uniquely identify the element. A literal is an element which is not denoted by an IRI, such as a string of text, a number or a date.

OWL ontologies can be divided into three primary types, ``classes``, ``properties`` ``literals``.  A ``class`` corresponds to an RDF subject or object, while a ``property`` corresponds to a predicate. It is possible to sub-class both ``classes`` and ``properties`` in a hierarchical manner, and a particular class or property may be the sub-class of multiple parent classes.

OWL permits the reuse and adaptation of existing ontologies in the development of new ones. This is in fact quite important because describing things using terms common to multiple datasets facilitates the sharing of information across the web. For this reason, the Oireachtas ontology reuses a number of other ontologies, including in particular the [European Legislative Identifier  (ELI)](http://publications.europa.eu/mdr/eli/documentation/) ontology, which is designed to facilitate sharing and integration of legal resources across the European Union, and [CEN-Metalex](http://www.metalex.eu/), which was developed as an interchange format for legal data. However, given the particular nature of the material published by the Houses of the Oireachtas, as well as the procedures through which they are accorded legal status, it is also necessary in some cases to create our own models to properly describe things.

At a document level, [Akoma Ntoso](http://www.akomantoso.org/) is being adopted as an XML schema for publication of the Official Report of Debates, and is being evaluated for Bills. Akoma Ntoso was developed to represent legal, parliamentary and judicial documents in XML format, and is currently under review as an [OASIS](https://www.oasis-open.org/) open standard.

To describe categories and taxonomies of things, including controlled vocabularies as ways to describe them, the [Simple Knowledge Organising Scheme (SKOS)](www.w3.org/TR/skos-reference/) ontology is used. Concept scheme tables can be found in [here](concept-schemes).

#### [URIs](#uris)

The namespace for the Oireachtas ontology is ``http://oireachtas.ie/ontology#``. The string ``oir:`` denotes that the following term is in the Oireachtas namespace. Class names are in camel case with all first letters of words capitalised: ``oir:BillFormat``. Property names are camel case with the very first letter in lower case: ``oir:amendedBy``

The namespace for URLs of instances of classes is ``http://oireachtas.ie`` and the patterns will be further described in the relevant sections.

#### [Schema Overview](#schema-overview)

The ontology is divided into four main areas:

- **Legislative Documents**  
These are the documents published by the Oireachtas as part of a deliberative process in a chamber. The most important example of a legislative document is a Bill, which is a draft law, but legislative documents could also be Standing Orders governing the conduct of business in the Oireachtas; motions that are proposed, moved or agreed by a chamber; documents laid before the Oireachtas; and reports prepared by committees.  

  Legislative Documents do not include documents published by the Service, however.

- **Journal Events**  
These are the procedures through which the business of the Oireachtas is planned and recorded, most importantly in respect of procedures that affect legislative documents during their lifecycle. They are recorded either in the Order Paper, for future events, or in the Official Report of debates, for events that have taken place.

- **Debates**  
These are the elements of the Official Report, or the transcribed record of debates in the chambers. Debates describe who said what, and also the journal events that took place in a chamber, for example, that an amendment to a Bill has been moved by a Member, considered by a chamber and agreed in accordance with Standing Orders. However, not all journal events are documented in the Official Report. For example, documents laid before the Houses, while formally acknowledged in a House, are recorded in the Order Paper rather than in the Official Report.

- **Oireachtas Agents**  
These are the entities who author, produce or modify legislative documents, journal events or debates. They include human individuals and the roles they occupy, such as Members, and collective entities, such as committees or houses. These roles and entities may be defined by legislation or be more informally defined, such as political parties.

#### [Hybrid Entities](#hybrid-entities)
Some things within the ontology cannot be categorised neatly in to one category. For example, an amendment to a Bill is both a legislative document in its own right and a journal event in that it effects a modification of the Bill. For this reason, a thing in question might be classified under multiple classes.

### [Bills](#bills)

A Bill is a proposed law which, after a formal process of deliberation by the Oireachtas, may or may not eventually be enacted after being passed by the Oireachtas and signed by the President, at which stage it becomes an Act.

In this ontology, Bills are described as ``legislative documents`` and as ``journal events``, corresponding to the Bill as a text document and to the procedures which give a Bill its legal standing, respectively.

#### [Bills as legislative documents](#bill-legislative-document)

As a legislative document, a Bill is described with the [functional requirements for bibliographic records (FRBR)](http://www.loc.gov/cds/downloads/FRBR.PDF) entity-relationship model used by both CEN-Metalex and ELI. In this model, a Bill is created as an individual intellectual work  (``eli:LegislativeResource``) and expressed as a series of versions during its lifecycle (``eli:LegalExpression``) which are manifested in a physical form, such as a PDF or XML file (``eli:LegalExpression``).

The Bill as legislative document is also associated with certain metadata about it, such as its sponsor, dates of publication and entry into force (enactment) and the Act it became, if relevant.


##### [Bill document URIs](#bill-doc-uris)

URIs for Bills as legislative documents have the following pattern:

    http://oireachtas.ie/ie/bill/{year}/{order number}/{language}@{version}/{main component}/{sub component}{format extension}

The following table provides example uses of the pattern:

| Class               | Example Value                         | Describes                                                      |
|---------------------|---------------------------------------|----------------------------------------------------------------|
| eli:LegalResource   | ie/bill/2015/44                       | The Bill as a distinct intellectual creation/ as a concept     |
| eli:LegalExpression | ie/bill/2015/44/eng@initiated         | Bill as initiated, English version                             |
|                     | ie/bill/2015/44/gle@initiated         | Bill as initiated, Irish version                               |
|                     | ie/bill/2015/44/mul@/dail             | Bill as initiated, multilingual version (eg, referendum Bills) |
|                     | ie/bill/2015/44/eng@ver_a             | 2nd version of Bill                                            |
|                     | ie/bill/2015/44/eng@ver_b             | 3rd version of Bill                                            |
|                     | ie/bill/2015/44/eng@passed            | Bill as passed by both Houses                                  |
|                     | ie/bill/2015/44/eng@ver_b/main        | Main component of Bill (ie, the Bill in its entirety)          |
|                     | ie/bill/2015/44/eng@ver_b/main/part_1 | Part 1 of the Bill                                             |
| eli:Format          | ie/bill/2015/44/eng@ver_b/main.xml    | Bill in XML (eg, Akoma Ntoso) format                           |
|                     | ie/bill/2015/44/eng@ver_b/main.pdf    | Bill in pdf format                                             |
|                     | ie/bill/2015/44/eng@ver_b/main.htm    | Bill in html format                                            |
|                     | ie/bill/2015/44/eng@ver_b/main.odt    | Bill in open office format                                     |



#### [Bills as journal events](#bill-journal-event)

##### [Bill event URIs](#bill-event-uris)

The URI pattern for Bill events is as follows:

    http://oireachtas.ie/ie/bill/{year}/{order number}/{house}/{event context}/{event topic}

These URI patterns can be distinguished from version URIs because name of House will be in place of language/version element

The following table lists the label and skos:conceptScheme vocabulary for Bill in events along with example URIs (to add concept scheme vocabulary):

| Event                                                     | URI                                          |
|-----------------------------------------------------------|----------------------------------------------|
| First Stage                                               | ie/bill/2015/44/dail/1                       |
| All Stages                                                | ie/bill/2015/44/dail/all                     |
| Second Stage                                              | ie/bill/2015/44/dail/2                       |
| Second and Subsequent Stages                              | ie/bill/2015/44/dail/2_sub                   |
| Order for Second Stage                                    | ie/bill/2015/44/dail/2_ord                   |
| Committee Stage                                           | ie/bill/2015/44/dail/3                       |
| Committee and Remaining Stages                            | ie/bill/2015/44/dail/3_sub                   |
| Order for Committee Stage                                 | ie/bill/2015/44/dail/3_ord                   |
| Report Stage                                              | ie/bill/2015/44/dail/4                       |
| Report and Final Stages                                   | ie/bill/2015/44/dail/4_sub                   |
| Order for Report Stage                                    | ie/bill/2015/44/dail/2_ord                   |
| Fifth Stage                                               | ie/bill/2015/44/dail/5                       |
| Financial Resolution(s)                                   | ie/bill/2015/44/dail/motion/finance_res      |
| Leave to Withdraw (I think always refers to 2nd Stage)    | ie/bill/2015/44/dail/motion/2/withdraw       |
| Instruction to committee                                  | ie/bill/2015/44/dail/motion/instruction      |
| Referral to Select Committee                              | ie/bill/2015/44/dail/motion/referral         |
| From the Seanad                                           | ie/bill/2015/44/dail/seanad_amd              |
| [Seanad Bill amended by the Dáil] Report and Final Stages | ie/bill/2015/44/seanad/4_sub/dail/amd        |
| Motion for Earlier Signature                              | ie/bill/2015/44/dail/motion/early            |
| Motion to Discharge Order for Second Stage                | ie/bill/2015/44/dail/motion/2_order/withdraw |
| Motion to Discharge Committee Stage                       | ie/bill/2015/44/dail/motion/3/withdraw       |
| Statement for Information of Voters: Motion               | ie/bill/2015/44/dail/motion/ref_info         |
| Referendum (Ballot Paper) Order 1998: Motion              | ie/bill/2015/44/dail/motion/ref_ballot       |
| Motion to Recommit (is this always on Report?)            | ie/bill/2015/44/dail/motion/recommit         |
| Restoration of Bill                                       | ie/bill/2015/44/dail/motion/restore          |
| Bill amendment                                            | ie/bill/2015/44/dail/3/amd_1                 |
| Bill recommendation (Seanad)                              | ie/bill/2015/44/seanad/3/rec_1               |
| Bill amendment to amendment                               | ie/bill/2015/44/dail/3/amd_1_1               |

#### [Bill Classes](#bill-classes)

| Class                   | sub-class of /based on                               |                                                                                                        |
|-------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| oir:BillResource        | eli:LegalResource, metalex:BibliographicWork         | The Bill (or amendment) as a distinct intellectual creation/ as a concept                              |
| oir:BillExpression      | eli:LegalExpression, metalex:BibliographicExpression |                                                                                                        |
| oir:BillFormat          | eli:Format, metalex:BibliographicManifestation       |                                                                                                        |
| oir:BillVersion         | eli:Version                                          | Version of Bill (see concept scheme                                                                    |
| oir:BillDelivery        | metalex:LegislativeDelivery                          | The action/event by which Bill first came before the Houses for consideration (see concept scheme)     |
| oir:BillDeliveryOutcome |                                                      | Outcome of oir:BillDelivery (see concept scheme)                                                       |
| oir:BillSource          | equiv./sub-class of oir:Role                         | Source of Bill (see concept scheme)                                                                    |
| oir:BillEvent           | metalex:LegislativeCreation                          | An event that affects the status of a Bill (see concept scheme)                                        |
| oir:BillStage           | oir:BillEvent                                        | The stage of a Bill (See concept schema)                                                               |
| oir:BillStatus          |                                                      | The current status of a Bill (see concept schema)                                                      |
| oir:amendingStage       | metalex:LegislativeModification                      | A stage (ie, committee or report) which can have as its outcome a new version (expression) of the Bill |
| oir:Mover               | metalex:Legislator, oir:Member, oir:Role             | A member who moves a motion, proposes a question or moves an amendment                                 |
| metalex:Result          |                                                      | The outcome of a Bill event                                                                            |
| oir:Amendment           | eli:LegalResource, eli:BillEvent, oir:amendingStage  | An amendment as simultaneously a document and a modifying event                                        |
| oir:AmendmentList       |                                                      | Numbered or unnumbered list of amendments, either proposed or made (see concept scheme)                |

#### [Bill Properties](#bill-properties)

| Property            |                                | Domain                              | Range                                                  | Notes                                                                                                      |
|---------------------|--------------------------------|-------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| eli:is_part_of      |                                | Bill                                | Bills Book                                             |                                                                                                            |
| eli:has_part        |                                | Bills Book                          | Bill                                                   |                                                                                                            |
| eli:is_realized_by  |                                | Bill Resource                       | Bill Expression                                        |                                                                                                            |
| eli:realizes        |                                | Bill Expression                     | Bill Resource                                          |                                                                                                            |
| eil:is_embodied_by  |                                | Bill Expression                     | Bill Format                                            |                                                                                                            |
| eli:embodies        |                                | Bill Format                         | Bill Expression                                        |                                                                                                            |
| eli:uri_schema      |                                |                                     |                                                        | URL for resource describing schema??                                                                       |
| eli:id_local        |                                | Bill Resource, Expression, Format   | either Bill URI or {year}-{no}                         |                                                                                                            |
| eli:type_document   |                                | Bill Resource                       | eil:ResourceType                                       | Eg, Bill, Act, Explanatory Memorandum or Draft Bill. Consult w A.G.                                        |
| eli:passed_by       |                                | Bill Resource (final stage)         | oir:oireachtas                                         | Perhaps oireachtas.ie should be the URI for the body corporate                                             |
| eli:date_document   |                                | Bill Resource                       | xsd:Date                                               | Date of President's signature                                                                              |
| eli:related_to      |                                | Bill Resource/Expression            | owl:Thing                                              | Use to relate to draft/heads of Bills, explanatory memos                                                   |
| eli:language        |                                | Bill Expression                     | lang:ENG, lang:GLE or lang:MUL                         |                                                                                                            |
| eli:title           |                                | Bill Expression                     | xsd:string(lang en or ga)                              | Short title, used for versions (LegalExpression) of Bill                                                   |
| eli:published_in    |                                | Bill Format                         | eg, http://oireachtas.ie/legislative_observatory       | "publication in which legal resource is published", eg, website                                            |
| eli:description     |                                | Bill Resource/Expression            | xsd:string(lang en or ga)                              | Bill long title                                                                                            |
| eli:publisher       |                                | Bill Expression/Format              | xsd:String - "Houses of the Oireachtas Service"        | Or just "Houses of the Oireachtas" for historical compliance                                               |
| eli:format          |                                | Bill Format                         | eg iana:text/xml, iana:text/html, iana:application/pdf |                                                                                                            |
| eli:version         |                                | Bill Expression                     | eg, oir:as_initiated                                   | See concept scheme                                                                                         |
| eli:version_date    |                                | Bill Expression                     | xsd:Date                                               | Date presented, passed or ordered to be printed                                                            |
| eli:rightsholder    |                                | Bill Format                         | xsd:AnyURI oir:oireachtas                              |                                                                                                            |
| eli:licence         |                                | Bill Format                         | xsd:AnyURI "http://oireachtas.ie/licence"              |                                                                                                            |
| eli:legal_value     |                                | Bill Format                         | probably eli:LegalValue-authoritive                    |                                                                                                            |
| dcterms:title       |                                | Bill Resource                       | xsd:string(lang en or ga)                              | Short title, for work (LegalResource) of Bill                                                              |
|                     |                                |                                     |                                                        |                                                                                                            |
| oir:originalTitle   |                                | Bill Resource                       | xsd:string(lang en or ga)                              | Short title of LegalResource as initiated                                                                  |
| oir:amended         | frbr:realizer                  | oir:chamber                         | Bill Expression                                        | Dáil, Seanad or committee responsible for amended version                                                  |
| oir:amendedBy       | frbr:realizerOf                | Bill Expression                     | oir:Chamber                                            | inverse of oir:amends                                                                                      |
| oir:sponsored       | frbr:realizer                  | oir:role or oir:person              | Bill Expression                                        | Bill sponsor (this also covers relevant Minister in case of Seanad Bills)                                  |
| oir:sponsoredBy     | frbr:realizerOf                | Bill Expression                     | oir:role or oir:person                                 | inverse of oir:sponsored                                                                                   |
| oir:delivered       | lkif:actor                     | oir:role or oir:person              | Bill Work                                              | agent, ie, Minister, Member or private person, who introduced Bill                                         |
| oir:deliveredBy     | lkif:actor_in                  | Bill Resource                       | oir:role or oir:person                                 | inverse of oir:delivered                                                                                   |
| oir:enactedAs       | possibly frbr:transformationOf | Bill Resource                       | Act Resource                                           | relationship between Act and Bill                                                                          |
| oir:enacts          | possibly frbr:transformation   | Act Resource                        | Bill Resource                                          |                                                                                                            |
| oir:status          |                                | Bill Resource                       | oir:BillStatus                                         | The stage that the Bill has reached (see concept scheme)                                                   |
| oir:inChamber       |                                | oir:BillEvent                       | oir:Chamber                                            | The House/committee in which a Bill event occurs                                                           |
| metalex:agent       |                                | oir:Mover                           | oir:BillEvent                                          | The act of beginning an event by moving a motion/amendment or proposing a question                         |
| oir:commenced       |                                | oir:BillEvent                       | xsd:Date or xsd:DateTime                               | The date on which the event commenced                                                                      |
| oir:concluded       |                                | oir:BillEvent                       | xsd:Date or xsd:DateTime                               | Date on which event concluded                                                                              |
| oir:debate          | metalex:matterOf               | oir:BillEvent                       | oir:debateRecord/dbsect                                | Reference to debate record(s) for event, at debateSection level                                            |
| oir:debateAbout     | metalex:matter                 | oir:debateRecord                    | oir:BillEvent                                          | inverse of oir:debateOn                                                                                    |
| metalex:matter      |                                | oir:BillEvent                       | Bill Resource                                          | the subject mater (the Bill) of the event                                                                  |
| metalex:matterOf    |                                | Bill Resource                       | oir:BillEvent                                          | inverse of metalex:matter                                                                                  |
| metalex:result      |                                | oirBillEvent                        | metalex:Result                                         | How the motion/question/amendment was decided                                                              |
| oir:eventContent    |                                | oir:BillEvent                       | oir:debateRecord/dbsect#sum or para                    | The eId in the debateRecord where the event is moved/proposed, at paragraph/summary or debateSection level |
| oir:eventContentOf  |                                | oir:debateRecord/dbsect#sum or para | oir:BillEvent                                          | inverse of oir:eventSubject                                                                                |
| oir:resultContent   |                                | oir:BillEvent                       | oir:debateRecord/dbsect#sum or para                    | The eId in the debateRecord where the event is decided at paragraph/summary or debateSection level         |
| oir:resultContentOf |                                | oir:debateRecord/dbsect#sum or para | oir:BillEvent                                          | inverse of oir:resultContent                                                                               |
| oir:amended         |                                | oir:Amendment                       | Bill Expression                                        | The version (expression) of the Bill which an amendment(s) modifies                                        |
| oir:amendedBy       |                                | Bill Expression                     | oir:Amendment                                          | The version (expression) that is created on foot of an amendment(s)                                        |
| metalex:predecessor |                                | Bill Expression, AmendmentList      | Bill Expression, AmendmentList                         | Is the preceeding version (expression) of a Bill or Amendment list                                         |
| metalex:successor   |                                | Bill Expression, AmendmentList      | Bill Expression, AmendmentList                         | inverse of metalex:predecessor                                                                             |

#### [Concept Schemes](#concept-schemes)

| oir:BillVersions                        |
|-----------------------------------------|
| oir:as_initiated                        |
| oir:as_a                                |
| oir:as_b                                |
| oir:as_c                                |
| oir:dail_passed                         |
| oir:seanad_passed                       |
| oir:passed                              |
|                                         |
| **oir:BillDelivery**                    |
| oir:application                         |
| oir:introduction                        |
| oir:presentation                        |
|                                         |
| **oir:BillDeliveryOutcome**               |
| oir:report_of_examiner_of_private_bills |
| oir:introduced                          |
| oir:refused_introduction                |
| oir:presented                           |
|                                         |
| **oir:BillSource**                        |
| oir:government                          |
| oir:private_member                      |
| oir:private_sponsor                     |
|                                         |
| **oir:BillStatus**                        |
| oir:current                             |
| oir:lapsed                              |
| oir:defeated                            |
| oir:withdrawn                           |
| oir:rejected_by_referendum              |
| oir:subject_to_referendum               |
| oir:awaiting_signature                  |
| oir:draft_heads                         |
| oir:enacted                             |
|                                         |
| **oir:BillStage**                         |
| oir:first_stage                         |
| oir:second_stage                        |
| oir:third_stage                         |
| oir:fourth_stage                        |
| oir:fifth_stage                         |


#### [Namespaced Schema](#referenced-schema)

| prefix  | namespace                                                 |
|---------|-----------------------------------------------------------|
| eli     | http://data.europa.eu/eli/ontology#                       |
| lang    | http://publications.europa.eu/resource/authority/language |
| oir     | http://oireachtas.ie/ontology#                            |
| iana    | http://www.iana.org/assignments/media-types/              |
| metalex | http://www.metalex.eu/metalex/2008-05-02#                 |
