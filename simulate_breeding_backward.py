from helper import *
from math import ceil
import sys


def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1


primes_dict = [None for i in range(UPPER_LIMIT)]

for p in PRIMES:
    primes_dict[p] = Prime(p)


LAST_BREEDABLE = UPPER_LIMIT // 2 - 1

i = LAST_BREEDABLE
while True:
    # print("Outer loop begin", i)
    is_break = False
    start = ceil(UPPER_LIMIT / i)

    # biggest_free_slot = rindex(primes_dict, None) + 1
    # start = ceil(min(UPPER_LIMIT, biggest_free_slot + 1) / i)
    # print(">>> idx", biggest_free_slot)
    # print(list(reversed(range(2, start))))

    for j in reversed(range(2, start)):
        if primes_dict[i] == None:
            break
        if primes_dict[j] == None:
            continue
        target = i * j
        # print("    Inner loop begin", j)

        if target >= UPPER_LIMIT:
            raise Exception("Something is wrong %d x %d = %d" % (i, j, target))

        if primes_dict[target] == None:
            oline = "%d x %d = %d" % (i, j, target)
            new_prime = primes_dict[i].breed(primes_dict[j])
            primes_dict[target] = new_prime

            if i == j:
                if primes_dict[i].burned:
                    primes_dict[i] = None
                    is_break = True
                    oline += " -- %d burned" % i
            else:
                if primes_dict[j].burned:
                    primes_dict[j] = None
                    oline += " -- %d burned" % j

                if primes_dict[i].burned:
                    primes_dict[i] = None
                    is_break = True
                    oline += " -- %d burned" % i
            print(oline)
            if is_break:
                break

    remaining_numbers = primes_dict.count(None) - 2

    if i == 2:
        i = LAST_BREEDABLE
        print("Remaining numbers:", remaining_numbers)
    else:
        i = i - 1

    if remaining_numbers == 0:
        break

print("===========")
for i in PRIMES[:31]:
    print(i, primes_dict[i].breed_count)
