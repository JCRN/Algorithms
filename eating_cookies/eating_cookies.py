#!/usr/bin/python

# 1. Can only eat {1, 2, 3} cookies at a time
#        so with n number of cookies:
#            - eat 1 cookie = (n - 1) remaining cookies
#            - eat 2 cookies = (n - 2) remaining cookies
#            - eat 3 cookies = (n - 3) remaining cookies
# 2. Known combinations:
#        - Only 1 way to eat 0 or 1 cookie: 0 or 1 = 1
#        - 2 cookies has 2 possible combinations, 1 at a time or both together so: 2 = 2
#        - 3 cookies has 4 combinations (info provided): 3 = 4
# 3. Fill cache:
#        - use a dictionary for key:val pairs
#        - key: n  val: the sum of all of the combinations of n


import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n not in cache:
        cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
