def factorial(x):
    if x > 1:
        return x * factorial(x - 1)
    else:
        return 1
    
print(lambda x: x * factorial(x))