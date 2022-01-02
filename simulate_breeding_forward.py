
from sortedcontainers import SortedDict

from helper import *


primes_dict = SortedDict()
for i in range(2, UPPER_LIMIT):
    primes_dict[i] = None


for p in PRIMES:
    primes_dict[p] = Prime(p)


i = 2
while True:
    is_break = False
    for j in range(i, UPPER_LIMIT):
        target = i * j
        if primes_dict[j] == None:
            continue
        if primes_dict[i] == None or target >= UPPER_LIMIT:
            break


        if primes_dict[target] == None:
            oline = "%d x %d = %d"%(i, j, target)
            # print("%d x %d = %d"%(i, j, target))
            new_prime = primes_dict[i].breed(primes_dict[j])
            primes_dict[target] = new_prime

            if i == j:
                if primes_dict[i].burned:
                    primes_dict[i] = None
                    is_break = True
                    oline += " -- %d burned"%i
            else:
                if  primes_dict[j].burned:
                    primes_dict[j] = None
                    oline += " -- %d burned"%j

                if primes_dict[i].burned:
                    primes_dict[i] = None
                    is_break = True
                    oline += " -- %d burned"%i
            print(oline)
            if is_break:
                break

    if i == UPPER_LIMIT - 1:
        i = 2
    else:
        i = i + 1

    if not None in primes_dict.values():
        break

print("===========")
for i in PRIMES[:31]:
    print(primes_dict[i].breed_count)
    # print(i)

