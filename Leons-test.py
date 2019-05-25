primes=[]
for n in range(2,1000):
    for p in primes:
        if not n%p:
            break
    else:
        primes.append(n)
print(primes)