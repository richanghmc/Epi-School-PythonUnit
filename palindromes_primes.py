from is_prime import is_prime

def palindromes_primes():
    for i in range(10000,100000):
        if is_prime(i):
            if is_palindrome(i):
                print(i)

def is_palindrome(n):
    stringTemp = str(n)
    middle = len(stringTemp) // 2
    stack = []
    for i in range(middle):
        stack.append(stringTemp[i])
    if len(stringTemp) % 2 == 1:
        middle += 1
    for j in range(middle,len(stringTemp)):
        if stack.pop() != stringTemp[j]:
            return False
    return True
