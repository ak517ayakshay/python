import time

t = time.strftime('%H:%M:%S')
#strftime is a method which converts dates to string and H M S are written so that time becomes readable that is for python to understand in what way does the user want the output
h = int(time.strftime('%H'))
#here type casting is required becoz strftime converts it to string and we cannot compare string with an integer
print(t)

if (h >= 0 and h < 12):
  print("good morning")
elif (h >= 12 and h <= 16):
  print("good afternoon")
else:
  print("good evening")

  
