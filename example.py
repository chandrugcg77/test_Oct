list_example=[]
print(list_example)
list_example=[1,2,3,4]
print(list_example)
sequences=["ATGATAAGAT","ATAGTATAA","ATAGTAGAAT"]
print(sequences)
#len ==> get the length of the list
#syntax==> len(name_of_list)
print(len(sequences))
print(len(list_example))

list_example=[]
print(len(list_example))
# Inserting element at any position
#list_name(index,data)
sequences.insert(0,"ATGC")
print(sequences)
sequences.insert(2,"ATGC")
print(sequences)


seq=[]
seq.append("ATGC")  #["ATGC"]
seq.append("AAA") #["ATGC","AAA"]
seq.insert(0,"CC")   #["CC","ATGC","AAA"]
print(seq)