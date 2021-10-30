from Bio import SeqIO
path=r"E:\github\test_Oct\day8\covid_seq.gb"

genbank_record=SeqIO.read(path,"genbank")
# print(genbank_record)
# print(type(genbank_record))

#.seq ==> sequence
print(genbank_record.seq)

#.id ==> id of sequence
print(genbank_record.id)

#.name==> name of seq
print(genbank_record.name)

#.description
print(genbank_record.description)

#.features ==> gives the list of all the features
print(genbank_record.features)
print(len(genbank_record.features))
for ft in genbank_record.features:
    print(ft)
for ft in genbank_record.features:
    if ft.type=="CDS":
        print(ft.type)
        print(ft.extract(genbank_record.seq))
        print(len(ft.extract(genbank_record.seq)))

#counting
covid_seq=genbank_record.seq
print(type(covid_seq))
print(covid_seq.count("A"))
print(covid_seq.count("G"))
print(covid_seq.count("ATTTAA"))

#indexing
print(covid_seq[99])

restriction_enzyme_site="ATA"
fragments=str(covid_seq).split(restriction_enzyme_site)
print(fragments)
print(len(fragments))

#list comprehension
fragments_gt_100=[fr for fr in fragments if len(fr)>100]
#                [varname for varname in data if varname ]
print(len(fragments_gt_100))
rna=covid_seq.transcribe()
#translate
translation_p=rna.translate()
print(translation_p)
a_chains=translation_p.split("*")
print(a_chains)

fil_aa_chains=[len(chains) for chains in a_chains if (len(chains)>0 and len(chains)<100)]
print(len(fil_aa_chains))

#import matplotlib.pyplot as plt
#plt.plot(fil_aa_chains)
#plt.show()
a_chains=[chains for chains in a_chains if (len(chains))>0]
from Bio.SeqUtils.ProtParam import ProteinAnalysis
for chains in a_chains:
    protein=ProteinAnalysis(str(chains))
    print(chains,protein.aromaticity(),protein.isoelectric_point())
#https://biopython.org/docs/1.76/api/Bio.KEGG.Compound.html