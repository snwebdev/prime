def f(n):
    pf = []
    i = 2
    while i < n:
        while n%i == 0:
            pf.append(i)
            n =  int(n / i)
        i += 1
    pf.append(n)
    pf.sort()
    return(pf)


print(f(2520
        ))