# functions in python 
# functions run only when called 
# functions can return data as a result 
# functions help avoid repetition of code 

# in python you use def to define a function followed by parentheses like so 
def first_function(): 
    print("it's interesting and usefull") 

# I have created a function called first_function if called it will print "it's interesting and usefull" 
# to call it I have to type the name of my function followed by parentheses
first_function() 

# function names follow the same rules as variable names in python 
# a function name must start with a letter or underscore 
# a function name can only contain letters, numbers, and underscores 
# function names are case-sensitive (myFunction and myfunction are different) 

# functions are very usefull for repetitive code 
# besicaly functions make repetitive code into reusable code 
# example, you are in physics calss and need to convert kelvin to celsius abunch of times 
# so you make two functions 
def ToCelsius(kelvin): 
    return(kelvin - 273.15) 

def ToKelvin(celsius): 
    return(celsius + 273.15)

# and then you can use them as many times as you want (if you dont deleat them) 

print(ToKelvin(100)) 
print(ToCelsius(300))
