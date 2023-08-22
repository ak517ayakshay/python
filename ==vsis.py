# both r comparision operator
# is compares exact location of object in memory like vivo y21 is ur moms phone but when adarsh takes it to party he will tell its his(like we r refering to same object)
# == compares values
a=8
b="8"
print(a is b)
print(a==b)
# both r fale
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a==b)
# here it is false true as both r diffrent objects but have same value
a=3
b=3
print(a is b)
print(a==b)
# both r true beocz in python once 3 is created it is created only once in memory location from there it is accssed each time so once u give a=3 memory location is created but when u give b = 3 2nd time same memory location is used so a and b are pointing towards same memory location ie y its true above insead of contants if we give strings,tuples,sets answer is true true