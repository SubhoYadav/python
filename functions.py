def hello_world():
    print("Hello World!")

hello_world()

def sum(num1 = 0, num2 = 0):
    if (type(num1) is not int or type(num2) != int):
        return 
    return num1 + num2

print(sum(5,"2"))
print(sum())

# When the number of arguments are unknown
def multiple_args(*args):
    print(args)
    print(type(args)) # Tuple

multiple_args(1,2,3,4,5)

# Keyword arguments or **kwargs

def multiple_named_args(**kwargs):
    print(kwargs)
    print(type(kwargs)) # dictionary

multiple_named_args(first = "Subho", last = "Yadav")


# scopes

count = 5
def usual_function(name):
    color = "Red"

    #using the count variable from the global scope
    global count
    count += 5
    count1 = 10
    print("count from the global scope " + str(count))
    print("Colour is: " + color)
    def greetings(name):
        nonlocal count1
        count1 += 10
        print("Count 1", count1)
        color = "sfron"
        print(color)
        print("Greetings from python: " + name)

    greetings(name)

usual_function("Subho Yadav")

"""
Difference between global and nonlocal

"global"
The global keyword is used to declare that a variable inside a function is global. 
This means that any assignment to this variable within the function will affect the variable with 
the same name in the global scope (i.e., outside all functions).

"nonlocal"
The nonlocal keyword is used to declare that a variable inside 
a nested function (i.e., an inner function) is not local to the inner function but rather 
belongs to the nearest enclosing scope that is not global.This is typically used in closures.

"""

# closures 

"""
A function can have access to the scope of its parent function, when the function returns
"""

def parent_function(name):
    coins = 3
    def play_again():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(name + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print(name + " has " + str(coins) + " coin left.")
        else:
            print(name + " has no coins left")
    return play_again

subho = parent_function("Subho")
puja = parent_function("Puja")

subho()
subho()
subho()
subho()

puja()
