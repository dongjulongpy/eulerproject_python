import math 

def maxPrimeFactors (n): 
    maxPrime = -1
    
    while n % 2 == 0: 
        maxPrime = 2
        n /= 2     # equivalent to n /= 2 
          
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 

    if n > 2: 
        maxPrime = n 
    return int(maxPrime)
  
print(maxPrimeFactors(600851475143))
