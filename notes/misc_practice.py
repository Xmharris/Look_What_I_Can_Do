# notes/misc_practice.py
import time
from functools import wraps

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"{func.__name__} took {t1 - t0:.6f}s")
        return result
    return wrapper

@timeit
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    print("is_prime(97):", is_prime(97))
    print("factorial(6):", factorial(6))
    print("slow_sum(100000):", slow_sum(100000))
