"""
A : >=90
  If length seq>10
     This is an ideal seq
  else
     This is not a ideal seq
B : >=80 and <90
C : <80
"""
seq=input("Please enter the sequence")
gc_percentage=100*(seq.count("G")+seq.count("C"))/len(seq)
print(gc_percentage)

if gc_percentage>=90:
    print("A")
    if len(seq)>10:
        print("This is an ideal seq")
    else:
        print("this is not an ideal seq")
elif gc_percentage>=80 and gc_percentage<90:
    print("B")
else:
    print("C")