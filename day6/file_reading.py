path=r"E:\github\test_Oct\day6\sequences.txt"
file=open(path,"r")
#file=open(path)
# read()  ⇒ Returns message in the file as string 
# file_contents=file.read()
# print(file_contents)
# readline() ⇒ reads file line by line (single line)
line1=file.readline()
line2=file.readline()
print(line1,line2)
# readlines() ⇒ Returns list of lines in the file
list_lines=file.readlines()
print(list_lines)