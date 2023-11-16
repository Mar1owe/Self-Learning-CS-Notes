def even_weighted(s):
    ls = []
    for i in range(0, len(s)):
        if i%2 == 0:
            ls += [i*s[i]]
    return ls