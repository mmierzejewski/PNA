# Prime numbers algorithm (by openai)
from datetime import datetime


def pna(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [x for x in range(n + 1) if primes[x]]


m = 200000000
t1 = datetime.now()
print('Start:', t1)
print('Amount of prime numbers in range from 2 to', m, ':', len(pna(m)))
t2 = datetime.now()
at = t2 - t1
print('Amount stop:', t2)
print('Amount time:', at)
print('The highest prime number in that range to', m, 'is', max(pna(m)))
t3 = datetime.now()
tht = t3 - t2
print('The highest stop:', t3)
print('The highest time:', tht)
print('Stop:', t3)
a = t3 - t1
print('Time of counting everything:', a)
