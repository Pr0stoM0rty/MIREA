s=0
a = input().split(' ')
for i in range(1,len(a)-1):
    if int(a[i])-int(a[i-1])>0 and int(a[i])-int(a[i+1])>0:
        s+=1
print(s)