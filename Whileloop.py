num=3
while num<=30:
    print(num)
    num+=3

seq="ATAGTAGATAGTAGATAAGATATAGTAA"
#    0 2  5 7 9
index=0
list_result=[]
while index<len(seq):
    if seq[index]=="A": #== , !=
        list_result.append(index)
    index+=1
print(list_result)


seq="ATGAT"
index=0
list_result=[]
last_found_domain_index=-1
while index<len(seq):
    found_result=seq.find("AT",last_found_domain_index+1)
    if found_result!=-1:
        list_result.append(found_result)
        last_found_domain_index=found_result
        index+=last_found_domain_index
    index+=1
print(list_result)


#look for the domain
print("ATG" in seq)
seq="ATGAT"
print("ATAAAG" in seq)