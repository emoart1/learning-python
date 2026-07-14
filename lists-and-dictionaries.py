# lists and dictionaries in python 
# lists are used to store multiple items in a single variable  
# when creating a list seperate the data, text or value with a comma (,) 

alist = [1, 2, 3, 4, 5] # list of integers (numeric) 
ThisList = ["apple", "banana", "cherry", "apple", "cherry", "strawberry"] # a list of sttings, often called a string 
that_list = [True, False, False, True, True, False] # a list of boolean values 

# you can also create a list with mixed data types, but it can be confusing and may lead to errors 
# lists are defined as objects with the data type 'list'
print(type(that_list))   # <class 'list'> 

# you can also make a list with the list() constructor
new_list = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))   # you have to use double parentheses because the list() constructor takes a single argument
print(type(new_list))   # <class 'list'> 

# there are four collection data types in python (lists, tuples, sets and dictionaries) 
# and four properties that they have in common (ordered, changeable, duplicates, indexed) 

#               ordered		changeable		duplicates      	indexed 
# lists         yes		    yes			    yes			        yes 
# tuples        yes		    no		    	yes			        yes 
# sets          no		    kinda...	    no	        	    no 
# dictionaries  yes		    yes			    keys-no values-yes	keys-yes values-no 

# lists are made by using square brackets [] 
# they can be ordered, are changeable, allow duplicate values and can be indexed
# indexing is just searching through the list, starting at 0, so the first item in a list is at index 0
print(alist) 
print(alist[0]) # it will print 1
print(new_list[6]) # it will print 7
print(ThisList[3:6]) # it will print ['apple', 'cherry', 'strawberry'] because it is slicing the list from index 3 to index 6, but not including index 6 
# can also be done with negative values but starting from -1 

# you can also use negative indexing to start from the end of the list, so the last item in a list is at index -1
print(new_list[-1]) # it will print 10

# lists are changeable, meaning that you can change, add, and remove items in a list after it has been created
# you can change the value of a specific item by referring to its index number
alist[0] = 10 # changing the first item in the list to 10

# they can also contain duplicate values, meaning that you can have items with the same value in a list 

# tuples are made by using parentheses ()
# tuples are the same as lists but they are immutable, meaning that you cannot change, add, or remove items in a tuple after it has been created
atuple = (1, 2, 2, 3, 6, 4, 5) # tuple of integers
print(atuple) 
print(type(atuple)) # <class 'tuple'>
print(atuple[2]) # it will print 2 because it is the third item in the tuple, and indexing starts at 0 
print(atuple[4]) 
# it will print 6 because it is the fifth item in the tuple and because tuples don't have to be ordered, and indexing starts at 0 

# sets are made by using curly brackets {}
# sets are the opposite of lists beacouse they are unordered, unchangeable, unique (so no duplicates), and unindexable 
# unordered means that the items in a set do not have a defined order, meaning that you cannot be sure in which order the items will appear 
set1 = {"apple", "banana", "cherry", "strawberry"} # set of strings 
print(set1) 
print(type(set1)) # <class 'set'> 
# unchangeable means that you can't change the items in a set, but you can add or remove items 
added_set = set1.add("orange") # adding an item to the set 
print(set1) 
removed_set = set1.remove("banana") # removing an item from the set 
print(set1) 
# unique means that you cannot have duplicate items in a set, so if you try to add a duplicate item it will not be added 
added_set = set1.add("apple") # trying to add a duplicate item to the set
print(set1) # output will be the same as before because the duplicate item was not added 
# unindexable means that you cannot access items in a set by their index number, so you cannot use indexing to access items in a set 
# you can bypass this by using a for loop to iterate through the set and access the items that way 
for x in set1: 
    print(x) 
# you can also use the in keyword to check if an item is in a set
if "apple" in set1: 
    print("Yes, apple is in the set") 
# you can also bypass the unindexable property of sets by converting the set to a list and then accessing the items in the list by their index number
set_to_list = list(set1)
print(set_to_list[1]) # it will print the second item in the list

# dictionaries are made by using curly brackets {} but unlike sets 
# they are ordered, changeable 
# they allow duplicate values but not duplicate keys and they are indexed by their keys instead of their index number 
dictionary13 = { 1: "apple", 2: "banana", 3: "cherry", 4: "strawberry" 
} 
full_to_null = { "1": "full" , 
"0": "empty" , 
"null1": "nothing" , 
"null2": "undefined" 
} 
print(dictionary13)
print(type(dictionary13)) # <class 'dict'> 
# (dict is short for dictionary) 
print(dictionary13[1]) # it will print apple because it is the value associated with the key "1" 
print(full_to_null["null1"]) # it will print the word "nothing" because it is the value associated with the key "null1" 
added_dict = dictionary13[5] = "orange" # adding a new key-value pair to the dictionary 
print(dictionary13) 
added_dict = full_to_null["2"] = "error" # adding a new key-value pair to the dictionary 
added_dict = full_to_null["null3"] = "undefined" # adding a new key-value pair to the dictionary that is a duplicate of null2 but with a different key 
print(full_to_null) 

# you can use insert() to add stuff to a list 
alist.insert(2, 99) # inserting the value 99 at index 2 in the list "alist" 
print(alist) 
# insert only works on lists 
# you can use pop() to remove stuff from a list or dictionary (easy to remember) 
full_to_null.pop("2") # removing 2 from the dictionary "full_to_null" 
full_to_null = {"2": "error", **full_to_null} # moving key "2" with value "error" to first position
print(full_to_null) 

# you can use extend() to add stuff to a list 
# you can add lists, tuples, sets, and dictionaries to a list using extend() 
alist.extend(new_list) # adding the values from "new_list" to the end of the list "alist" 
print(alist) 
