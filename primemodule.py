def is_prime(n):
    if n < 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5), 2):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    print(get_primes(n))

def get_primes(n):
    lst = []
    for i in range(1, n-1):
        if is_prime(i):
            lst.append(i)
    return lst
