#to change or modify a tuple u must convert it to list first and then do but u can concatinate two tuples as u r making a new tuple
t=(1,2,3,4,5,1,2,3,5,6,3)
print(t.count(1))
# same as that of in list
print(t.index(2))
# u can also see index of particular element in specific range too
print(t.index(1,2,6))

# here it is finding 1 in space of 2 to 6 tuple is first sliced in btwn 2 to 6 amd then  index is found