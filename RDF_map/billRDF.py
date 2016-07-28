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

oir = Namespace("http://oireachtas.ie/ie/oireachtas/")
eli = Namespace("http://oireachtas.ie/eli/ie/oir/")


DATADIR = "../data"

GRAPH_FILE = "../data/billsbook.ttl"

stageLU = {'1': 'FirstStage',
 '2': 'SecondStage',
 '2_ord': 'OrderSecondStage',
 '3': 'CommitteeStage',
 '3_ord': 'OrderCommitteeStage',
 '4': 'ReportStage',
 '4_ord': 'OrderReportStage',
 '5': 'FifthStage',
 'seanad_amd': 'SeanadAmdDail',
 'deemed':"DeemedPassed",
 'withdrawn':"LeaveToWithdraw",
 'lapsed':"LapsedBillEvent",
 'restored':"RestoredBill",
 'finance_res':"FinancialResolution",
 "rejected":"BillRejection"}

status_lu = {"rejected":"DefeatedBill",
            "awaiting_sign":"AwaitingSignatureBill",
            "current":"CurrentBill",
            "draft":"DraftHeadsofBill",
            "enacted":"EnactedBill",
            "lapsed":"LapsedBill",
            "rejected_by_referendum":"RejectedAtReferendumBill",
            "subject_ref":"SubjectToReferendumBill",
            "withdrawn":"WithdrawnBill",
            "invalid":"RepugnantToConstitutionBill"}
def load_graph():
    g.parse(GRAPH_FILE)

#pprint(members[43])

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

def bill_triples(g):
    with open(os.path.join(DATADIR, "ParsedBillsBook.json"), "r") as f:
        bills = json.load(f)
    for b in bills:
        uri = b['uri'].lower()
        if "amendment of the constitution" in b["bill_title_sh_en"].lower():
            bill_init = uri+"/mul@initiated"
        else:
            bill_init = uri+"/eng@initiated"
        g.add((oir[uri], RDF.type, OIR.BillResource))
        g.add((oir[bill_init], RDF.type, OIR.BillExpression))
        g.add((oir[bill_init], ELI.realizes, oir[uri]))
        g.add((oir[uri], ELI.is_realized_by, oir[bill_init]))
        g.add((oir[uri], DCTERMS.title, Literal(b["bill_title_sh_en"], lang="en")))
        g.add((oir[uri], DCTERMS.title, Literal(b["bill_title_sh_ga"], lang="ga")))
        g.add((oir[uri], DCTERMS.title, Literal(b["bill_title_sh_ga"], lang="ga")))
        g.add((oir[uri], ELI.type_document, OIR.Bill))
        g.add((oir[uri], OIR.billStatus, OIR[status_lu[b['status']]]))
        g.add((oir[uri], OIR.billSource, OIR[b['source'].replace(" ", "")+"Bill"]))
        g.add((oir[uri], OIR.billDelivery, OIR[b['method'].replace(" ", "")]))
        if b['status'] == "enacted":
            g.add((oir[uri], ELI.date_document, Literal( b['date_signed'], datatype=XSD.date) ))
            try:
                g.add((oir[uri],  OIR.enactedAs, URIRef(b['act_uri']) ))
            except TypeError:
                print(b['act_uri'])
            g.add((URIRef(b['act_uri']), oir.enacts, oir[uri] ))
        if 'bill_title_long_en' in b.keys():
            g.add(( oir[uri], ELI.description, Literal(b['bill_title_long_en'], lang="en") ))
        if 'bill_title_long_ga' in b.keys():
            g.add(( oir[uri], ELI.description, Literal(b['bill_title_long_ga'], lang="ga") ))
        if 'bill_title_sh_orig_en' in b.keys():
            g.add(( oir[uri], OIR.originalTitle, Literal(b['bill_title_sh_orig_en'], lang="en")  ))
            g.add(( oir[uri], OIR.originalTitle, Literal(b['bill_title_sh_orig_ga'], lang="ga")  ))
        if "sponsorRole" in b.keys():
            for sponsor in b['sponsorRole']:
                if "roleURI" in sponsor.keys():
                    g.add(( oir[bill_init], OIR.sponsoredBy, URIRef(sponsor['roleURI']) ))
                    g.add(( URIRef(sponsor['roleURI']), OIR.sponsored, oir[bill_init] ))


        for e in b['events']:
            elems = e['uri'].split("/")
            if elems[-1] == "signature":
                pass
            else:
                event_name = stageLU[elems[-1]]
                if elems[3] in ['dail', 'seanad']:
                    house = elems[3]
                else:
                    house = e['stage'].split("/")[3]
                g.add(( oir[uri], CEN.matterOf, oir[e['uri']] ))
                g.add(( oir[e['uri']], CEN.matter, oir[uri] ))
                g.add(( oir[e['uri']], OIR.billEventType, OIR[event_name] ))
                g.add(( oir[e['uri']], OIR.inChamber, oir[house] ))
                g.add(( oir[e['uri']], DCTERMS.date, Literal(e['date'], datatype=XSD.date) ))
                if "stage" in e.keys():
                    on_stage = e['stage']
                    stage_elems = on_stage.split("/")
                    stage_name = stageLU[stage_elems[-1]]
                    stage_house = stage_elems[3]
                    g.add(( oir[on_stage], OIR.onStage, oir[on_stage] ))
                    g.add(( oir[on_stage], OIR.billEventType, OIR[stage_name] ))
                    g.add(( oir[on_stage], OIR.inChamber, oir[stage_house] ))



def serialize_graph(g, file_name):
    g.serialize(destination=(os.path.join(DATADIR, file_name)), format="turtle")

def main():
    #initialize graph
    g= Graph()
    print("Graph Initialized")
    initialize_graph(g)
    bill_triples(g)
    print("bills:", len(g))
    file_name = "bills.ttl"
    serialize_graph(g, file_name)
    print("Graph serialized")

if __name__ == '__main__':
    main()
