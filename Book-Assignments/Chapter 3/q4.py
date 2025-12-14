def make_adder(n):
    def adder(x):
        return x+n
    return adder

add_five = make_adder(5)
print(add_five(10))