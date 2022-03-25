"""
Create a function that takes an integer argument and returns a list of prime numbers found in the decimal representation of that number (not factors).

For example, extract_primes(1717) returns [7, 7, 17, 17, 71].

The list should be in ascending order. If a prime number appears more than once, every occurrence should be listed. 
If no prime numbers are found, return an empty list.
"""

def isPrime(n, i = 2):
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return isPrime(n, i + 1)

def extract_primes(n):
    n, res = str(n), []
    c = ''
    for i in range(len(n)):
        if n[i] != '0':
            c += n[i]
        else:
            continue
        if isPrime(int(c)):
            res.append(int(c))
        for j in range(i+1, len(n)):
            c += n[j]
            if isPrime(int(c)):
                res.append(int(c))
        c = ''
    return sorted(res)

print(extract_primes(10234))
