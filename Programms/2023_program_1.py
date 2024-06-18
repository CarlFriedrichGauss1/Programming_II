import re
import math


def Python(x):
    product = []
    minimum = []
    for i in range(len(x)):
        prod = 1
        min = math.inf
        for j in range(len(x[i])):
            prod = prod*x[i][j]

            if x[i][j] < min:
                min = x[i][j]
                
        product.append(prod)
        minimum.append(min)
    
    return product , minimum

x = ([1,2,3], [5,6,7])
print(Python(x))
            
            
