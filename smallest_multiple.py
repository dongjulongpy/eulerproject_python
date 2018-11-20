def gcd(a, b):

    min_n = min(a, b)
    max_n = max(a, b)

    if min_n == 0: return a
    else: return gcd(min_n, max_n%min_n)

def gcm(a, b):
    return (a*b)/gcd(a,b)

smallest = 1

for i in range(1, 20):
    gc = gcm(i, i+1)
    smallest = gcm(gc, smallest)

print(smallest)
