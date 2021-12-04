#Python – Remove Tuples of Length K

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
K=2

print("original list is: ",str(test_list))

res=[ele for ele in test_list if len(ele)!=K ]

# filter() filters non K length values and returns result
#res = list(filter(lambda x : len(x) != K, test_list))

print(res)