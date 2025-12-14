import functools
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)

@functools.lru_cache(maxsize=None)
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

NormalFib = time.time()
print("Normal Fib(10): ", fib(10))
print(f"Time Taken {time.time()-NormalFib:.5f}")

FastFib = time.time()
print("Normal Fib(10): ", fib_fast(10))
print(f"Time Taken {time.time()-FastFib:.5f}")

