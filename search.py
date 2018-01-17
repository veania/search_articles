from Bio import Entrez
import xml.etree.ElementTree as ET

Entrez.email = "elizarova@phystech.edu"

key_words = '[[ [ seawater OR marine OR sediment OR freshwater OR ocean OR river OR lake OR aquatic] metagenome ] ' \
            'OR [ marine microbial community ]] NOT gut] NOT intestine] NOT human'
handle = Entrez.esearch(db="bioproject", term=key_words)
record = Entrez.read(handle)
handle.close()

handle = Entrez.esearch(db="bioproject", term=key_words, retmax=record['Count'])
record = Entrez.read(handle)
handle.close()

for id in record['IdList']:
    handle = Entrez.efetch(db="bioproject", id=id, retmode='xml')
    record = handle.read()
    handle.close()
    root = ET.fromstring(record)

    project_accession = root.findall('.//ArchiveID')[0].attrib['accession']
    print project_accession
    handle = Entrez.esearch(db="pmc", term=project_accession)
    record = handle.read()
    handle.close()

    root = ET.fromstring(record)
    number_of_results = int(root[0].text)
    if number_of_results != 0:
        id_article = root.findall('.//IdList/Id')[0].text
        print 'ARTICLE_ID:', id_article

        db_name = "pmc"
        handle = Entrez.efetch(db=db_name, id=id_article, retmode='xml')
        record = handle.read()
        handle.close()
        root = ET.fromstring(record)

        title = root.findall('.//title-group/article-title')[0].text
        abstract = root.findall('.//abstract/p')[0].text

        txt = open("Output.txt", "a")
        txt.write('%s\n%s id: %s\nTITLE: %s\nABSTRACT:\n%s\n' %
                  (project_accession, db_name, id_article, title, abstract))
        txt.close()
