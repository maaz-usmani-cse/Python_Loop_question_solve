a="maaz"
b=a[::-1]
print(b)



a="maaz"
for i in range(len(a)-1,-1,-1):
    print(a[i],end=' ')


a=[20,30,50]
d=[]
for i in range(len(a)-1,-1,-1):
     d.append(a[i])
print(d)