
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def ispalindrome(x):
    y = str(x)
    l = len(y)
    i = 0
    ans = True
    if(l%2==0):
        while i<l/2 and ans:
            if(y[i]!=y[l-i-1]):
                ans = False
            i+=1
    else:
        ans = False
    return ans

x = 999
y = 999
found = False

while y > 1 and not found:
    while y > x:
        y-=1
        x+=1
    while x<=999 and not found:
        z =x*y
        found = ispalindrome(z)
        y-=1
        x+=1
    x=y
    y=999

print(z)


    




