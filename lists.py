# Lists areone of 4 collection data types in python
users = ['Subho', 'Dave', 'Sara']
empty_list = []

print("Subho" in users)
print("Subho" in empty_list)

print(users[0])
print(users[-1])
print(users[-2])
print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))

users.append("elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

users += "SE" # inserts each character in the list from the string "SE"
print(users)

users.insert(0, "BOB")
print(users)

users[2:2] = ["Yadav", "Software"] # Only inserts values
print(users)

users[2:4] = ["My", "Name"] #replaces values from the previous list
print(users)


users.remove("BOB")
print(users)

print(users.pop())
print(users)

del users[4]
print(users)

# users.clear()
# print(users)

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

# Integer lists
nums = [4, 42, 78, 1, 5]
nums.reverse()

print(nums)
nums.sort()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# sorting without modifying the original lsit

# using global sorted function
print(sorted(nums, reverse=True))
print(nums)

# making copies of the list
nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print("")

my_nums.sort(reverse=True)
print(my_nums)
print(my_copy)
print(nums_copy)

print(type(my_copy))
print(list(["Aman", 24, False]))

# Tuples
# They are kind of immutable lists
tupleX = tuple((1, "Subho", True))
my_tuple = ("Yadav", False, "SE") # packing a tuple
print(tupleX)
print(type(my_tuple))

print("Lets see if the list access annotations work with tuples or not\n")
print(tupleX[0:2])
print("Yes it works")

# In order to add/remove something, we need to convert the tuple into a list

mutable_list = list(my_tuple)
# mutable_list.append("Dave Gray")
mutable_list.extend(["Dave Gray", 1, 1,1,1,1,1])

new_tuple = tuple(mutable_list)
print(new_tuple)

# Unpacking the tuples
(one, two, *rest) = new_tuple
print(one)
print(two)
print(rest)

print("")
(one, *two, rest) = new_tuple
print(one)
print(two)
print(rest)

print("")
print(new_tuple.count(1))