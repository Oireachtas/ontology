## Ontology of Houses, Constituencies, Parties, Members and Member Roles

The [Organisation](https://www.w3.org/TR/vocab-org/) ontology is extensively reused to model the organisational and temporal components of the Houses of the Oireachtas, Members of the Houses and the roles they play, including in ministerial and committee positions.

Member, House and Cabinet data can be downloaded in ttl format from /data/member-house-cabinet.ttl

### [Houses of the Oireachtas and Cabinets](#houses)

Houses of the Oireachtas are modelled as both temporal entities, which correspond to the period of existence of an individual Dáil or Seanad, and also as continuous entities corresponding to the concept of the setting in which the debates take place, as well as the entity commonly understood as the Dáil or Seanad. This setting is described by the class ``Chamber``, which in this context denotes a continuous entity associated not so much with the physical location of the particular House as the idea of a debating chamber. A ``chamber`` can also describe a committee. A ``Chamber`` is a direct sub-class of the class ``oir:Oireachtas``, which in turn sub-classes ``org:FormalOrganisation``

The temporal quality is described by the class ``HouseTerm``, which is a sub-class of both ``oir:Oireachtas`` and ``time:ProperInterval``. A ``HouseTerm`` has a start date and end date (if the House has dissolved) corresponding to the relevant House's first sitting and dissolution, respectively. Again, a committee can be an instance of ``HouseTerm``.

With the exception of the pre-1936 Seanad, Houses are identified by their name ("Dáil", "Seanad" or committee name) and for the Dáil and Seanad, their sequential number. The pre-1936 Seanad was continuous, with Members either appointed or elected for terms ranging from three to nine years, and elections held every three years between 1922 and 1936. By convention, the Seanad as it existed until it was abolished until 1936 is also known as the First Seanad (although this is not reflected in the URIs), and the first Seanad elected under the Constititution as the Second Seanad.

The [time]() ontology is adapted to describe temporal events by creating a subclass of time:ProperInterval, ``oir:EventDate``. The ``time:EventDatetime`` class is not appropriate for the Oireachtas events because the time element is not present.

Cabinets are described by the class ``oir:Cabinet`` and are modeled as temporal entities similar to ``oir:HouseTerm``. All Cabinets except the provisional government are coterminous with the Dáil to which they are linked. This is not absolutely accurate because under the Constitution, governments (and their members) remain in place beyond the dissolution of a Dáil until they are replaced by the new Government.


#### [House and Cabinet URI patterns](#house-uri)

``http://oireachtas.ie/ie/oireachtas/house/{house}/{house number}/{start|end}/{xs:date}``
``http://oireachtas.ie/ie/oireachtas/cabinet/{house}/{house number}/{start|end}/{xs:date}``

- ``house`` is either *dail* or *seanad*
- ``house number`` is the sequential number of a term of the Dáil or the Seanad or, in the case of the pre-1936 Seanad, a year of elections of a proportion of its Members.
- One of ``commenced``, ``dissolved`` followed by xs:date string is the oir:EventDate for date of election, commencement or dissolution of the term.

This table provides example usage of the URI pattern:

|class|example URI|Describes|
|-----|--|--|
|oir:Chamber|/house/dail|The Dáil as a debating chamber/setting|
|oir:HouseTerm|/house/dail/31|The 31st Dáil|
|oir:EventDate|/house/dail/31/start/2011-03-09|Commencement of 31st Dáil|
|oir:EventDate|/house/dail/31/end/2016-02-03|Dissolution of 31st Dáil|
|oir:Cabinet|/cabinet/dail/31|The Cabinet of the 31st Dáil|

#### [House and Cabinet classes](#house-class)

|Class|Sub-Class of/based on|Description|
|-|-|-|
|oir:Oireachtas|org:FormalOrganisation|The Houses of the Oireachtas|
|oir:Chamber|oir:Oireachtas, metalex:Agent, rda:Agent|Dáil, Seanad or committee as continuous entity/debate setting|
|oir:HouseTerm|oir:Oireachtas, time:ProperInterval|Term of existence of a Chamber|
|oir:EventDate|time:TemporalEntity|The date on which an event occurs|


#### [House and Cabinet properties](#house-property)

Relevant sub-classes are set out below, but see the [Organisation](https://www.w3.org/TR/vocab-org/) ontology for more complete documentation.

| Property|Domain| Range | Notes  |
|-|
|oir:termOf|oir:HouseTerm|oir:Chamber|Term of the Dáil or Seanad (or committee)|
|oir:hasTerm|oir:Chamber|oir:HouseTerm|Inverse of oir:termOf|
|oir:start|time:TemporalEntity|oir:EventDate|Start date of period of oir:HouseTerm|
|oir:end|time:TemporalEntity|oir:EventDate|End date of period of oir:HouseTerm|
|oir:precededBy|oir:HouseTerm|oir:HouseTerm|Expressing succession|
|oir:succeededBy|oir:HouseTerm|oir:HouseTerm|Expressing succession|
|oir:cabinetOf|oir:Cabinet|oir:HouseTerm|The Cabinet or Government of a Dáil|


### [Members of the Oireachtas](#members)

Members of the Oireachtas are modelled using the ``foaf`` schema to describe their biographical details, the ``eli`` and ``metalex`` schema for their legislative agency, and the ``organisation`` schema for their temporal roles as Deputies or Senators; Ministers and Ministers of State; party membership; committee members; and chairs of Oireachtas bodies, such as Ceann Comhairle or committee chair.

For convenience, Members URIs are linked to the relevant DBpedia URI by means of an ``owl:SameAs`` property.

The image below is an example of how the organisation ontology is used describe periods of Cabinet membership. Periods of membership of the Dáil or Seanad are described using the same method.

![Membership schematic](BertieTaoiseach.jpg)

#### [Member URI patterns](#member-uri)

http://oireachtas.ie/ie/oireachtas/member/{firstname}-{opt middle name or initial}-{last name}.{D|S}.{xs:date}

member/{firstname}-{opt middle name or initial}-{last name}.{D|S}.{xs:date}/{dail|seanad}/{house number}/{elected|commenced|ended}/{date}

|class|example URI|Describes|
|-----|--|--|
|oir:Member|/member/Enda-Kenny.D.1975-11-12|Enda Kenny, an individual who was elected to the Oireachtas.|
|org:Membership|/member/Enda-Kenny.D.1975-11-12/dail/31|Enda Kenny's membership of the 31st Dáil|
|time:ProperInterval|/member/Enda-Kenny.D.1975-11-12/dail/31|The period during which Enda Kenny was a Member of the 31st Dáil|
|oir:EventDate|/member/Enda-Kenny.D.1975-11-12/dail/31/elect/2011-02-25|The date of Enda Kenny's election to the 31st Dáil|
|oir:EventDate|/member/Enda-Kenny.D.1975-11-12/dail/31/start/2011-03-09|The commencement date of Enda Kenny's period of service in the 31st Dáil|
|oir:EventDate|/member/Enda-Kenny.D.1975-11-12/dail/31/end/2016-02-03|The end date of Enda Kenny's period of service in the 31st Dáil|
|org:Membership|member/Enda-Kenny.D.1975-11-12/cabinet/dail/31|Enda Kenny's membership of the Government (Cabinet) of the 31st Dáil|
|time:ProperInterval|/member/Enda-Kenny.D.1975-11-12/cabinet/dail/31|The period during which Enda Kenny was a member of Government of the 31st Dáil|



#### [Member Classes](#member-class)

Relevant sub-classes are set out below, but see the [Organisation](https://www.w3.org/TR/vocab-org/) ontology for more complete documentation.

|Class|Sub-Class of/based on|Description|
|-|-|-|
|oir:Member|metalex:Legislator, foaf:Person, rda:Person|An individual agent who at some stage was a Member of the Oireachtas|
|oir:MinisterialRole|org:Role|Ministerial role during a period of ``org:Membership`` of Cabinet|
|oir:GovernmentMembers|foaf:Group, org:OrganisationalUnit|The collective of Members who support the Government|
|oir:OppositionMembers|foaf:Group, org:OrganisationalUnit|The collective of Members who oppose the Government|
|oir:PrivateMember|oir:BillSource|A Member of the Oireachtas who is not a Member of Cabinet|

#### [Member properties](#member-property)

| Property|Domain| Range | Notes  |
|-|
|foaf:familyName|oir:Member|xs:string| |
|foaf:firstName|oir:Member|xs:string| |
|foaf:Name|oir:Member|xs:string| |
|foaf:profession|oir:Member|xs:string|Career background of Member|
|dbo:date_of_birth|oir:Member|xs:string|Where available|
|dbo:date_of_death|oir:Member|xs:string|Where available|
|org:memberOf|oir:Member|oir:Oireachtas| |
|oir:elected|time:TemporalEntity|oir:EventDate|date of election|
|oir:start|time:TemporalEntity|oir:EventDate|Start date of period of membership|
|oir:end|time:TemporalEntity|oir:EventDate|End date of period of membership|
|oir:governmentOf|oir:GovernmentMembers|oir:HouseTerm|Linking Government members to relevant House|
|oir:oppositionOf|oir:OppositionMembers|oir:HouseTerm|Linking Opposition  members to relevant House|
