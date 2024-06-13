band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="page", guitar="plant")
print(band)
print(band2)

print(type(band))
print(len(band))

# Access elemenets in a dictionary
print(band['guitar'])
print(band.get("vocals"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# type casting into string
print(type(list(band.items())))

# verify if aq key exists
print("guitar" in band)
print("triangle" in band)

# change values in the dictionary
band["vocals"] = "coverdale"
band.update({"base": "JPJ"})
print(band)

print(band.pop("base")) # returns the value for the key that has been removed
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # returns a tuple of the removed key/value pair what was last added
print(band)

# delete and clear
band["drums"] = "Bonham"
print(band)

del band["drums"]
print(band)

band2.clear()
print(band2)

del band2
# print(band2)

band2 = band # creates a reference
print("Bad copy")
print(band)
print(band2)
band2["drums"] = "Bonham"

print(band)
print(band2)

# Nested dictionaries

member1 = {
    "name": "plant",
    "instrument": "Vocals"
}

member2 = {
    "name": "page",
    "instrument": "Guitar"
}

band4 = {
    "member1": member1,
    "member2": member2
}

print(band4["member2"]["instrument"])

#sets
set1 = {1,2,3,4}
set2 = set({1,2,3,4})
print(set1)
print(set2)

set1 = {1,2,2,3}
print(set1)

#True is a dupe of 1 and False is a dupe of 0
set1 = {1, True, 2, 3, False, 0}
print(set1)

# you cannot access an element in the set using its index or key as was the case for lists and tuples

# Add element to a set
set1.add(8)

# Add another set to an existing set
set3 = {5,6,7}
set1.update(set3)
# you can pass lists, tuples and distionaries to the update function

print(set1)

print("")

one = {1,2,3}
two = {2,3,4}

print(one.union(two)) # do not changes the set "one"
print(one)

# following methods changes the set "one"
one.intersection_update(two) # keeps only the duplcates
print(one)

one.symmetric_difference_update(two) #keeps everything except the duplicates
print(one)