
#Decorator used to add external functionality in the predefined function

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

# it can be accessed by using annotation of that function and can be accessed 
@my_decorator
def greet():
    print("Hello!")


greet()

# Decorator example code snippet

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        result = func(*args, **kwargs)
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))

# by this we can use decorator to add the multiple functionlity in the predefine function 
# in multiple function 