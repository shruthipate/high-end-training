#prime algorithm
def sieveOfEratosthemes(n):
    count_prime=[True]*(n+1)
    p=2
    while(p*p<=n):
        if count_prime[p]:
            for i in range(p*p,n+1,p):
                count_prime[i]=False
        p+=1
    for p in range(2,n+1):
        if count_prime[p]:
            print(p)
n=30
sieveOfEratosthemes(n)
