def pair_2(l):
    first = 0
    last = len(l)-1
    f1 = 1
    f2 = 1
    top= 1000
    bottom = 99
    pairs=[]
    total = 1
    for n in l:
        if n > 0:
            total = total * n
    while first < last:
        next = first +1
        while next < last + 1:
            f1 =l[first] * l[next]
            f2 = int(total / f1)
            if  bottom < f1 < top and bottom < f2 < top:
            #if True:
                pairs.append([f1, f2])
            next += 1
        first += 1
    return(pairs)

def all(n):
    f = 2
    l = []
    while f < n + 1:
        while n % f == 0:
            l.append(f)
            n = int(n / f)
        f += 1
    return(l)







