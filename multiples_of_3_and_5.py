multiples_3 = list(range(0, 1000, 3))
multiples_5 = list(range(0, 1000, 5))
multiples_15 = list(range(0, 1000, 15))

print("Problem Result: ", sum(multiples_3) + sum(multiples_5) - sum(multiples_15))
