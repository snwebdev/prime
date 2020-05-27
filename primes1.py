def f(n):
    d = 2
    for c in range(n):
        while d < c and not c % d == 0:
            d += 1
            if d == c:
                print(c)
        d = 2
        c += 1


print(f(200))
