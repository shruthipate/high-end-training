l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            count=count+1
print(count)