def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        falling_factorial = 1
        next_number_to_mul = n
        while k > 0:
            falling_factorial = falling_factorial * next_number_to_mul
            next_number_to_mul -= 1
            k -= 1
        return falling_factorial
            


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    next_number = y
    sum_of_digits = 0
    while next_number >= 1:
        sum_of_digits += next_number%10
        next_number = next_number//10
    return sum_of_digits

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n:
        if n - (n//10) * 10 == 8:
            n = n//10
            if n - (n//10) * 10  == 8:
                return True
                break
            else:
                continue
        else:
            n = n//10
            continue
    return False
        
