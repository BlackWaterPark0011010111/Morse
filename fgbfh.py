def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper



@log_function
def say_hello():
    print("Hello, World!")

say_hello()   

