set_example={"ATGCT","ATAGTATA","ATGCT"} #set will remove the duplicate members
print(set_example)


set_example={"YC1","YC2","YC3","YC3"}
print(set_example)

t_cell_epitopes={"LPVLQV","FGDSVE","VEKGVLPQLEQ","ARTAPH","EIPVA"}
b_cell_epitopes={"ARTAPH","IQYG","EIPVA"}


#all the available epitopes
#union operation
all_epitopes=t_cell_epitopes|b_cell_epitopes
print(all_epitopes)

# #common eitopes
common_epitopes=t_cell_epitopes&b_cell_epitopes
print(common_epitopes) 
#all the epitopes that are present in tcell but in bcell
print(t_cell_epitopes-b_cell_epitopes)

#all the epitopes that are present in bcell but in tcell
print(b_cell_epitopes-t_cell_epitopes)
#all the epitopes that are present in either t cell or bcell but not in both
#symmetric difference
print(b_cell_epitopes^t_cell_epitopes)

set1={1,2,3}
set2={3,4}
print((set1|set2)-set1)

b_cell_epitopes={"ARTAPH","IQYG","EIPVA"}

b_cell_epitopes.add("IQY")
print(b_cell_epitopes)
b_cell_epitopes.add("IQY")
b_cell_epitopes.add("IQY")
b_cell_epitopes.add("IQY")
print(b_cell_epitopes)