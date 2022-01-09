import csv

UPPER_LIMIT = 2 ** 14
# UPPER_LIMIT = 1024
# UPPER_LIMIT = 32
PRIME_FACTORS_FILE = "prime_factors.csv"


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
            if not self.is_prime():
                raise Exception("Composites cannot be squared: %d" % self.val)

            self.breed_count += 1

        if not self.is_prime():
            self.burn()

        if not other.is_prime():
            other.burn()

        return Prime(self.val * other.val, parents=[self, other])

    def is_prime(self):
        return self.parents == []

    def burn(self):
        self.burned = True


def erastothenes_sieve(n):
    """Get primes up to n in a list.
    Won't need to implement this in solidity.
    This is just to generate primes."""
    primes = []
    composites = []
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(1, n + 1):
        if prime[p]:
            primes.append(p)
            # print(p) #Use print(p) for python 3
        else:
            composites.append(p)
    return primes, composites


PRIMES, COMPOSITES = erastothenes_sieve(UPPER_LIMIT)
PRIME_INDICES = {}  # A mapping prime -> index (0 based)
for n, p in enumerate(PRIMES):
    PRIME_INDICES[p] = n


def hamming_weight(n):
    c = 0
    while n:
        c += 1
        n &= n - 1

    return c
