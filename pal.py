def pals():
    l = []
    for x in range(997,111,-1):
        half = [int(x) for x in str(x)]
        otherhalf = list(half)
        otherhalf.reverse()
        l.append((half + otherhalf))
    return(l)
