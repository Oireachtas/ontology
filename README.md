
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

#### [OWL and RDF syntax](syntax)

OWL uses the [resource description framework (RDF)](http://www.w3.org/RDF/) syntax. The RDF syntax describes data as a series of three-part statements linking things to other things.

The three parts of the statement are called the subject, predicate and object, with the predicate expressing the relationship that the subject has with the object. Thus the sentence ``Enda Kenny holds the office of Taoiseach`` could be expressed in pseudo-rdf as ``<Enda Kenny><holds><office of Taoiseach``, with ``<Enda Kenny>`` as the object of the statement, ``<holds>`` as predicate and ``<office of the Taoiseach>`` as object.

The predicate expresses the relationship from the subject to the object unidirectionally, so the statement cannot be reversed. In other words, one cannot state ``<office of Taoiseach><holds><Enda Kenny>`` but must instead use a new predicate: ``<office of Taoiseach><is held by><Enda Kenny>`` subject-object relations. This statement demonstrates that subjects and objects are mutable, that is, the object of one statement can become the subject of another. Indeed predicates can also be subjects or objects, as with the OWL property ``inverseOf``, which describes two predicates as the inverse of each other: ``<holds><owl:inverseOf><is held by>.

Each element in an RDF statement is either a [Internationalised resource identifier (IRI)] (http://www.w3.org/Addressing/#background) (an IRI is a generalisation of URIs which permit a wider range of characters) or a literal (or a blank node but these are not important in this discussion). An IRI is a string of characters which can uniquely identify the element. A literal is an element which is not denoted by an IRI, such as a string of text, a number or a date.

OWL ontologies can be divided into three primary types, ``classes``, ``properties`` ``literals``.  A ``class`` corresponds to an RDF subject or object, while a ``property`` corresponds to a predicate. It is possible to sub-class both ``classes`` and ``properties`` in a hierarchical manner, and a particular class or property may be the sub-class of multiple parent classes.

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

A Bill is a proposed law which, after a formal process of deliberation by the Oireachtas, may or may not eventually be enacted after being passed by the Oireachtas and signed by the President, at which stage it becomes an Act. Bills are a particular type of legislative document

#### [Bills as legislative documents](#bill-legislative-document)

##### [Bill document URIs]#(bill-doc-uris)

URIs for Bills as legislative documents have the following pattern:

    http://oireachtas.ie/ie/bill/{year}/{order number}/{language}@{version}/{main component}/{sub component}{format extension}

The following table provides example applications of the pattern:

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

##### [Bill event URIs]#(bill-event-uris)

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

#### [Referenced Schema](#referenced-schema)

| prefix  | namespace                                                 |
|---------|-----------------------------------------------------------|
| eli     | http://data.europa.eu/eli/ontology#                       |
| lang    | http://publications.europa.eu/resource/authority/language |
| oir     | http://oireachtas.ie/ontology#                            |
| iana    | http://www.iana.org/assignments/media-types/              |
| metalex | http://www.metalex.eu/metalex/2008-05-02#                 |
