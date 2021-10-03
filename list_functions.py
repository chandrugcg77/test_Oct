# remove()  Removes the first item with the specified value
list_example=[1,1,1,2,3,4,3]
list_example.remove(1)
print(list_example)
# reverse() Reverses the order of the list
list_example=[1,2,3]
list_example.reverse()
print(list_example)
# sort()    Sorts the list
gc_percentages=[10.8,34,12,90,99,92]
gc_percentages.sort()
print(gc_percentages)

# clear()   Removes all the elements from the list
sequences=["atagt","atgata"]
sequences.clear()
print(sequences)


# copy()    Returns a copy of the list
sequences1=["atagt","atgata"]
sequences2=sequences1.copy()
sequences2.clear()
print(sequences1)
print(sequences2)
list_1=[1,2]
list_2=[3,4]

new_list=list_1+list_2
print(new_list)

new_list=list_2+list_1
print(new_list)


#extend
list_1.extend(list_2)
list_3=[9,8]
list_1.extend(list_3)
print(list_1)