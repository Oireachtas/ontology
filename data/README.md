
## Oireachtas Member Data



Oireachtas Members' biographical information and Cabinet roles, compiled from information extracted from the [Department of the Taoiseach](http://taoiseach.ie/eng/Historical_Information/History_of_Government/), the [Oireachtas Members' database](http://www.oireachtas.ie/members-hist/) and [Wikipedia](https://en.wikipedia.org/wiki/Category:Oireachtas). The data is provided in json format.

Data on party membership, Ministers of State, chairs of the Houses and of committees and committee membership will be added shortly. This is still a work in progress, so please let us know if you spot any errors or gaps in the data.

### The Data

This repository contains the following data:

- ``members.json``

  Basic biographical information about Members of the Oireachtas extracted from the [Oireachtas Members' database](http://www.oireachtas.ie/members-hist/), including name and, where available, birth-date, death-date, profession and additional details. The ``eId`` URI which allows Members to be cross-referenced with the other files in this repository. The eId string consists of Member fullName and the date of first entry/election to the Dáil or Seanad (denoted by ``D`` or ``S``, respectively).

  The ``memberid``, ``electionid`` (not complete) and ``wikiTitle`` fields contain cross-references to Member data contained in the [Oireachtas Members' database](http://www.oireachtas.ie/members-hist/), ElectionsIreland.org and Wikipedia page titles, respectively. The ``pId`` field is mainly an internal reference for the Oireachtas Debates authoring system but it also provides a unique identifier for all Members who have been recorded as contributing to a debate in the Dáil or Seanad.

- ``dail.json`` and ``seanad.json``

  Sets out number and name of each Dáil and Seanad, along with date of establishment and date of dissolution, uniquely identified by ``houseURI``, which is a string consisting of the name of the chamber(dail or seanad) followed by its number.

- ``service.json``

  The periods which each Member (identified by ``eId``) served in the Dáil and Seanad, including election date, date of first entry to the relevant House and date of conclusion of that period, whether because of death, resignation or dissolution. A Member is elected for a constituency, identified by ``constURI`` - this is contained in an array because some Deputies in the first four Dáileanna were elected in multiple constituencies. The relevant House is identified by ``houseURI`` and each service also has a unique ``serviceURI`` comprising a combination of Member ``eId`` and ``houseURI``


- ``ministers.json``, ``taoisigh.json`` and ``tanaiste.json``

  Cabinet roles since the first Dáil, including title of office as a string, holder (which is the same as ``eId`` in members.json) and start and end dates of the relevant individual's period in that office. Periods as Minister conclude (or should conclude) no later than the dissolution of the relevant Dáil, but Taoiseach and Tánaiste periods can span several Dáileanna.

  URIs for ministerial offices haven't yet been developed, so in the meantime the ``wikiOffice`` field offers a way of grouping offices by area (based on the most recent name of the office in most cases.)
