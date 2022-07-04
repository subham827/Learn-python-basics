#user defined function
def greet():
    print('Good morning')
greet()

def average(a,b):
    return (a+b)/2

print(average(2,3))

#Recurive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
