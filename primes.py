"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import ceil, sqrt

def primes(number_of_primes):
    list = []
    list.append(2)
    prime = 1
    while number_of_primes > 1:
        prime+=1
        for divisor in range(2, ceil(sqrt(prime))+1):
            if prime % divisor == 0:
                break
            elif divisor == ceil(sqrt(prime)):
                list.append(prime)
                number_of_primes-=1
        
    return list
