import time

start = time.time()

a, b = 0, 1

total = 0

while b < 4000000:
    
    a, b = b, a+b
    
    if b % 2 == 0:
        total += b

print(sum)
end = time.time()
timer = end - start

print(total)
print("Time : ", timer)
    

    
    

    
