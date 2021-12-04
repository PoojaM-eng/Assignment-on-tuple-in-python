#Python – Flatten tuple of List to tuple

test_tuple=([5, 6], [6, 7, 8, 9], [3])


# printing original tuple
print("The original tuple : " + str(test_tuple))

res=tuple(sum(test_tuple,[]))

# printing result
print("The flattened tuple : " + str(res))