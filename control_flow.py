import math

meaning = 42
print('')

if meaning > 10:
    print('Right On!')
else:
    print('Not today!')

# Ternary operators in python

print('Right on!') if meaning > 42 else print('Not today !')

# String Data types

#literal assignment
first = 'Subho' 
last = "Yadav"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

#constructor function

icecream = str("twin butterscotch and chocolate")
print(type(icecream))
print(type(icecream) == str)
print(isinstance(icecream, str))

# concatenation
fullname = first + last
fullname += "!"
print(fullname)

#casting a number to a string
decade = str(1980)
# decade = 1980
print(type(decade))
print(decade)

statement = "I like punjabi sad songs from the decade " + decade + "s."
print(statement)

# multiline string
multiline = """
Hello, my name is Subho Yadav and 
       I am a software Engineer by profession
                I work at a Gurugram base startup company named
Collab Circle pvt. ltd.
"""
# String methods
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("Collab Circle pvt. ltd.", "GIDE.AI"))



multiline += "          "
multiline = "              " + multiline
print(len(multiline))

print( len( multiline.strip() ) )
print( len( multiline.lstrip() ) )
print( len( multiline.rstrip() ) )


title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheese Cake".ljust(16, ".") + "$4".rjust(4))

#String index value
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some string methods that return boolean data

# Methods are case sensitive
print(first.startswith("s")) 
print(first.endswith("o"))

# Numeric data types

price = 100
best_price = int(80)
print(type(best_price))
print(type(best_price) == str)
print(isinstance(best_price, str))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type 
cmplx = 3+2j
print(type(cmplx))
print(cmplx.real)
print(cmplx.imag)


print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa, 1)) # rounds to the nearest 1 decimal place

# math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting string to an integer
zipcode = "743136"
zipcode = int(zipcode)
print(type(zipcode))

# Typecast errors
# zip_val = int("Kolkata")


