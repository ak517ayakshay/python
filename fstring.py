# introduced from python 3.6 onwards


name = "akshay"
country = "india"
print(f"my name is {name} and i am from {country}")
# f here means formatted string
# you can also give it to integers and even round off and even u can modify the strings
print(f"my name is {name[0:4]} and i am from {country}")
cgpa=9.17777
print(f"my name is {name} and my cgpa is {cgpa:0.2f}")
# this rounded off to 9.18
print(f"my name is {{name}} and i am from {{country}}")
# this prints the string as it is