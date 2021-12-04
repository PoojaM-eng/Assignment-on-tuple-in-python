#Find the size of a Tuple in Python

#using getsizeof() function

import sys

Tuple1=("A",1,"B",2,"C",3)
Tuple2=("Geek1","raju","Geek2","ramu","Geek3","rahu")
Tuple3=((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("size of tuple1: "+str(sys.getsizeof(Tuple1))+" bytes")
print("size of tuple2: "+str(sys.getsizeof(Tuple2))+" bytes")
print("size of tuple3: "+str(sys.getsizeof(Tuple3))+" bytes")


#using __sizeof()__ method
print("size of tuple1: "+str(Tuple1.__sizeof__())+" bytes")
print("size of tuple2: "+str(Tuple2.__sizeof__())+" bytes")
print("size of tuple3: "+str(Tuple3.__sizeof__())+" bytes")