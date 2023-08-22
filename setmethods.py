s1={1,2,3,4}
s2={3,4,5}
print(s1.union(s2))
# this is same as that of maths 
s1.update(s2)

# this update function brings in those values which r in s2 but not in s1 this basically updates s1 union doesnt changes the sets but update func does
print(s1.intersection(s2))
# this does intersection
s1.intersection_update(s2)
# this is like update but in intersection it updates s1 to intersection set of both s1 and s2
print(s1)
print(s1.symmetric_difference(s2))
# this is like a-b
# u also have symmetric diffrence update
print(s1.isdisjoint(s2))
# compares 2 sets and prints the value true if all elements of set r =
print(s2.issuperset(s1))
s1.add(7)
# adds the element
s1.remove(1)
s1.discard(3)
# the main diffrence between remove and discard in sets is remove func throws error if element is not present whereas discard func doesnt thorws an error
s1.pop()
# this method removes the last element of the test but as the sets are unordered we dont know wch element is being removed