            
def BinarySearch(data,element):
    beg=0
    end=len(data)-1
    while(beg<=end):
         mid=(beg+end)//2
         if (element == data[mid]):
                return mid
         elif (element > data[mid]):
                beg = mid+1
         else:  
                end =mid-1
    else:
        return -1

data=[10,20,30,40,50,60,70,85]
element=int(input("Enter the element which you want to match"))

index=BinarySearch(data,element)
if(index==-1):
    print("Search is not found")
else:
    print("Search is found",index)
            
