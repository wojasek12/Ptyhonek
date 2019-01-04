import random
import math
import sys
def wprowadz_liczbe(text = "Wprowadz liczbe: "):
    return int(raw_input(text))

# def check_if_prime(number):
#     ifPrime = True
#     if (number == 1):
#         ifPrime = False
#
#     for i in range(2, number/2 + 1):
#         if number%i == 0:
#             ifPrime = False
#             break
#
#     if(ifPrime):
#         print("Liczba jest pierwsza")
#     else:
#         print("Liczba nie jest pierwsza")
#
a = wprowadz_liczbe()
# check_if_prime(a)

if a == 0 or a == 1:
    print("Number is neither composite nor prime")
    sys.exit()
if a == 2:
    print("Number is prime")
    sys.exit()
b = sum([True if a%factor == 0 else False for factor in ([2] + (range(3, int(math.sqrt(a)), 2)))])

if sum([True if a%factor == 0 else False for factor in ([2] + (range(3, int(math.sqrt(a)), 2)))]):
    print("Number is composite")
else:
    print("Number is prime")