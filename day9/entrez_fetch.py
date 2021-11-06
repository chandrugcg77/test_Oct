from Bio import Entrez
from Bio import SeqIO
Entrez.email = "akr.cpibtc@gmail.com"
handler = Entrez.efetch(db="nucleotide", id="AY851612", rettype="gb", retmode="text")
#1)genbank ==>rettype="gb"
#2)fasta ==>rettype="fasta"

print(handler.read(),file=open("AY851612.gb","w"))