from Bio import Entrez
from Bio import SeqIO
Entrez.email = "akr.cpibtc@gmail.com"
handle = Entrez.esearch(db="nucleotide", retmax=5, term="BRCA", idtype="acc")
record = Entrez.read(handle) #dictionary
print(record["Count"])
print(record["IdList"])

for id in record["IdList"]:
    handler=Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    record=SeqIO.read(handler,"gb")
    print(id,"==>",record.description)