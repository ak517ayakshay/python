#block under this gets executed irrespective of error occured or no
try:
    b=int(input("En") )
except:
    print("inavlid input")
finally:
    print("i am executed  the either ways")        
    #this statement executed both the cases
# VVIP main use case of finally **************************
# def func():
#     try:
#       b=int(input("En") )
#       return 1
#     except:
#      print("inavlid input")
#      return 0
#     print("i am executed both the timws")
# x=func()
# here we can see that the print statement did not get executed but if use finally IT GETS EXECUTED EVEN AFTER THE RETURN STATEMENT this is the main use case of finally
def func1():
    try:
      return 1
    except:
     print("inavlid input")
     return 0
    finally:
        print("i am executed both the timws")
# x=func()
y=func1()
# this is the main use case of finally the block of it gets executed even after the function return finally matlab honna he honna hai execute hokke he rahega mera bachha