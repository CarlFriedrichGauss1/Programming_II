import math 

def pythagorean_triples(p):
    triples = []
    for a in range(p):
        for b in range(a , p-a):
            c = math.sqrt(a**2 + b**2)
            if a + b + c <= p and a > 0 and b > 0 and c > 0 and c.is_integer():
                triples.append((a,b,c))

    return triples

print(pythagorean_triples(100))