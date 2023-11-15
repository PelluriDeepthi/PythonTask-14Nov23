# Write a program to demonstrate working with dictionaries in python
dict = {"Fruit": "Guava", "Vegetable": "Potato"}
print("Dictionary is:", dict)

print("\nFruit is:", dict["Fruit"])

keydict = dict.keys()
print("\nKeys in given dictionary:", keydict)
valdict = dict.values()
print("Values in given dictionary:", valdict)

dict["Juice"] = "Orange"
print("\nUpdated dictionary:", dict)

dict["Vegetable"] = "Cabbage"
print("Updated dictionary value of vegetable is:", dict)