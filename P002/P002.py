sum=0
x1=1
x2=2
while x2<=4000000:
    if (x2%2)==0:
        sum = sum + x2
    dum = x1 + x2
    x1 = x2
    x2 = dum

print('The sum is: '+str(sum))

