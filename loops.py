# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# A pretty strange thing bin python, the statements in else gets executed when the condition in the while loop fails

names = ["Dave", "Sara", "John"]

for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for name in names:
    if (name == "Sara"):
        break
    print(name)

for name in names:
    if (name == "Sara"):
        continue
    print(name)

# for x in range(4):
#     print(x)

for x in range(2,4):
    print(x)

# starts at 5 and goes until 101 incrementing by 5 each time
for x in range(5,101,5):
    print(x)
else:
    print("Glad that\'s over")

names = ["Dave", "Sara", "John"]
actions = ["eats", "sleeps", "codes"]

# Nested loops
for name in names:
    for action in actions:
        print(name + " " + action)

for action in actions:
    for name in names:
        print(name + " " + action)