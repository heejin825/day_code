
def sieve(n):
    primes = [True] * (n+1)                             # 100개의 primes를 만듬듬
    primes[0] = primes[1] = False                       # 0과 1은 False
    
    for i in range(2, int(n**0.5) + 1):                 # 2 부터 
        if primes[i]:
            for j in range(i*i, n+1, i):
               primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]

print(sieve(100)) 


