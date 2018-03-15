def fun(a,b):
    # Defines function created by combining two equations provided in the problem so that c is eliminated. When this function is zero, a and b are found.
    result = a**2 + b**2 - (1000 - a - b)**2
    return result

c= -1
for a in range(1,999):
    if c > 0:
        break
    for b in range(1,999):
        if fun(a,b)==0:
            c = 1000 - a - b
            product = a*b*c
            print('product = ' + str(product))
            break
