def is_prime(n):
   
    if n <= 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
        
    return True

sum_primes = 0

for i in range(2,2000000):
    
    if is_prime(i):
        sum_primes += i

print(sum_primes)
