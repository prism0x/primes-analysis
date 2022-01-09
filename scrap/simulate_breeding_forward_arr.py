
from sortedcontainers import SortedDict

from helper import *


# primes_arr = SortedDict()
# for i in range(2, UPPER_LIMIT+1):
#     primes_arr[i] = None


# for p in PRIMES:
#     primes_arr[p] = Prime(p)

primes_arr = [None for i in range(UPPER_LIMIT + 1)]

for p in PRIMES:
    primes_arr[p] = Prime(p)

ofile = open("breeding_sequence.js", "w")
ofile.write("BREEDING_SEQUENCE = [\n")

i = 2
while True:
    is_break = False
    for j in range(i, UPPER_LIMIT):
        target = i * j
        if primes_arr[j] == None:
            continue
        if primes_arr[i] == None or target > UPPER_LIMIT:
            break


        if primes_arr[target] == None:
            oline = "%d x %d = %d"%(i, j, target)
            ofile.write("  [%d, %d],\n"%(i,j))
            # print("%d x %d = %d"%(i, j, target))
            new_prime = primes_arr[i].breed(primes_arr[j])
            primes_arr[target] = new_prime

            if i == j:
                if primes_arr[i].burned:
                    primes_arr[i] = None
                    is_break = True
                    oline += " -- %d burned"%i
            else:
                if  primes_arr[j].burned:
                    primes_arr[j] = None
                    oline += " -- %d burned"%j

                if primes_arr[i].burned:
                    primes_arr[i] = None
                    is_break = True
                    oline += " -- %d burned"%i
            print(oline)
            if is_break:
                break

    # remaining_numbers = primes_arr.count(None) - 2

    if i == UPPER_LIMIT:
        i = 2
        # print("Remaining numbers:", remaining_numbers)
    else:
        i = i + 1

    # if not None in primes_arr.values():
    #     break

    if not None in primes_arr[2:]:
        break

    # if remaining_numbers == 0:
    #     break

ofile.write("]")

print("===========")
for i in PRIMES[:31]:
    print(i, primes_arr[i].breed_count)
    # print(i)

