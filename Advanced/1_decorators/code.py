# Inner Functions
# ==================

# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     inner_func()


# outer_func("Hello")

# Function Closures
# ==================


# def outer_func(msg):
#     message = msg

#     def inner_func(newmsg):
#         print(message + " " + newmsg)

#     return inner_func


# new_func = outer_func("Hello")
# new_func("there")


# Decorator Functions
# ==================


# Decorator 1


def my_decorator(func):
    def wrapper():
        print("Something is happeneing before the function is called")
        func()
        print("Something is happeneing after the function is called")

    return wrapper


# @my_decorator
# def say_hello():
#     print("Helllooo!")


# say_hello = my_decorator(say_hello)
# say_hello()


# Decorator 2

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()

#     return wrapper_do_twice


# @do_twice
# def say_hello():
#     print("Hello!")


# say_hello()

# Decorator 3


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet(name):
    print("Creating Greeting")
    print(f"Hi {name}")


greet("ZZZ")


# Creating Greeting
# Hi ZZZ
# Creating Greeting
# Hi ZZZ
