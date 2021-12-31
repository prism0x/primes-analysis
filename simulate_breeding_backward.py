
from sortedcontainers import SortedDict

from helper import *
from math import ceil
import sys

class Prime:
    def __init__(self, val, parents=[]):
        self.val = val
        self.parents = parents
        self.breed_count = 0
        self.burned = False

    def breed(self, other):
        if self.val != other.val:
            self.breed_count += 1
            other.breed_count += 1
        else:
            self.breed_count += 1

        if self.parents != []:
            self.burn()

        if other.parents != []:
            other.burn()

        return Prime(self.val*other.val, parents=[self, other])

    def burn(self):
        self.burned = True

# PRIMES_ARR = []

# def add_new_prime()

primes_dict = SortedDict()
for i in range(2, UPPER_LIMIT):
    primes_dict[i] = None


for p in PRIMES:
    primes_dict[p] = Prime(p)


# i = 2
LAST_BREEDABLE = UPPER_LIMIT // 2 - 1

i = LAST_BREEDABLE
while True:
    reset_to_beginning = False
    # for j in range(i, UPPER_LIMIT):
    start = ceil(UPPER_LIMIT / i) + 1
    # import ipdb; ipdb.set_trace()
    # start = UPPER_LIMIT
    for j in reversed(range(i, start)):
        target = i * j
        if primes_dict[j] == None:
            continue
        # if primes_dict[i] == None or target >= UPPER_LIMIT:
            # break
        if primes_dict[i] == None or target >= UPPER_LIMIT:
            continue


        if primes_dict[target] == None:
            oline = "%d x %d = %d"%(i, j, target)
            # print("%d x %d = %d"%(i, j, target))
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
            # sys.stdout.flush()

    # if reset_to_beginning or i == UPPER_LIMIT - 1:
    #     i = 2
    # else:
    #     i = i + 1
    remaining_numbers = primes_dict.values().count(None)

    if reset_to_beginning or i == 2:
        i = LAST_BREEDABLE
        print("Remaining numbers:", remaining_numbers)
    else:
        i = i - 1


    if remaining_numbers == 0:
        break

print("===========")
for i in PRIMES[:31]:
# for i in range(2, 22):
    print(i, primes_dict[i].breed_count)
# print(primes_dict[2].breed_count)

# print(primes_dict)
# print(primes_dict)
# import ipdb; ipdb.set_trace()
# print(PRIMES)