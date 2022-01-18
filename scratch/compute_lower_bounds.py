from helper import *
from math import floor, ceil


def primes_smaller_than(k):
    return len([i for i in PRIMES if i <= k])


def count_numbers_that_dont_have(k , p):
    result = 0
    for i in range(2, k+1):
        power = 1
        no_prime_factor = True
        while True:
            divisor = p**power
            if divisor > i:
                break
            if i % divisor == 0:
                no_prime_factor = False
                break
            power += 1
        if no_prime_factor:
            # print(i)
            result += 1
    return result

# print("lol", count_numbers_that_dont_have(1000,7))

# import ipdb; ipdb.set_trace()

# Possibly this sequence: https://oeis.org/A105111
multipliers = {
    1: 1,  # 1 -> 1
    2: 1,  # 2 -> 1
    3: 2,  # 2+1 -> 2
    4: 1,  # 4 -> 1
    5: 2,  # 4+1 -> 2
    6: 2,  # 4+2 -> 2
    7: 3,  # 4+2+1 -> 3
    8: 1,  # 8 -> 1
    9: 2,  # 8+1 -> 2
    10: 2,  # 8+2 -> 2
    11: 3,  # 8+2+1 -> 3
    12: 2,  # 8+4 -> 2
    13: 3,  # 8+4+1 -> 3
    14: 3,  # 8+4+2 -> 3
}

for p in PRIMES[:31]:
    total_count = 0
    for i in range(1, 15):
        a = primes_smaller_than((UPPER_LIMIT) / p ** i)
        # print("    >>>", i, a, multipliers[i])
        # total_count += a * multipliers[i]
        # print(i, ceil(i/2))
        total_count += a * ceil(i/2)
        # total_count += floor((UPPER_LIMIT-1)/p**(i+2)) * multipliers[i]
        # total_count += count_numbers_that_dont_have(UPPER_LIMIT, p) * multipliers[i]

    print(p, total_count)
