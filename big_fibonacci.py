def big_fibonacci(digits):
    n = 0
    fibonacci = 0
    prev = 1
    curr = 1
    while n < digits:
        fibonacci = curr + prev
        prev = curr
        curr = fibonacci
        n = len(str(fibonacci))
    return fibonacci