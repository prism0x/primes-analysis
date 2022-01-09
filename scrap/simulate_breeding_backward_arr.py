from helper import *
from math import ceil
import sys


def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1


primes_arr = [None for i in range(UPPER_LIMIT + 1)]

for p in PRIMES:
    primes_arr[p] = Prime(p)


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
        if primes_arr[i] == None:
            break
        if primes_arr[j] == None:
            continue
        target = i * j
        # print("    Inner loop begin", j)

        if target >= UPPER_LIMIT:
            raise Exception("Something is wrong %d x %d = %d" % (i, j, target))

        if primes_arr[target] == None:
            oline = "%d x %d = %d" % (i, j, target)
            new_prime = primes_arr[i].breed(primes_arr[j])
            primes_arr[target] = new_prime

            if i == j:
                if primes_arr[i].burned:
                    primes_arr[i] = None
                    is_break = True
                    oline += " -- %d burned" % i
            else:
                if primes_arr[j].burned:
                    primes_arr[j] = None
                    oline += " -- %d burned" % j

                if primes_arr[i].burned:
                    primes_arr[i] = None
                    is_break = True
                    oline += " -- %d burned" % i
            print(oline)
            if is_break:
                break

    remaining_numbers = primes_arr.count(None) - 2

    if i == 2:
        i = LAST_BREEDABLE
        print("Remaining numbers:", remaining_numbers)
    else:
        i = i - 1

    if remaining_numbers == 0:
        break

print("===========")
for i in PRIMES[:31]:
    print(i, primes_arr[i].breed_count)
