def palindromic(number):
    return int(str(number)[::-1]) == c

maxnumber = 0

for i in range(999,99,-1):
    for j in range(i,99,-1):
        if palindromic(str(i*j)) and i*j > maxnumber:
            maxnumber = i*j
            
print("The Max: ", maxnumber)
