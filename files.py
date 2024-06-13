# r => Read
# a => Append
# w => Write
# x => Create

import os

f = open('files/names.txt', "rt") # open the file in read(r) mode and the file is a text file

# print(f.read()) # reads the entire file 

# print(f.read(4)) # reads the first 4 characters of the file

# print(f.readline()) # reads one line from the file

# using a loop to read a file concisely
for line in f:
    print(line)

f.close()

# If the file we want to read does not exists then we throw an error

try:
    f = open("random_names.txt", "rt")
    print(f.read())
except:
    print("The file doies not exist")
finally:
    f.close()

# Append
f = open("files/names.txt", "at")
f.write("\nVirendra")
f.close()

f = open("files/names.txt", "rt")
print(f.read())
f.close()

# Write (Overwrite)
f = open("files/context.txt", "wt")
f.write("I deleted all of the context in the file.")
f.close()

f = open("files/context.txt", "rt")
print(f.read())
f.close()


# Creating a file: does not throw any error if the file already exists

f = open("files/new_file.txt", "wt")
f.close()

# The following method of creating a file throws an error if the file already exists

if not os.path.exists("files/another_new_file.txt"):
    f = open("files/another_new_file.txt", "xt")
    f.close()

#  File operations with implicit error handling

with open('files/more_names.txt') as f:
    content = f.read()
    f.close()

with open('files/names.txt', 'wt') as f:
    f.write(content)
    f.close()

