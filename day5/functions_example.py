def check_sequence(rna_seq):
    result={"UAA":0,
           "UGA":0,
            "UAG":0
           }
    for codons in ["UAA","UGA","UAG"]:
        if codons in rna_seq:
            result[codons]+=1
    return result
rna_seq="UAAAAGGCGAGAUAAAUA"  
print(check_sequence(rna_seq))

seq="ATAGT"

gc_percent=100*(seq.count("G")+seq.count("C"))/len(seq)
print(gc_percent)

#definition
def calculate_gc_percentage(seq):
    gc_percent=100*(seq.count("G")+seq.count("C"))/len(seq)
    return gc_percent

#calling
print(calculate_gc_percentage("ATAGTAGAAT"))
print(calculate_gc_percentage("AA"))



# def get_all_codons():
#     return ["UAA","UGA","UAG"]



# def download_covid_sequences():
#     #
    

# print(get_all_codons())



def calculate_area(l,w):
    return l*w



length=10
width=100

print(calculate_area(length,width))


def count_motifs(seq,motif):
    return seq.count(motif)


print(count_motifs("ATAGGATATA","TA"))
print(count_motifs(motif="TA",seq="ATAGGATATA"))
print(count_motifs("ATAGGA","TA"))

#loop index
def get_alll_indexes(seq,motif):
    index=0
    list_result=[]
    last_found_domain_index=-1
    while index<len(seq):
        found_result=seq.find(motif,last_found_domain_index+1)
        if found_result!=-1:
            list_result.append(found_result)
            last_found_domain_index=found_result
        index+=1
    return list_result
 
print(get_alll_indexes("ATAGGATATA","TA"))


import re
def get_all_indexes_new(seq,motif):
    indexes=[]
    for index in list(re.finditer(motif,seq)):
        indexes.append((index.start(),index.end()))
    return indexes

print(get_all_indexes_new("ATAGGATATA","TA"))


def calculate_gc_percentage(seq):
    gc_percent=100*(seq.count("G")+seq.count("C"))/len(seq)
    return gc_percent

from statistics import mean

def get_avg_gc_percentage(seq1,seq2):
    return  mean([calculate_gc_percentage(seq1),calculate_gc_percentage(seq2)])


print(get_avg_gc_percentage("ATGC","GG"))