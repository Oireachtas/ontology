## Department Ontology

Departments could be conceived as particular arrangements of modular functions, which are organised according to an org:ChangeEvent which takes legal form in a Statutory Instrument (SI) under [section 6 (1) of the Ministers and Secretaries (Amendment) Act, 1939](http://www.irishstatutebook.ie/eli/1939/act/36/section/6/enacted/en/html#sec6) or the various Ministers and Secretaries Acts.

The list of orders made under the 1939 Act is [here](http://www.irishstatutebook.ie/eli/isbc/ordersundersection6.html).

Departments are offices operating functions on behalf of Ministers, who is assigned certain roles under the relevant Statutory Instrument.

Ministers are Members of the Oireachtas who are also members of the Cabinet, which for the purpose of this ontology is the equivalent as the definition of Government in [Article 28.1 of the Constitution](http://www.irishstatutebook.ie/eli/cons/en/html#part5). That Article also establishes the roles of Taoiseach and Tánaiste.

Ministers of State are appointed by order of the Dáil (confirm this).

A Minister without portfolio is a Member who has been appointed to the Cabinet but does not yet have a formal ministerial role because the relevant SI has not issued. I don't know if appointment dates are retrospective.

###URLs

Names for specific Department and Ministerial roles consist of their functions (with the words "Department of" removed) separated by double underscores:

department/function1__function2_function3
minister/trade__industry__commerce

Where a function name is a phrase rather than a single word, the words in the phrase are separated by a single underscore:
department/foreign_affairs__trade
minister_state/social__protection

For ministerial or Cabinet roles:

http://oireachtas.ie/taoiseach
http://oireachtas.ie/tanaiste

http://oireachtas.ie/minister/{specific title}
http://oireachtas.ie/minister_state/{specific title}

http://oireachtas.ie/minister_without_portfolio

Where a Departmental function is a phrase rather than a single


http://oireachtas.ie/department/{department specific name}
http://oireachtas.ie/department/transport__tourism__sport

For departmental functions or areas:

http://oireachtas.ie/department/function/{function}/{SI date}
http://oireachtas.ie/department/function/transport/2011-03-29

The Statutory Instrument date (SI) is either the date of the SI published under the 1930 Act or the appointment date in the case of SIs for other Ministers and Secretaries Acts.

A challenge with this the date of SI is that the date of signature of the Statutory Instrument must be parsed from its text - as does the departmental function. One alternative is to use the date on which the Taoiseach announced the Ministerial appointment or department reshuffle, but this is not the official date of appointment.
