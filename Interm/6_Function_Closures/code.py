def outer_func():
    def inner_func():
        print("Hello inside!")

    print("Hello outside!")
    inner_func()


outer_func()
# inner_func()


def mug(stuff):
    def inside():
        print(f"Yummy {stuff}")

    inside()


mug("Coffee")
