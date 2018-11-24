for a in range(0,333):
    
    for b in range(a+1, a+332):
        c = 1000 - (a+b)

        if a*a + b*b == c*c:
            maxproduct = a*b*c

print(maxproduct)
