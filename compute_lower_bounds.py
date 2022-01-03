from helper import *


def primes_smaller_than(k):
    return len([i for i in PRIMES if i < k])


# def count_numbers_that_dont_have(k , n):
#     result = 0
#     for i in range(2, k+1):
#         power = 1
#         no_prime_factor = True
#         while True:
#             divisor = 2**power
#             if divisor > i:
#                 break
#             if i % divisor == 0:
#                 no_prime_factor = False
#                 break
#             power += 1
#         if no_prime_factor:
#             result += 1
#     return result


# Possibly this sequence: https://oeis.org/A105111
multipliers = {
    1: 1,  # 2 -> 1
    2: 1,  # 2*2 -> 1
    3: 2,  # 2*2*2 -> 2
    4: 1,  # 2*2*2*2 -> 1
    5: 2,  # 2*2*2*2 * 2 -> 2
    6: 2,  # 2*2*2*2 * 2*2 -> 2
    7: 3,  # 2*2*2*2 * 2*2 * 2 -> 3
    8: 1,  # 2*2*2*2*2*2*2*2 -> 1
    9: 2,  # 2*2*2*2*2*2*2*2 * 2 -> 2
    10: 2,  # 2*2*2*2*2*2*2*2 * 2*2 -> 2
    11: 3,  # 2*2*2*2*2*2*2*2 * 2*2 * 2 -> 3
    12: 3,  # 2*2*2*2*2*2*2*2 * 2*2*2*2 -> 2
    13: 3,  # 2*2*2*2*2*2*2*2 * 2*2*2*2 * 2 -> 3
    14: 3,  # 2*2*2*2*2*2*2*2 * 2*2*2*2 * 2*2 -> 3
}

for p in PRIMES[:31]:
    total_count = 0
    for i in range(1, 15):
        a = primes_smaller_than(UPPER_LIMIT / p ** i)
        # print(i, a, multipliers[i])
        total_count += a * multipliers[i]

    print(p, total_count)
