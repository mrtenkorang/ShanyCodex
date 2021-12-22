
  
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time


def prime(num: int) -> bool:  # returns a boolean value

    # big question,what is a prime number
    prime_flag = True
    count_divisible = 0
    for v in range(2, num):
        if num % v == 0:
            prime_flag = False
    return prime_flag


def primeGenertor(number: int):
    factlist = [1]
    for b in range(2, number):
        if number % b == 0 and prime(b):
            factlist.append(b)

    return max(factlist)


# prime function works...Hurray .:)

if __name__ == '__main__':
    start = time.time()
    print(primeGenertor(600851475143))
    end = time.time()
    time_difference = (end - start) / 60
    print("Time in Mins ; ", time_difference)
