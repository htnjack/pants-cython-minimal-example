import cython

def say_hello_to(name):
    if not cython.compiled:
        print("NOT COMPILED")
    print("Hello %s!" % name)