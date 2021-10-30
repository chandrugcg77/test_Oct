path=r"sequences.txt"
file=open(path,"w")

#write
file.write("ATGATAGTAGAAGTAGATA\n")
file.write("ATGATAGAGA\n")
file.write("ATGATAGATATA\n")
#writeline
file.writelines("ATGATAGATAATAATTA\n")
file.writelines("ATGATAGATATAAAA\n")
file.writelines("ATGATAGATATAATTATAT\n")

#Additional Functionality
list_seq=["TATAGATAA\n","ATAATTAAAA\n"]
file.writelines(list_seq)
file.writelines(["Anand\n","Kumar"])
#At the end
file.close()