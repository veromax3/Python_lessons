def our_format(func):
    def decorator(*args):
        for arg in args:
            print(f"{arg} +", end = " ")
        print("\b\b=", end = " ")

        func(*args)
    return decorator

@our_format
def sum(a, b):
    print(a + b)

@our_format
def sum4(a, b, c, d):
    print(a + b + c + d)

sum(4, 6)
sum4(4, 2, 1, 9)