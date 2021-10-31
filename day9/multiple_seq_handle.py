from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd
path=r"E:\github\test_Oct\day9\ls orchid.fasta"
records=SeqIO.parse(path,"fasta") #iterator object

# count=0
# for seq_records in records:
#     print(seq_records.id)
#     count+=1
# print(count)

seq_records=list(records)
print(len(seq_records))



data=pd.DataFrame.from_dict({
    "id":[seq.id for seq in seq_records],
    "length":[len(seq.seq) for seq in seq_records],
    "gc":[GC(seq.seq) for seq in seq_records]
})
print(data)

data_len_700=data.loc[(data["length"]>700) & (data["gc"]>50)&(data["gc"]<55)]
print(data_len_700)
print(len(data_len_700))
data_len_700.to_excel("filtered_data.xlsx")
data_len_700.to_csv("filtered_data.csv")
data_len_700.to_string("result.txt")


records=[seq for seq in seq_records if len(seq.seq)>700 and GC(seq.seq)>55 ]
SeqIO.write(records,"filtered_fasta_seq.fasta","fasta")