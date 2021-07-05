def LinearSearch(data,element):
    for i in range(1,len(data)):
        if element==data[i]:
            return i
    else:
        return -1

data=[10,20,30,40,50,60,70,85]
element=int(input("Enter the element which you want to match or search"))

index=LinearSearch(data,element)
if index==-1:
    print("element not found")
else:
    print("element is found",index)