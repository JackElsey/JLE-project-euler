sum = 0
sum_of_squares = 0

for i in range(1,101):
    sum = sum + i
    sum_of_squares = sum_of_squares + i**2

difference = sum**2 - sum_of_squares
print(str(difference))
