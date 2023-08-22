def cube(n):
    '''this function takes in a number and returns the cube of it'''
    # the above statement is not a comment its a docstring
    return n*n*n
p=cube(3)
print(p)
print(cube.__doc__)
# "THESE SHOULD BE WRITTEN JUST BELOW FUNCTION DEFINATION , METHOD,CLASS OR ELSE THEY WONT BE CONSIDERED"
# this is the way to access the doc string
# these r not ignored like comments they r given a special priority by the python compiler
# they can be used in functions classes etc they tell brief about i/o of function basically describes wt does the function / a class work for
# __doc__ is called as doc attribute
#pep 8
#guildline for python programing it makes python progrm readable maintainable and compileable
# zen of python
# know abt this