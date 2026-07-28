# conditionals in python 
# there are three to four conditionals, depends if you count while as one of them 
# the main ones are 'if' 'elif' (a combination of else and if) and 'else' 

# there are four basic conditions 
# ==    equal to        the difference between '=' and '==' is that '=' is used to assign a value and '==' is used to compare values 
# !=    not equal to 
# >     greater than 
# <     less than 
# and then there also is 
# >=    greater than or equal 
# <=    less than or equal 

# can be used to make a number guessing game 
secret = 42
guess = int(input("Guess the number: "))

if guess == secret:   # first condition: "if guess (variable) is equal to secret (variable) execute..." 
    print("Correct!") 
elif guess < secret:   # second condition: "else, if guess (variable) is greater than secret (variable) execute..." 
    print("Too low!") 
else:   # "else (if none of the above is true) execute..." 
    print("Too high!") 

# or to check if user is loged in 
is_loged_in = True 
if is_loged_in: 
    print("user is loged in") 
else: 
    print("no one is loged in") 
    print("plaese log in to continue") 

# you can use this for many diferent things 
day = 3

if day == 1:        # if true use this one, if not continue to next elif
  print("Monday")
elif day == 2:      # else, if true use this one, if not continue to next elif or if no if and elif statements are true go to else 
  print("Tuesday")
elif day == 3:      # else, if true use this one, if not continue to next elif or if no if and elif statements are true go to else
  print("Wednesday")
elif day == 4:      # else, if true use this one, if not continue to next elif or if no if and elif statements are true go to else
  print("Thursday")
elif day == 5:      # else, if true use this one, if not continue to next elif or if no if and elif statements are true go to else
  print("Friday")
elif day == 6:      # else, if true use this one, if not continue to next elif or if no if and elif statements are true go to else
  print("Saturday")
else:       # if none of the previous if and elif statements were true, use this one 
  print("Sunday")

# you can also compress these statements into one line like so 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 

# or you can use them like this 
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# or this 
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

# logical operators
# there is 'and' 'or' and 'not' 
# and       returns true if both statements are true 
# or        returns true if one of the statements is true 
# not       reverses the result, returns false if the result is true 

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True") 

if a < b or a > c: 
    print("At least one of the conditions is True") 

if not b > a:
    print("a is NOT greater than b")

# you can combine multiple logical operators in a single expression 
# python evaluates not first, then and, then or 

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!") 

# wehen combining multiple logical operators, use parentheses to make your intentions clear and control the order of evaluation 
temperature = 25
is_raining = False
is_weekend = True
if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

# nested if statements 
# nested if statement is an if statement inside of an if statement 
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# each level of nesting creates a deeper level of decision making 
# the code evaluates from the outermost condition inward 
age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive") 

score = 85
attendance = 90
submitted = True
if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

# you can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read 
# but if you want to be the only one who can read the code then go right ahead 

# sometimes nested if statements can be simplified by using other logical operators like and 
# The choice depends on your logic 

temperature = 25
is_sunny = True
if temperature > 20:        # without and 
  if is_sunny:
    print("Perfect beach weather!")

temperature = 25
is_sunny = True
if temperature > 20:        # with and 
  if is_sunny:
    print("Perfect beach weather!")

score = 92
extra_credit = 5
if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

# the pass statement 
# if statements cannot be empty, but if you for some reason have an if statement with no content, use the pass statement to avoid getting an error 
# the pass statement is a null operation (nothing happens when it executes), It serves as a placeholder 
# why is pass usefull?
# the pass statement is useful in several situations 
# like for example 
# when you're creating code structure but haven't implemented the logic yet 
# when a statement is required syntactically but no action is needed 
# as a placeholder for future code during development 
# in empty functions or classes that you plan to implement later 

# during development, you might want to sketch out your program structure before implementing the details 
# The pass statement allows you to do this without syntax errors 

age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

# a comment is ignored by python, but pass is an actual statement that gets executed (though it does nothing) 
# you need pass where Python expects a statement, not just a comment 

# this would cause an error (empty code block on line 203):
# score = 85
# if score > 90:
#   This is excellent
# This will raise an IndentationError 

# this works correctly with pass:
score = 85
if score > 90:
  pass # This is excellent
print("Score processed")\

value = 50
if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

def calculate_discount(price):
  pass # TODO: Implement discount logic
# Function exists but doesn't do anything yet 
