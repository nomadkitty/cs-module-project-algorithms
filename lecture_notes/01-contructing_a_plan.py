'''
We'll say that a positive int divides itself
if every digit in the number divides into the
number evenly.

Example One:
So for example 128 divides itself
since 1, 2, and 8 all divide into 128 evenly. 

Example Two:
64
This dose noe divide itself because 64 is not evenly divisible by 6.

And we'll say that 0 does not divide into anything
evenly, so no number with a 0 digit divides itself. 
Write a function to determine if a number divides itself.
[source - https://codingbat.com/prob/p165941]
'''

# Questions
# How big the numbers we will receive as input?

# Assumptions
# the test has to work for all the numbers
# output will be a boolean (either True or False)


def divides_self(num):
    # if num is equal to zero
    # return false
    if num == 0:
        return False
    # if length of input is 1
        # return True
    if len(str(num)) == 1:
        return True
    # split input into iterable collection of integers
    # loop over collection of digits
    for digit in str(num):
        digit_int = int(digit)
        # if num is not evenly divisible by current digit or current digit is 0
        # return false
        if digit_int == 0 or num % digit_int != 0:
            return False
    # return True if we loop over entire collection
    return True


print(divides_self(0))  # -> false
print(divides_self(1))  # -> true
print(divides_self(10))  # -> false
print(divides_self(128))  # -> true
print(divides_self(12))  # -> true
print(divides_self(120))  # -> false
