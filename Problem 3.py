"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

num = 600851475143
ans = 2

while not isprime(num):
    if(isprime(ans)):
        while(num%ans==0):
            num = num/ans
    ans+=1

if num==1:
    print(ans-1)
else:
    print(num)

