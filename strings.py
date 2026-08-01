# strings in Python
# strings are surrounded by either single or double quotation marks 
print("Hello") 
print('I\'m sad....') 
print("can \"you\" help me...?")
# to use single quote inside a string that is surrounded by single quotes, you can use backslash (\) to escape it, the same goes for double quotes 

# you can also use triple quotes for multi-line strings
print("""This is a multi-line string made with triple double quotes.
It spans multiple lines.""") 

print('''This is also a multi-line string made with triple single quotes.
It can also span multiple lines.''')

# you can use varaibles to store strings
name = "Gabriel" 
print(name) # and then you can use the variable to print the string that you assigned to it 

# strings are arrays (yes, you can access individual characters in a string using an index starting from 0)
print(name[0])  # prints the first character of the string 
print(name[1])  # prints the second character of the string 

# you can also use negative indexing to access characters from the end of the string
print(name[-1]) # prints the last character of the string 
print(name[-2]) # prints the second to last character of the string 

# you can use slicing to get a substring from a string
print(name[0:3]) # prints the first three characters of the string 
print(name[2:4]) # prints the third to fourth characters of the string 

# you can also use slicing with negative indexing 
print(name[-4:-1]) # prints the fourth to last to second to last characters of the string 

# whaen slicing you don't have to specify the start or end index, if you don't specify the start index it will start from the beginning of the string, if you don't specify the end index it will go until the end of the string
print(name[:3]) # prints the first three characters of the string 
print(name[2:]) # prints the third character to the end of the string 

# loops can be used to iterate through the characters in a string
for x in name:
    print(x) # prints each character in the string on a new line 

# you can use the len() function to get the length of a string
print(len(name)) # prints the length of the string 

# you can use the "in" keyword to check if a substring is present in a string
print("Gab" in name) # prints True if the substring "Gab" is present in the string 
print("John" in name) # prints False if the substring "John" is not present in the string 
text = "why am I subjected to this torment...? why do I have to be tortured by this painful existence...? why can't I just be happy...? why can't my soul be free.. free as the wind that blows through the trees, free as the birds that soar through the sky, free as the waves that crash against the shore... why can't I just be free...?" 
print("torment" in text) # prints True if the substring "torment" is present in the string 

# you can use the "not in" keyword to check if a substring is not present in a string
print("Gab" not in name) # prints False if the substring "Gab" is present in the string 
print("John" not in text) # prints True if the substring "John" is not present in the string 

# you can use the upper() method to convert a string to uppercase
print(name.upper()) # prints the string in uppercase 

# you can use the lower() method to convert a string to lowercase
print(text.lower()) # prints the string in lowercase 

# you can use the strip() method to remove any whitespace from the beginning or end of a string 
print(text.strip()) # prints the string with any leading or trailing whitespace removed 

# you can use the replace() method to replace a substring with another substring in a string
john = "john is not happy with his life, he is tormented by his existence and he is suffering from the pain of living in a world that doesn't care about him" 
print(john.replace("tormented", "suffering")) # prints the string with the substring "tormented" replaced with "suffering" 

# you can use the split() method to split a string into a list of substrings based on a specified delimiter
print(text.split(" ")) # prints a list of substrings split by spaces 

# you can use if statements to check if a string is in uppercase or lowercase or if something is in the string or not 
if name.isupper():
    print("The string is in uppercase") 

if name.islower():
    print("The string is in lowercase") 

if "Gab" in name:
    print("The substring 'Gab' is present in the string") 

# you con combine strings using the + operator
first_name = "Gabriel"
last_name = "Martinez"
full_name = first_name + " " + last_name
print(full_name) # prints "Gabriel Martinez"
print("{} {}".format(first_name, last_name))

# you can not combine strings with numbers using the + operator, you will get a TypeError
# you can use formatting to combine strings and numbers using the format() method
age = 20
print("I am {} years old".format(age)) # prints "I am 20 years old" 

print(f"I am not {age} years old") # prints "I am not 20 years old" using f-strings (formatted string literals) 

# placeholders can be used in strings to insert values using the format() method 
stuff = "I am {} years old and my name is {}".format(age, full_name)
print(stuff) # prints "I am 20 years old and my name is Gabriel Martinez" 

print(f"12 * 69 = {12 * 69}") # prints "12 * 69 = 828" using f-strings (formatted string literals) 

# escape characters can be used to insert special characters in strings, such as newlines (\n), tabs (\t), and backslashes (\\)
# there are many escape characters in Python, you can find them on the internet 
print("This is a string with a newline character\nThis is the second line") # prints a string with a newline character 

# string methods can be used to manipulate strings, such as upper(), lower(), strip(), replace(), split(), and many more. You can find a list of string methods in the Python documentation. 

