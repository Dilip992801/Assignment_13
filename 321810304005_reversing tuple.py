a,l=(1,2,3,4),[3,2]
j=len(a)-1
print("tuple is:",a)
l=list(a)
for i in range(0,len(a)-1):
	l[i]=a[j]
	j-=1
print("after reversing tuple:",tuple(l))	
	
