l=list(map(int,input().split()))
target=int(input())
i=0
j=0
cur_sum=l[0]
while j<len(l)-1:
    if cur_sum==target:
        print(i,j,cur_sum)
        break
    elif cur_sum>target:
        cur_sum-=l[i]
        i+=1
    else:
        j+=1
        cur_sum+=l[j]

        