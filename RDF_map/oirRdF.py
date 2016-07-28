import re, csv, json, os
from pprint import pprint
from dateutil import parser
from rdflib import URIRef, Literal, Namespace, Graph
from rdflib.namespace import RDF, OWL, SKOS, DCTERMS, XSD, RDFS, FOAF

ELI = Namespace("http://data.europa.eu/eli/ontology#")
OIR = Namespace("http://oireachtas.ie/ontology#")
CEN = Namespace("http://www.metalex.eu/metalex/2008-05-02#")
FRBR= Namespace("http://purl.org/vocab/frbr/core#")
ORG = Namespace("http://www.w3.org/ns/org#")
DBO = Namespace("http://dbpedia.org/ontology/")
TIME = Namespace("http://www.w3.org/2006/time#")
DBP = Namespace("http://dbpedia.org/resource/")

oir = Namespace("http://oireachtas.ie/ie/oireachtas/")
eli = Namespace("http://oireachtas.ie/eli/ie/oir/")


DATADIR = "../data"

GRAPH_FILE = "../data/member.ttl"

def load_graph():
    g.parse(GRAPH_FILE)

def initialize_graph(g):
    #for initialzing new graphs
    g.bind("eli", ELI)
    g.bind("oir", OIR)
    g.bind("owl", OWL)
    g.bind("metalex", CEN)
    g.bind("frbr", FRBR)
    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS)
    g.bind("org", ORG)
    g.bind("dbo", DBO)
    g.bind("time", TIME)

def house_triples(g):
    with open(os.path.join(DATADIR, "dail.json")) as f:
        dail = json.load(f)
    with open(os.path.join(DATADIR, "seanad.json")) as f:
        seanad = json.load(f)
    houses = seanad+dail
    for i, house in enumerate(houses):
        hnum = house['houseNum']
        uri = house["houseURI"][1:]
        g.add((oir[uri], RDF.type, OIR.HouseTerm))
        if uri.split("/")[-2] == "seanad":
            chamber = "seanad"
        else:
            chamber = "dail"
        if chamber == "seanad" and len(hnum) == 4:
            other_label = "First Seanad"
            g.add((oir[uri], SKOS.altLabel, Literal(other_label, lang="en")))
        g.add((oir[uri], OIR.termOf, oir[chamber]))
        g.add((oir[uri], RDFS.label, Literal(house['houseName'], lang="en")))
        end = house['end'] if type(house['end']) != float else None
        commenced = "{}/start/{}".format(uri, house['start'])
        g.add((oir[uri], OIR.start, oir[commenced]))
        g.add((oir[commenced], CEN.xsdDate, Literal(house['start'], datatype=XSD.date)))
        g.add((oir[commenced], RDF.type, OIR.EventDate))
        if hnum != "1" and hnum != "1922":
            if chamber == "seanad" and (len(hnum) == 4 or hnum == "2"):
                if hnum == "2":
                    pre = "1934"
                else:
                    pre = str(int(hnum) - 3)
            else:
                pre = str(int(hnum)-1)
            preceding = uri.replace(hnum, pre)
            g.add((oir[uri], OIR.precededBy, oir[preceding]))
            g.add((oir[preceding], OIR.succeededBy, oir[uri]))
            #print(uri, "=====", preceding)
        if chamber == "dail":
            cabURI = "cabinet/dail/{}".format(hnum)
            cabLabel = "Government of the "+house['houseName']
            cabAltLabel = "Cabinet of the "+house['houseName']
            cabStart = house['start']
            g.add((oir[cabURI], RDF.type, OIR.Cabinet))
            g.add((oir[cabURI], OIR.cabinetOf, oir[uri]))
            g.add((oir[cabURI], RDFS.label, Literal(cabLabel, lang="en")))
            g.add((oir[cabURI], SKOS.altLabel, Literal(cabAltLabel, lang="en")))
            cabCommenced = "{}/start/{}".format(cabURI, cabStart)
            g.add((oir[cabURI], OIR.start, oir[cabCommenced]))
            g.add((oir[cabCommenced], CEN.xsdDate, Literal(cabStart, datatype=XSD.date)))
            g.add((oir[cabCommenced], RDF.type, OIR.EventDate))
        if end:
            dissolved = "{}/end/{}".format(uri, end)
            g.add((oir[uri], OIR.end, oir[dissolved]))
            g.add((oir[dissolved], CEN.xsdDate, Literal(house['end'], datatype=XSD.date)))
            g.add((oir[dissolved], RDF.type, OIR.EventDate))
            if chamber == "dail" and i+1 < len(houses):
                cabEnd = houses[i+1]['start']
                cabEndURI = "{}/end/{}".format(cabURI, cabEnd)
                g.add((oir[cabURI], OIR.ended, oir[cabEndURI]))
                g.add((oir[cabEndURI], CEN.xsdDate, Literal(cabEnd, datatype=XSD.date)))
                g.add((oir[cabEndURI], RDF.type, OIR.EventDate))


def members_triples(g):
    with open(os.path.join(DATADIR, "members.json")) as f:
        members = json.load(f)
    for m in members:
        uri = m['eId'][1:]
        db = "http://dbpedia.org/resource/"+m['wikiTitle'].replace(" ", "_")
        g.add((oir[uri], RDF.type, OIR.Member))
        g.add((oir[uri], ORG.memberOf, OIR.Oireachtas))
        g.add((oir[uri], OWL.sameAs, URIRef(db)))
        g.add((oir[uri], FOAF.name, Literal(m['fullName'])))
        g.add((oir[uri], FOAF.firstName, Literal(m['firstName'])))
        g.add((oir[uri], FOAF.familyName, Literal(m['lastName'])))
        for d in ["date_of_birth", "date_of_death"]:
            if m.get(d):
                g.add((oir[uri], DBO[d], Literal(m[d], datatype=XSD.date)))
        if m.get("memberid"):
            mId = "members-hist/default.asp?housetype=&MemberID="+m['memberid']
            g.add((oir[uri], OIR.MemberId, oir[mId]))
        for t in ['profession', "details", "showAs", "pId"]:
            if m.get(t):
                g.add((oir[uri], OIR[t], Literal(m[t], lang="en")))


def service_triples(g):
    with open(os.path.join(DATADIR, "service.json")) as f:
        service = json.load(f)
    g.add((OIR.EventDate, RDFS.subClassOf, TIME.TemporalEntity))
    for s in service:
        eId = s['eId'][1:]

        house = s["houseURI"][1:]
        #serviceURI in json ends with dail.31 - turning that into dail/31
        service_uri = s['serviceURI'][1:].split("/")
        service_uri = "/".join(service_uri[:-1]+[service_uri[-1].replace(".", "/")])
        period = "{}/period".format(service_uri)
        if s['elected'] is not None:
            elected = "{}/elect/{}".format(service_uri, s['elected'])
        commenced = "{}/start/{}".format(service_uri, s['periodStart'])
        concluded = "{}/end/{}".format(service_uri, s['periodEnd']) if type(s['periodEnd']) != float else None

        if house.split("/")[-2] == "dail":
            title = "Deputy"
        else:
            title = "Senator"
        g.add((oir[eId], ORG.member, oir[service_uri]))
        g.add((oir[service_uri], RDF.type, ORG.Membership))
        g.add((oir[service_uri], ORG.role, OIR[title]))
        g.add((oir[service_uri], ORG.organisation, oir[house]))
        g.add((oir[service_uri], ORG.memberDuring, oir[period]))
        for c in s['constURI']:
            g.add((oir[service_uri], OIR.represent, oir[c]))
        g.add((oir[period], RDF.type, TIME.ProperInterval))
        if s['elected'] is not None:
            g.add((oir[period], OIR.elect, oir[elected]))
            g.add((oir[elected], RDF.type, OIR.EventDate))
            g.add((oir[elected], CEN.xsdDate, Literal(s['elected'], datatype=XSD.date)))
        g.add((oir[period], OIR.start, oir[commenced]))
        g.add((oir[commenced], CEN.xsdDate, Literal(s['periodStart'], datatype=XSD.date)))
        g.add((oir[commenced], RDF.type, OIR.EventDate))
        if concluded:
            g.add((oir[period], OIR.end, oir[concluded]))
            g.add((oir[concluded], RDF.type, OIR.EventDate))
            g.add((oir[concluded], CEN.xsdDate, Literal(s['periodEnd'], datatype=XSD.date)))


def government_member_triples(g):
    with open(os.path.join(DATADIR, "government_members.json")) as f:
            government_members = json.load(f)
    for s in government_members:
        eId = s['eId'][1:]
        role = "role"+s['uri']
        label = s['office']
        g.add((oir[role], RDF.type, OIR.Minister))
        g.add((oir[role], RDFS.label, Literal(label, lang="en")))
        if "functions" in s.keys():
            for function in s['functions']:
                function_label = function.replace("_", " ").title()
                function_uri = "minister/function/"+function
                g.add((oir[role], OIR.hasMinisterialFunction, oir[function_uri]))
                g.add((oir[function_uri], OIR.ministerialFunctionOf, oir[role] ))
                g.add((oir[function_uri], RDF.type, OIR.MinisterialFunction))
                g.add((oir[function_uri], RDFS.label, Literal(function_label, lang="en") ))
        for cab in s['cabinets']:
            try:
                cabinet = cab['cabinet'].split("oireachtas/")[1]
            except IndexError:
                cabinet = cab['cabinet'][1:]
            if cabinet[0] != "c":print(cabinet)
            cab_membership = eId + "/" + cabinet + s['uri']
            period = cab_membership + "/period"
            start = cab_membership + "/start/" + cab['start']
            g.add((oir[cab_membership], ORG.organisation, oir[cabinet]))
            g.add((oir[cab_membership], RDF.type, ORG.Membership))
            g.add((oir[cab_membership], ORG.role, oir[role]))

            g.add((oir[eId], ORG.member, oir[cab_membership]))

            g.add((oir[cab_membership], ORG.memberDuring, oir[period]))
            g.add((oir[period], RDF.type, TIME.ProperInterval))
            g.add((oir[period], OIR.start, oir[start]))
            g.add((oir[start], CEN.xsdDate, Literal(cab['start'], datatype=XSD.date)))
            g.add((oir[start], RDF.type, OIR.EventDate))
            if cab['end'] is not None:
                end = cab_membership + "/end/" + cab['end']
                g.add((oir[period], OIR.end, oir[end]))
                g.add((oir[end], CEN.xsdDate, Literal(cab['end'], datatype=XSD.date)))
                g.add((oir[end], RDF.type, OIR.EventDate))

def party_triples(g):
    with open(os.path.join(DATADIR, "parties.json")) as f:
            party_members = json.load(f)
    for p in party_members:
        member = p['member'][1:] if p['member'].startswith("/") else p['member']
        dbp = "http://dbpedia.org/resource/"+p['party']
        start = p['start']
        end = p['end']
        party_membership = "{}/{}".format(p['uri'], p['oir_party'])
        party_membership = party_membership[1:] if party_membership.startswith("/") else party_membership
        period = party_membership+"/period/"+start
        g.add((oir[member], ORG.member, oir[party_membership]))
        g.add((oir[party_membership], RDF.type, ORG.Membership))
        g.add((oir[party_membership], ORG.organisation, oir[p['oir_party']]))
        g.add((oir[p['oir_party']], RDFS.label, Literal(p['oir_party'].replace("_", " "), lang="en") ))
        g.add((oir[p['oir_party']], RDF.type, OIR.Party))
        g.add((oir[party_membership], URIRef("http://dbpedia.org/property/party"), URIRef(dbp)))
        g.add((oir[party_membership], ORG.memberDuring, oir[period]))
        g.add((oir[period], RDF.type, TIME.ProperInterval))
        g.add((oir[period], OIR.start, oir[start]))
        g.add((oir[start], CEN.xsdDate, Literal(p['start'], datatype=XSD.date)))
        g.add((oir[start], RDF.type, OIR.EventDate))
        if p['end'] is not None:
            end = party_membership + "/end/" + p['end']
            g.add((oir[period], OIR.end, oir[end]))
            g.add((oir[end], CEN.xsdDate, Literal(p['end'], datatype=XSD.date)))
            g.add((oir[end], RDF.type, OIR.EventDate))

def serialize_graph(g, file_name):
    g.serialize(destination=(os.path.join(DATADIR, file_name)), format="turtle")

def main():
    #initialize graph
    g= Graph()
    print("Graph Initialized")
    initialize_graph(g)
    house_triples(g)
    print("houses:", len(g))
    members_triples(g)
    print("members:", len(g))
    service_triples(g)
    print("service:", len(g))
    government_member_triples(g)
    print("cabinets:", len(g))
    party_triples(g)
    print("party triples:", len(g))
    #file_name = "parties.ttl"
    file_name = "oireachtas.ttl"
    serialize_graph(g, file_name)
    print("Graph serialized")

if __name__ == '__main__':
    main()
