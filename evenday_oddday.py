lst=[]
num=int(input("enter the no of days"))
for e in range(num):
    x=int(input("enter the days"))
    lst.append(x)
count=0
count1=0
for i in range(len(lst)):
    if lst[i]%2==0:
         count+=1     
    else:
        count1+=1
print(" total count of even no:",count)
print("total count of odd no:",count1)       
