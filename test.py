def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n-1)

'''
define
    if n is less than 10
        print "no missing numbers between n and n
    else(n is greater than 10)
        set two parameters: last_digit, without_last
        if without_last is less than 10
            return difference
        else
            call function again(recursive part)
            return the difference between the 
'''