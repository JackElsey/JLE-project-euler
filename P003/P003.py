import math

def test_if_prime(x):
    # Returns True if x is a prime number.
    result = True
    for i in range(2,math.ceil(x/2)+1):
        if x%i==0:
            result = False
            break
    return result

def next_prime_number(x):
    # Finds the next prime number that comes after x. x doesn't have to be prime.
    y_is_prime = False
    y = x
    while not y_is_prime:
        y = y + 1
        y_is_prime = test_if_prime(y)
    return y

x = 2
num = 600851475143
greatest_prime_factor = 1
while x<=num:
    #print(str(num)+', '+str(x)+', '+str(greatest_prime_factor))
    if num%x==0:
        if x>greatest_prime_factor:
            greatest_prime_factor = x
        num = num/x
        x = 2
        continue
    x = next_prime_number(x)

print(str(greatest_prime_factor))
