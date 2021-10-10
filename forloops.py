seq="AAATGATAGATGATAGA"

for bases in seq:
    print(bases)
    
#reading the list by using the for loop
sequences=["TAGATA","AAATAGAT","TTAATA"]
for seq in sequences:
    print(seq,len(seq))

seq_data={
    "id":"21345",
    "seq":"atagatagtagata",
    "founder":"Nitin"
}
for data in seq_data:
    print(data,seq_data[data])

