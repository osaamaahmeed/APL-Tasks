numbers = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = list(filter((lambda x: x%2 != 0),numbers))
print(odd_numbers)

square_numbers = list(map(lambda x: x**2, odd_numbers))
print(square_numbers)

square_odd_numbers = list(map(lambda x: x**2, filter(lambda x: x%2 != 0, numbers)))
print(square_odd_numbers)