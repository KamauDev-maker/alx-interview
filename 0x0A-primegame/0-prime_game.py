#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(num):
    """
    Method that takes in one arguments and return either true or False
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_up_to_n(n):
    """
    Method that takes in an integer and returns a primes
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Method that takes in two arguments and returns the winner
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes_up_to_n(n)
        total_primes = len(primes)

        if total_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
