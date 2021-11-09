from is_prime import is_prime

def primes_below(n):
    primes = []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    return primes

s = ["a","b","c"]
print(s)
s[0:2] = "f"
print(s)

a = "abc"
print(list(a))
print("".join(a))