l=[]
n=int(input("enter total no of elements in list:"))
print("enter elements in list:")
for i in range(n):
	l.append(input())
print("list is :",l)
print("after converting list to tuple:",tuple(l))