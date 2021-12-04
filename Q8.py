#Python – Order Tuples by List

# initializing list
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing order list
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

temp=dict(test_list)

res=[(key,temp[key]) for key in ord_list]
print(res)