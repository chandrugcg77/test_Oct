seq=input("Please enter the sequence: ")
length=len(seq)
if length>9:
    print("This is an ideal sequence")
else:
    print("This is not an ideal sequence")
"""
A : >=90
B : >=80 and <90
C : <80
"""
seq=input("Please enter the sequence")
gc_percentage=100*(seq.count("G")+seq.count("C"))/len(seq)
print(gc_percentage)

if gc_percentage>=90:
    print("A")
elif gc_percentage>=80 and gc_percentage<90:
    print("B")
else:
    print("C")