""" 
   You can use funtion as a argument to another funtion. 
   Program to print your name multiple times :)
   Let's see how it looks like..!
"""

#funtion to return name five times.
def five_times(name):
  return name * 5

#funtion to return the above funtion.
def applied_fun(fun_name,your_name):
  return fun_name(your_name)

#finally call the functions.
print(applied_fun(five_times, "some_name\n"))
