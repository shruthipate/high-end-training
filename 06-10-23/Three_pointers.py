def solve(arr):
    for p3 in range(len(arr)-2):
        p1 = p3+1
        p2 = len(arr)-1
        while p1<p2:
            sum = arr[p1] + arr[p2] + arr[p3]
            if sum == target:
                return (arr[p1], arr[p2], arr[p3])
            elif sum < target:
                p1 += 1
            else:
                p2 -= 1
    return False
    
arr = [2,3,4,5,6]
target = 15
result = solve(arr)
print(result)