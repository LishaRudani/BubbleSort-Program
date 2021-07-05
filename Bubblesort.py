data=[41,3,36,78,29,54,11]

print(data)

for i in range(len(data)):
    for j in range(len(data)-1):
        if(data[j]>data[j+1]):
            data[j],data[j+1]=data[j+1],data[j]
print("============================")
print(data)
