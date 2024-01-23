import os

def fizzbuzz():

    size = 21

    for i in range(1, size):
        if i % 3 == 0:
            print(f"{i} Fizz")
        elif i % 5 == 0:
            print(f"{i} Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")

fizzbuzz()
