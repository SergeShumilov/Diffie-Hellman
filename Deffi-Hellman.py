"""This is simple script for Diffie-Hellman's protocol"""
import random


def isPrime(n):
    """check if the number is prime"""

    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def number_generation():
    """These numbers are not kept in secret"""
    prime_numbers = [i for i in range(10000, 20000) if isPrime(i)]

    p = random.choice(prime_numbers)
    y = 20000
    while y >= p-1:
        y = random.choice(prime_numbers)

    nums = list()
    nums.append(p)
    nums.append(y)

    return nums


nums = number_generation()


# Deffi-Hellman's Protocol
a_choice = int(input('Enter an integer to send: '))  # secret number by a


def a_protocol_func():

    k_a = (nums[1] ^ a_choice) % nums[0]  # calculating key for user a
    return k_a


b_choice = int(input('Enter an integer to send: '))  # secret number by b


def b_protocol_func():

    k_b = (nums[1] ^ b_choice) % nums[0]  # calculating key for user b
    return k_b


def get_secret_key():
    # calculating secret key
    ka = (b_protocol_func() ^ a_choice) % nums[0]
    kb = (a_protocol_func() ^ b_choice) % nums[0]
    if ka == kb:
        print("Secret key: " + str(kb))
    else:
        print('Something wrong')


if __name__ == '__main__':
    get_secret_key()
