k = 1
def hailstone(n):
    if n == 1:
        k += 1
        print(k)
        return 1
    elif n%2 ==0:
        k += 1
        print(n/2)
        return hailstone(n/2)
    else:
        k += 1
        print(3*n + 1)
        return hailstone(3*n + 1)