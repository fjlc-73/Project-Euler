"""
20 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isprime(x):
    prime = True
    y = 2
    if x!=2:
        while prime and y<=round(x/2):
            if x%y==0:
                prime = False
            y+=1
    
    return prime

max = 20
x = 2
ans = 1
cont = 0

while x<=max:
    if isprime(x):
        cont = 1
        while x**cont <= max:
            cont+=1
        ans *= x**(cont-1)
    x+=1

print(ans)
