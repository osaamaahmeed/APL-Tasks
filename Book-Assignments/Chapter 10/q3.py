def filter_positive():
    while True:
        number = (yield)
        if number > 0:
            print(f"Positive number: {number}")


co = filter_positive()
next(co)
co.send(-3)
co.send(5)
co.send(0)
# co.send(25)
