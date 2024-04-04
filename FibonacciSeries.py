#Generic Method
def fibonacci(n):
    a,b = 0,1
    if n<0:
        print("Incorrect input")
    elif n == 0:
        return a
    else:
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
        return b
print(fibonacci(5))

