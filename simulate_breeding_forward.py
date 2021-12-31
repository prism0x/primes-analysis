
from sortedcontainers import SortedDict

from helper import *


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


i = 2
while True:
    reset_to_beginning = False
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
            print(oline)

    if reset_to_beginning or i == UPPER_LIMIT - 1:
        i = 2
    else:
        i = i + 1

    if not None in primes_dict.values():
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