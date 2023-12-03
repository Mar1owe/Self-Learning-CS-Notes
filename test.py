def even_weighted(s):
    return [i*s[i] for i in range(0,len(s)) if i%2 ==0]