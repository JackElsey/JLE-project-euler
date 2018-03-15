def test_if_palindromic(x):
    # Returns True if x is palindromic, which means that x is read the same way forwards as it is read backwards (e.g., "9009").
    str_x = str(x)
    if str_x == str_x[::-1]:
        return True
    else:
        return False

palindromes = {}
for i in range(1,1000):
    for j in range(1,1000):
        if test_if_palindromic(i*j):
            palindromes.update({i*j:[i,j]})

print(str(max(palindromes.keys())))
