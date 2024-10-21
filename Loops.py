n = int(input())
l = []
if 1<=n<=20:
    for i in range(0,n):
        l.append(i)
    for i in l:
        print(i**2)
else: 
    raise ValueError("pipu")
