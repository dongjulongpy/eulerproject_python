l = range(101)

sum_of_squares = sum(x**2 for x in l)
square_of_sum = sum(x for x in l)**2

print(square_of_sum - sum_of_squares)
