import re, csv, json, os, requests
from lxml import etree
from pprint import pprint
from dateutil import parser
from rdflib import URIRef, Literal, Namespace, Graph
from rdflib.namespace import RDF, OWL, SKOS, DCTERMS, XSD, RDFS, FOAF
from config import EXIST, GRAPHDB

ELI = Namespace("http://data.europa.eu/eli/ontology#")
OIR = Namespace("http://oireachtas.ie/ontology#")
CEN = Namespace("http://www.metalex.eu/metalex/2008-05-02#")
FRBR= Namespace("http://purl.org/vocab/frbr/core#")
ORG = Namespace("http://www.w3.org/ns/org#")
DBO = Namespace("http://dbpedia.org/ontology/")
TIME = Namespace("http://www.w3.org/2006/time#")

oir = Namespace("http://oireachtas.ie/")
eli = Namespace("http://oireachtas.ie/eli/ie/oir/")

DATADIR = "../data"

NS = {'akn': "http://docs.oasis-open.org/legaldocml/ns/akn/3.0/CSD13"}

def initialize_graph(g):
    #for initialzing new graphs
    g.bind("oir", OIR)
    g.bind("dcterms", DCTERMS)

def debate_triples(g, fp):
    root = etree.parse(fp).getroot()
    date = root.find(".//{*}FRBRWork/{*}FRBRdate").attrib['date']
    house= root.find(".//{*}FRBRWork/{*}FRBRauthor").attrib['href'][1:]
    debate_uri = root.find(".//{*}FRBRWork/{*}FRBRuri").attrib['value'][1:].replace("akn/ie", "ie/oireachtas")
    g.add((oir[debate_uri], RDF.type, OIR.DebateRecord))
    g.add((oir[debate_uri], DCTERMS.date, Literal(date, datatype=XSD.date)))
    g.add((oir[debate_uri], OIR.inChamber, oir[house]))
    for dbsect in root.xpath(".//akn:debateSection[@name='debate']|.//akn:debateSection[@name='question']", namespaces=NS):
        dbs_uri = debate_uri + "/" + dbsect.attrib['eId']
        heading = dbsect.find("./{*}heading").text
        debate_type = dbsect.attrib['name']

        g.add((oir[dbs_uri], RDF.type, OIR.DebateSection))
        g.add((oir[dbs_uri], OIR.partOf, oir[debate_uri]))
        g.add((oir[debate_uri], OIR.part, oir[dbs_uri]))

        g.add((oir[dbs_uri], OIR.debateType, OIR[debate_type]))
        g.add((oir[dbs_uri], DCTERMS.title, Literal(heading)))
        try:
            bill_uri = dbsect.attrib['refersTo'][1:].replace(".", "/")
            g.add((oir[dbs_uri], OIR.subject, oir[bill_uri]))
            g.add((oir[bill_uri], OIR.subjectOf, oir[dbs_uri]))
        except KeyError:
            pass
        for spk in dbsect.xpath(".//akn:speech|.//akn:question", namespaces=NS):
            contrib_uri = debate_uri + "/" + spk.attrib['eId']
            pId = spk.attrib['by'][1:]
            contrib_type = spk.tag.split("}")[-1].title()
            g.add((oir[contrib_uri], RDF.type, OIR.contrib_type))
            g.add((oir[contrib_uri], OIR.partOf, oir[dbs_uri]))
            g.add((oir[dbs_uri], OIR.part, oir[contrib_uri]))
            if len(pId)>0:
                member = root.find(".//{*}TLCPerson[@eId='"+pId+"']").attrib['href'][1:]
                g.add((oir[contrib_uri], OIR.madeBy, oir[member]))
                g.add((oir[member], OIR.made, oir[contrib_uri]))
            if "as" in spk.attrib.keys():
                role = root.find(".//{*}TLCRole[@eId='"+spk.attrib['as'][1:]+"']").attrib['href'][1:]
            if "to" in spk.attrib.keys():
                questionee = root.find(".//{*}TLCRole[@eId='"+spk.attrib['to'][1:]+"']").attrib['href'][1:]
                g.add((oir[contrib_uri], OIR.questionTo, oir[questionee]))
            if "refersTo" in spk.attrib and spk.attrib['refersTo'].startswith("#pq"):
                pq_uri = debate_uri + "/" + spk.attrib['refersTo'][1:]
                g.add((oir[contrib_uri], OIR.answerTo, oir[pq_uri]))
                g.add((oir[pq_uri, OIR.answer, oir[contrib_uri]]))
            for para in spk.findall(".//{*}p"):
                p_uri = debate_uri + "/" + para.attrib['eId']
                g.add((oir[p_uri], RDF.type, OIR.DebateParagraph))
                g.add((oir[p_uri], OIR.partOf, oir[contrib_uri]))
                g.add((oir[contrib_uri], OIR.part, oir[p_uri]))


def get_debate_records():
    dbrecs = etree.parse('../data/debateRecords_1919-2015.xml').getroot()
    return dbrecs.xpath("debateRecord[@house='dail']")

def serialize_graph(g, file_name):
    g.serialize(destination=(os.path.join(DATADIR, file_name)), format="turtle")

def main():
    meta = "../data_2016-06-05/dail"
    for fp in os.listdir(meta):
        g= Graph()
        initialize_graph(g)
        debate_triples(g, os.path.join(meta, fp))
        file_name = os.path.join(DATADIR, "debatesRDF/dail", fp.replace(".xml", ".ttl"))
        serialize_graph(g, file_name)
        import_path = "data/import/url/oireachtas"
        data = {"context":"urn:debates",
                "url": "file:///"+os.path.join(DATADIR, file_name),
                "baseURI": "http://oireachtas.ie",
                "dataFormat":"turtle"}
        r = requests.post(GRAPHDB+import_path, data=data)
        if r.status_code != 202:
            print(fp, "\n", r.text)
            break


if __name__ == '__main__':
    main()
