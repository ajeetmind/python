
# no of trailing zeroes

def trailing_zeros(n):
    res = 0
    i = 5
    while (n / i >= 1):
        res += n // i
        i *= 5
    return res


print(trailing_zeros(30))

# Pallindrome Numebr

# prime number 

# HCF