number = 0
number_found = False

while not number_found:
    number = number + 1
    if number%100000==0:
        print(str(number))
    number_found = True
    for i in range(2,21):
        if number%i!=0:
            number_found = False
            break

print('The number is '+str(number))
