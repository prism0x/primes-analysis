
from sortedcontainers import SortedDict

from helper import *
UPPER_LIMIT =2**14

primes_dict = SortedDict()
for i in range(2, UPPER_LIMIT):
    primes_dict[i] = None


for p in PRIMES:
    if p<UPPER_LIMIT:
        primes_dict[p] = Prime(p)


i = 2
while True:
    reset_to_beginning = False
    for j in range(i, UPPER_LIMIT):
        target = i * j
        
        # j isnt available for breeding so move to next one
        if primes_dict[j] == None:
            continue
        
        # if i isn't available for breeding or the target is too big go to next i
        if primes_dict[i] == None or target >= UPPER_LIMIT:
            break

        # target is a possible match
        if primes_dict[target] == None:
            oline = "%d x %d = %d"%(i, j, target)
#             print("%d x %d = %d"%(i, j, target))
            
            # new_prime has value of target, with parents i,j
            new_prime = primes_dict[i].breed(primes_dict[j])
            
            # target now available for breeding 
            primes_dict[target] = new_prime

            if i == j:
                if primes_dict[i].burned:
                    primes_dict[i] = None
                    reset_to_beginning = True
                    oline += " -- %d burned"%i
            else:
                # reset composite numbers
                if  primes_dict[j].burned:
                    primes_dict[j] = None
                    oline += " -- %d burned"%j

                if primes_dict[i].burned:
                    primes_dict[i] = None
                    reset_to_beginning = True
                    oline += " -- %d burned"%i

#                 print(oline)
    if reset_to_beginning or i == UPPER_LIMIT - 1:
        i = 2
    else:
        i = i + 1
    
    # everything has been found
    if not None in primes_dict.values():
        break
    
print("===========")
for i in PRIMES[:10]:
    if i<UPPER_LIMIT:
        print(i, primes_dict[i].breed_count)

