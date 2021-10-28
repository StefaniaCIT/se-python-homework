"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""
def logout(func):
    def inner(*args):
        output = func(*args)
        file = open("output12.data", "w")
        file.write(str(output))
        file.close()
        file = open("output12.data", "r")
        print(file.read())
    return inner


@logout
def f(x):
    print(x)

f(3)