name = "!!akshay!.....!!!!!"
print(name.upper())
#strings are imutable(u cant change them when u do name.upper new string is given the old string is not modified) meaning it doesnt change ur previous change it creates new string and applies the change which is given by u
print(name.lower())
print(name.strip("!"))
#strip removes the items mentioned in the braces which are  "only at the end or beginning"
print(name.rstrip("!"))
#this strips from right side that is which are present at the end
print(name.lstrip("!"))
#this strips from left side that is which are present at the beginning
print(name.replace("akshay", "aky"))
#this replaces all occurences of 1st string with second string
food = "rice wheat curd"
print(food.split(" "))
#this splits the string into a LIST each element of list is taken until symbol given un braces is found
cudi = "kkk.ffjjf.jror0..rh"
print(cudi.split("."))
#here spliting took place wrt to a dot(.)
nam = "akshay is a legeNd"
print(nam.capitalize())
#capitalise function capitalizes 1st letter and rest to lower case
print(nam.center(100))
#50 spaces are added front and back
str = "India is ind and it is India Indiasss"
print(str.replace("India", "ind"))
print(str.endswith("asss"))
#this checks for endswith
# 1. strings are immutable.
# 2. any method on string takes a copy of the object.
# 3.string.upper will convert the string to an upper case
# 4.string.lower will convert the string to lower case
# 5. string.rstrip("character") will strip the trailing characters of string 
# 6.string.replace("character/alphabets", new character/alphabets") will replace the existing specified alphabets in string with new ones
# 7. string.split splits the string at the given alphabet and returns a list of items
# 8.string.capitalize capitalizes the first character of the word and turns rest all the characters to lower case
# 9.string.center center aligns the string by adding the number of spaces mentioned in parenthesis
# 10. string.count counts the total number of a particular set of characters in a string
# 11. string.endswith checks whether a string ends with the specific characters
# 12.string.find finds the first occurrence of a given value and return the index value of the position of that occurrence
# 13.string.index finds the occurrence of a given value and returns the index value of the position however, if it is unable to find it will give an error causing the program to exit
# 14.string.isalnum checks to find if string is alphanumeric and returns true or false
# 15.string.isalpha checks if there are any numbers in the string
# 16.string.islower checks if there are only lower aphabets in the string
# 17. string.isprintable checks if all the characters are printable in the string(non printable characters e.g \n)
# 18 string.isspace checks if any space bar has been used in the string
# 19.string.istitle The istitile() returns True only if the first letter of each word of the string is capitalized, else 20. string.isupper checks if all characters are uppercase in a string
# 21. string.startswith checks if a string starts with a given value
# 22. string.swapcase convert uppercase to lowercase and vice versa in a string
# 23.string.title converts first character of all the words in the sentence to capital