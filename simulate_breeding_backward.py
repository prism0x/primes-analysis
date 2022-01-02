
from sortedcontainers import SortedDict

from helper import *
from math import ceil
import sys


primes_dict = [None for i in range(UPPER_LIMIT)]
# primes_dict = SortedDict()
# for i in range(2, UPPER_LIMIT):
    # primes_dict[i] = None


for p in PRIMES:
    primes_dict[p] = Prime(p)


LAST_BREEDABLE = UPPER_LIMIT // 2 - 1

i = LAST_BREEDABLE
while True:
    # print("Outer loop begin", i)
    reset_to_beginning = False
    start = ceil(UPPER_LIMIT / i)
    for j in reversed(range(i, start)):
        # print("    Inner loop begin", j)
        target = i * j
        if primes_dict[j] == None:
            continue
        if primes_dict[i] == None or target >= UPPER_LIMIT:
            continue


        if primes_dict[target] == None:
            oline = "%d x %d = %d"%(i, j, target)
            new_prime = primes_dict[i].breed(primes_dict[j])
            primes_dict[target] = new_prime

            if i == j:
                if primes_dict[i].burned:
                    primes_dict[i] = None
                    reset_to_beginning = True
                    oline += " -- %d burned"%i
            else:
                if  primes_dict[j].burned:
                    primes_dict[j] = None
                    oline += " -- %d burned"%j

                if primes_dict[i].burned:
                    primes_dict[i] = None
                    reset_to_beginning = True
                    oline += " -- %d burned"%i
            print(oline, flush=True)

    remaining_numbers = primes_dict.count(None) - 2

    if reset_to_beginning or i == 2:
        i = LAST_BREEDABLE
        print("Remaining numbers:", remaining_numbers)
    else:
        i = i - 1


    if remaining_numbers == 0:
        break

print("===========")
for i in PRIMES[:31]:
    print(i, primes_dict[i].breed_count)

