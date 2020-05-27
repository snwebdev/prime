import pal
import factor

def string_ints_to_int(s):
    return(int(''.join(map(str,s))))


n = 840



pals = pal.pals()
for pal in pals:

    i = string_ints_to_int(pal)
    factors =(factor.all(i))
    if len(factor.pair_2(factors)) > 0:
        print(pal)
        print(factor.pair_2(factors))
