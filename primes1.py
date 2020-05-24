def f(n):
    primes = []
    d = 2
    for c in range(n):
        while d < c and not c % d == 0:
            d += 1
            if d == c:
                primes.append(c)
        d = 2
        c += 1
    return(primes)


print(f(200))
