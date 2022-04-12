def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

        
    
def number_of_groups(n, k):
    # Cnk = n! / ((n - k)! · k!)
    Cnk = factorial(n) / (factorial(n - k) * factorial(k))
    return int(Cnk)


print(number_of_groups(5, 3))  
    
    
