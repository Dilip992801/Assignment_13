t = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print("slicing the tuple",t)
s = t[3:5]
print("t[3:5]:",s)
s= t[:6]
print("t[:6]:",s)
s= t[5:]
print("t[5:]:",s)
s= t[:]
print("t[:]:",s)
s = t[-8:-4]
print("t[-8:-4]:",s)
t= tuple("HELLO WORLD")
print("\nnow slicing the tuple",t)
s= t[2:9:2]
print("t[2:9:2]:",s)
s= t[::4]
print("t[::4]:",s) 
s= t[9:2:-4]
print("t[9:2:-4]:",s)