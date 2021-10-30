#counting no of lines in a file
path=r"E:\github\test_Oct\day6\sequences.txt"
file=open(path)
lines=file.readlines()
print(len(lines))
#getting any particular lines
print(lines[7])
#creating a data file
data_file=open("data.txt","w")
data_file.writelines(["1\t","2\t","3\t","4\t","\n"])
data_file.writelines(["1\t","2\t","3\t","4\t","\n"])
data_file.writelines(["1\t","2\t","3\t","4\t","\n"])
data_file.writelines(["1\t","2\t","3\t","4\t","\n"])
data_file.close()
#searching in the file
path=r"E:\github\test_Oct\day6\sequences.txt"
file=open(path)
lines=file.readlines()
for line in lines:
    if "AAA" in line:
        print("Found")

count=0
for line in lines:
    if "AAA" in line:
        print("Found")
        count+=1
print(count)
for index,line in enumerate(lines):
    if "AAA" in line:
        print("Found",index)
file.close()


def get_gc_percentage(seq):
    gc_percentage=100*(seq.count("G")+seq.count("C"))/len(seq)
    if gc_percentage>10:
        return True
    else:
        return False

result=filter(get_gc_percentage,lines)
print(list(result))