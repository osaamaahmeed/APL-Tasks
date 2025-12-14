def my_reduce(func, list, initial=None):
    if initial is not None:
        result = initial
        items_to_check = list
    else:
        result = list[0]
        items_to_check = list[1:]

    for item in items_to_check:
        result = func(result, item)

    return result

numbers = [1,2,3,4,5]
print(my_reduce(lambda x,y: x*y, numbers))