#Python – All pair combinations of 2 tuples

test_tuple1=(4,5)
test_tuple2=(7,8)

print("original tuple 1 is: ",str(test_tuple1))
print("original tuple 2 is: ",str(test_tuple2))

res=[(a,b) for a in test_tuple1 for b in test_tuple2]
res=res+[(a,b) for a in test_tuple2 for b in test_tuple1]
print(res)