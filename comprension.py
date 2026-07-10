n=[x for x in range(1,6)]
print(n)

n=[x for x in range(8) if x%2==0]
print(n)

a=[1,2,6,5,8]
b=[]
for i in a:
    b.append(i)
print(b)

b=[i for i in a]
print(b)

f=['mango','apple','banana','orenge']
g=[i for i in f if "a" in i]
print(g)

#condition
new=[i for i in f if i!="apple"]
print(new)

nu=[i for i in range(10)]
print(nu)
nu =[i for i in range(10) if i<5]
print(nu)

nu=[i for i in range(10) if i%2==0]
print(nu)

o=[i.upper() for i in f]
print(o)

