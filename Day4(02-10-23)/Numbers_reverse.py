#To print numbers in reverse
n=int(input())
def fun(n):
    if(n==0):
        return
    print(n)
    fun(n-1)
fun(n)