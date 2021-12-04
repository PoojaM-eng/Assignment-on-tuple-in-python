#Python program to sort a list of tuples by second Item

def Tuple_Sort(tup):

    return sorted(tup, key=lambda x:x[1])

# Driver Code
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

print(Tuple_Sort(tup))