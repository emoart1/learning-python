# variables in Python
# there are 4 different types of variables in python: integers, floats, strings, and booleans 
# integers are numbers without decimal points 
x = 1 

# floats are numbers with decimal points 
y = 1.5 

# strings are sequences of characters 
z = "Hello, World!" 

# booleans are values that are either True or False 
a = True 
b = False 

# to specify the type of a variable, you can use casting, which is the process of converting a variable from one type to another, for example: 
c = int(1.5) 
# c will be 1, because the decimal part is truncated 

d = float(1) 
# d will be 1.0, because it is converted to a float 

e = str(1) 
# e will be "1", because strings are converted to text 

f = bool(1) 
# f will be True, because any non-zero number is considered True when converted to a boolean 

# you can also use the type() function to check the type of a variable, for example: 
print(type(c))  # <class 'int'> 
print(type(d))  # <class 'float'> 
print(type(e))  # <class 'str'> 
print(type(f))  # <class 'bool'> 

# for strings, you can use single quotes or double quotes, but I would recommend using double quotes for consistency (so you don't have problems with apostrophes), for example: 
g = "I don't want to have problems with apostrophes!" 

# you can also use triple quotes for multi-line strings 
h = """This is a multi-line string. 
It can span multiple lines without the need for escape characters.""" 

# you can also use the len() function to get the length of a string 
print(len(z))  # it would print 13 

# you can also use the + operator to concatenate strings 
i = z + " " + g 
print(i)  # it would print "Hello, World! I don't want to have problems with apostrophes!" 

# you can also use the * operator to repeat strings 
j = z * 3 
print(j)
# it would print "Hello, World!Hello, World!Hello, World!" 

# you can also use the in operator to check if a substring is in a string
print("Hello" in z)  # it would print True 

# variables can also be named using letters, numbers, and underscores and they can be as long as you want them to be, but they cannot start with a number 
greeting = "Hello, I'm learning about Python!" 
print(greeting)  # it would print "Hello, I'm learning about Python!" 

# if you want to make a variable that has a name that is more than one word, I'd recommend using underscores or to capitalize the first letter of each word 
today_is_a_good_day = False 
TodaysDateIs = "24/6/2026" 

# and do not under any circumstances use a dash (-) in a variable name, because it will be interpreted as a minus sign and will cause an error!!! 

# you can also assign multiple variables at once 
k, l, m = 1, 2.5, "Hello!" 
print(k)  # it would print 1 
print(l)  # it would print 2.5 
print(m)  # it would print "Hello!" 

# you can also assign the same value to multiple variables at once
n = o = p = True 
# now n, o, and p are all have a value of True :) 

# you can quickly assign a value to a variable by using a list, tuple, etc. 
list_of_values = ["it's 3:28 pm...", "I'm tiered...", "Hello..."] 
q, r, s = list_of_values 
print(s + " " + q + " " + r) # it would print "Hello... I'm tiered... it's 3:28 pm..." 

# you can overwrite a variable by simply assigning it a new value
x = 10 # it would overwrite the value of x to 10, and now x is 10 instead of 1

# global variables are variables that are defined outside of a function and can be accessed from anywhere in the code, they are defined using the global keyword 
def cool(): 
    return("cool!")   # return is used becouse if I would use print it would the equivalent of print(f"cool!\npython is ") 

def my_function(): 
    print("python is" + " " + f"{cool()}") 

my_function()  # it would print "python is cool!" and now you can use it anywhere in the code, because it is a "global variable"


def why(): 
    t = "why am I doing this...?" 
    u = "I'm so tiered..." 
    print(t + " " + u)  

why() # and it will print "why am I doing this...? I'm so tiered..." becouse you defined t and u inside the function and printed them out at the end, so you don't have to use print() to print it 

# you can use del to delete a variable 
v = "my name is lucifer" # and now we can deleat it 
del v # we deleated it so now it is not usable anymore, and if you try to print it, it will give you an error because it is not defined anymore (value of null) 
v = "I took my meds at 12:03 pm" # reassigned the variable 

