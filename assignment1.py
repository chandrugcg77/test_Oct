sequences=["ATGATAAGAT","ATCGAGCTGAT"]
print(len(sequences))
sequences=("ATCAGCGATGTCGATGCTAGT")
print(len(sequences))
gc_percentages=("ATGCGCGCGCGCGCATCGCGCGCG")
print(gc_percentages)
#indexing

#              -4       -3         -2             -1           #RIGHT-LEFT
sequences=["ATAGAT","ACTAGTA","ATCGAATGTAG","ATCGTAATGAT"]
#              0       1         2             3           #LEFT-RIGHT

print(sequences[0])
print(sequences[1])
print(sequences[-2])

list_example=["A","T","C"]
list_example.reverse()
print(list_example)
