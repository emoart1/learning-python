# numbers in python 
# there are three numeric types in python 

a = 1 # a is an integer or an int because it is a whole number without a decimal point  
b = 4.5 # b is a float because it has a decimal point 
c = 8j # c is a complex number because it has a real and imaginary part, where the imaginary part is j 

# you can check the type of a number/variable using the type() function 
print(type(a)) # <class 'int'> 
print(type(b)) # <class 'float'> 
print(type(c)) # <class 'complex'> 

# an integer can be of any length, it is only limited by the memory available
# integers can be positive or negative but they have to be whole numbers 
d = 123456789 
e = -987654321 

# floats or "floating point numbers" are numbers that have one or more decimal points 
# they can also be positive or negative and of any length 
f = 3.14159265359 
g = -2.71 

# they can also be scientific numbers with an "e" to indicate the power of 10
h = 3e2 # 3 * 10^2 = 300
i = -4e3 # -4 * 10^3 = -4000 

# complex numbers are written with a "j" as the imaginary part 
j = 2 + 3j # 2 is the real part and 3j is the imaginary part 

# you can convert between numeric types using the int(), float(), and complex() functions 
k = int(b) # converts the float 4.5 to int 4 by remorving the decimal part 
l = float(a) # converts the int 1 to float 1.0 (adds a decimal point to the number) 
m = complex(a) # converts the int 1 to complex 1 + 0j (adds an imaginary part of 0 becouse it is not specified) 

# to make a ramdom number in python you can use the random module 
import random 
n = random.randint(1, 10) # generates a random integer between 1 and 10 
# or you can use random.random(1, 10) or random.randrange(1, 10) 
print(n) 

n = random.uniform(1, 10) # generates a new random number that is a float between 1 and 10  
print(n)  

o = complex(random.randint(1, 10)) # generates a random complex number 
print(o) 



# there are 7 arithmetic operations in python 
# addition, subtraction, multiplication, division, modulus, exponentiation and floor division 

print(f"12 + 18 = {12 + 18}") 
# adition (I don't have to and will not explain further) 

print(f"d - f = {d - f}") 
# subtraction (again, I don't have to and will not explain further) 

print(f"3 * 927 = {3 * 927}") 
# multiplication (if you don't understand multiplication you shouldn't be learning python) 

p = 15
q = 4
print(f"p / q = {p / q}") 
# devision (I don't think I have to elaborate on this matter) 

print(f"p % q = {p % q}") 
# module output is the remainder after devision 
# two equations I came up with to visualize it -> p / q = 3.75 => p % q = q * 0.75 = [int(15 / 4) * 4 - 15] * -1 
# instead of [] use (), I just used [] so it is more visible 
# let's test is my equation 

def equation_prover(): 
    r = random.randint(1, 100)
    s = random.randint(1, 100)
    while r <= s:
        del s 
        del r 
        r = random.randint(1, 100)
        s = random.randint(1, 100)
    t = (int(r / s) * s - r) * -1 
    if t == r % s: 
        print(f"""\n equation is correct
{r} % {s} = (int({r} / {s}) * {s} - {r}) * -1 = {r % s} \n""") 
    else: 
        print("\n no, the equation is not correct \n") 

equation_prover() 

# and now exponentation 
print(f"{p} ** {q} = {p ** q}") 
# exponentation is just multiplying a numbet by itself multiple times
# an equation to visualize it -> p ** q = (((p * p) * p) * p) [whare "q" is the amount of time it is multiplied] 
# to prove the equation works I will make another equation_prover 

def equation_prover_2():
    r = random.randint(1, 100)
    s = random.randint(1, 10)

    t = 1
    for _ in range(s):
        t *= r

    multiplication = str(r)
    for _ in range(s - 1):
        multiplication = f"({multiplication} * {r})"

    if t == r ** s:
        print(f"""
equation is correct
{r} ** {s} = {multiplication} = {t}
""")
    else:
        print(f"""
no, the equation is not correct
{r} ** {s} = {multiplication} = {t} != {r ** s}
""")

equation_prover_2() 

# floor devision 
# floor devision always rounds down so the number can become an integer 
# another equation -> p // q = int(p / q) 
# to prove the equation works I will make another equation_prover that will be very similar to the first one 

def equation_prover_3(): 
    r = random.randint(1, 100)
    s = random.randint(1, 100)
    while r <= s:
        del s 
        del r 
        r = random.randint(1, 100)
        s = random.randint(1, 100)
    t = int(r / s)
    if t == r // s: 
        print(f"""\n equation is correct
{r} // {s} = int({r} / {s}) = {r // s} \n""") 
    else: 
        print("\n no, the equation is not correct \n") 

equation_prover_3() 

