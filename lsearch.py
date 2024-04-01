def lsearch(list,n,val):
    for i in range(0,n):
        if(list[i]==(val)):
           return i
    return -1
list=[1,45,7,5,2,4,67,8,5,4,3,5,3,3,566,6]
n=len(list)
val=1
res=lsearch(list,n,val)
if res==-1:
    print("value not found")
else:
    print("value of number is at index",res)
