
print(dir())
print()
# print(dir(__builtins__))
global x
global y
x = 22
y = "Ana"


def f():
    x = 40
    print(x)
    print(globals().get('x'))
    print(y)


f()
