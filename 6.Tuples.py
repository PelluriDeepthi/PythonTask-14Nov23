# Write a program to demonstrate working with tuples in python
emptytup = ()
print("Empty tuple is:", emptytup)

tup = (1, 3, 5, 7, 9)
print("\nTuple:", tup)
print("Length of the tuple is:", len(tup))

acctup = tup[1:5]
print("\nAccessing elements from tuple:", acctup)

mixtup = (2, 3, "Six", 7.9)
print("\nMixed Tuple is:", mixtup)
print("Length of the tuple is:", len(mixtup))

nestedtup = (6, 10, (43, 69, 20))
print("\nNested tuple is:", nestedtup)
print("Length of the tuple is:", len(nestedtup))