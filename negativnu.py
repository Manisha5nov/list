a=[1,2,3,5,7,9,-8,-6,-4,-1,-3]
count=0
for i in a:
    if i<0:
        count+=1
        print(count,i)
    if i>0:
        count+=1
        print(count,i)
        
