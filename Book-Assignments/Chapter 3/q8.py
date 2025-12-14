def log_cal(func):
    def wrapper(*args, **kwargs):
        print(f"Log: Starting execuxtio of {func.__name__}")
        result = func(*args, **kwargs)
        print("Log: Finished execution")
        return result
    return wrapper

@log_cal
def add_numbers(a,b):
    print(f"Calculating {a} + {b}")
    return a+b

answer = add_numbers(5,10)
