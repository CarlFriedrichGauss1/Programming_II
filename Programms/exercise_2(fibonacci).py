def fibonacci(n):
    if n == 0:
        return []    
        
    elif n == 1:
        return [0]

    fib_sequence = [0,1]

    for i in range(2,n):
        next_term = fib_sequence[-2] + fib_sequence[-1]
        fib_sequence.append(next_term)
    return fib_sequence

print(fibonacci(10))
