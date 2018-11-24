def is_prime(n):
   
    if n == 1: return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
        
    return True

prime_numbers, a = list(), 2

while True:
    
    if is_prime(a):
        prime_numbers.append(a)

    a += 1

    if len(prime_numbers) == 10001:
        break

print(prime_numbers[-1])
