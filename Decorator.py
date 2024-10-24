def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@my_decorator
def say_name():
    print("My name is Rafin")

say_name()