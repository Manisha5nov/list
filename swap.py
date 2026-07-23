a=[1,2,3,5,7,9]
s=min(a)
l=max(a)
i=a.index(s)
j=a.index(l)
a[i],a[j]=a[j],a[i]
print(a)