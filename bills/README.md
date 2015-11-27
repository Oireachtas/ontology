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
