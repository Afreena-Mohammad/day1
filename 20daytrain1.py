a=int(input())
b=list(map(int,input().split(" ")))
k=[]
s=[]
e=[]
for i in range(a):
    d=int(input())
    if(d>=b[0] and d<=b[1]): # or if(d>=min(b) and d<=max(b))
        k.append(d)
    else:
        continue
for i in k:
    if i%2==0:
        s.append(i)
for i in k:
    for j in range(0,max(s)):
        if(2**j==i):
            e.append(i)
print(s)
print(e)