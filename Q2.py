#Python program to create a list of tuples from given list having number and its cube in each tuple

def Program(list1):
    res=[(val,pow(val,3)) for val in list1 ]
    return res

def main():
    list = []
    size = int(input("enter number of elements"))
    for j in range(size):
        print("enter list elements: ", j + 1)
        value = int(input())
        list.append(value)
    print("Accepted list is: ", list)
    result=Program(list)
    print("expcted output is: ",result)

if __name__=="__main__":
    main()