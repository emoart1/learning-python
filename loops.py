# loops in python 
# there are two loops in python for and while 

# while loops are loops that repeat until the condition is true or util the condition is met 
a = 0 
while a <= 10 :  
    if a == 10 :
        print("a is now 10 \n") 
        break 
    else : 
        print(a) 
        a += 1 

# for loops 
# for loops are used when you need to repeat an action multiple times 
c = "python"
for b in c:   # with this you are saing "for every item in this collection/list, do this" where 'c' is the collection/list and 'b' is where the value is stored 
    print(b) # this will print every letter in "python" because it takes the string in 'c' and makes it into a list in witch every letter is it's own value 
    if b == "n" : 
        print("\n") 
# but because 'b' can only store one value at a time, it changes with each loop 
d = {"apple", "brush", "thing", "stuff", "thing2", "code"} 
for e in d:   # every time the loop runs it looks at the next item in the list 'd' and puts that value into 'e' 
    print(e)   # and this prints the value of 'e' every time 
    print("\n") 
# this is usefull when you want to for example, list files in a directory or smething like that 
filesindirectory = ["1.txt", "random.txt", "project_final_V12.3.6.md", "python_installer.exe", "python_fixer.sh", "copy_fail.py", "systemvolume.dat", "dirtifrag.git"] 
for file in filesindirectory: 
    print(file) 
# just make the 'filesindirectory' take the names in the curent directory and you almost have the "ls" command from linux 
