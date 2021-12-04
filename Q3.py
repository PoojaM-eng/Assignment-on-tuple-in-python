#Python – Adding Tuple to List and vice – versa

list1=[1,5,7]

print("original list is: ",str(list1))

tup1=(10,9)

# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)
list1+=tup1

# Adding Tuple to List and vice - versa
# Using tuple(), data type conversion [tuple + list]
res=tuple(list(tup1)+list1)

print("The container after addition : ",res)
print("The container after addition : " + str(list1))