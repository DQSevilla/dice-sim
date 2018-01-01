"""
This script runs the known n-die simulation methods
and should display a graphical distribution of the
results as an output.
"""

import random

COIN = ("H", "T")

def flip_coin():
    """ returns 0 for heads, 1 for tails """
    return 0 if random.random() < 0.5 else 1

def general_algo_helper(sides):
    """ Implements the general roll simulation algorithm.
        Returns the number that was "rolled" by the sim """
    roll = 1
    curr = flip_coin()
    change = second = False
    count = [0, 0]
    count[curr] = 1

    for i in range(2, sides+1):
        prev = curr
        curr = flip_coin()
        count[curr] += 1

        if count[0] > 1 and count[1] > 1:
            change = False
            break

        if not change and curr != prev:
            roll = i
            if i == 2:
                second = True
                continue
            change = True

        if second:
            roll -= 1
            second = False
            change = True

    if not change:
        return general_algo_helper(sides)

    return roll

def general_algo_debug_helper(sides, numflips):
    """ Core code for the debug version of the general algorithm.
        Returns a tupple (roll, flip, numflips) where sides is
        the result of the simulated roll, flip is an array of coin
        flip values that represents that roll, and numflips is the
        total number of coin flips that it took to achieve """
    roll = 1
    curr = flip_coin()
    change = second = False
    count = [0, 0]
    flip = [""]*sides

    count[curr] = 1
    flip[0] = COIN[curr]

    for i in range(2, sides+1):
        prev = curr
        curr = flip_coin()
        count[curr] += 1
        flip[i-1] = COIN[curr]

        if count[0] > 1 and count[1] > 1:
            change = False
            break

        if not change and curr != prev:
            roll = i
            if i == 2:
                second = True
                continue
            change = True

        if second:
            roll -= 1
            second = False
            change = True

    if not change:
        return general_algo_debug_helper(sides, numflips + sum(count))

    return (roll, flip, numflips + sum(count))

def general_algorithm_debug(sides, debug=True):
    """ Debug version of the general roll algorithm """
    if not isinstance(sides, int):
        raise TypeError("Error: 'sides' must be of type int")
    if sides < 1:
        raise ValueError("Error: 'sides' must be positive")
    if sides == 1:
        return 1
    if sides == 2:
        return flip_coin()
    if debug:
        return general_algo_debug_helper(sides, 0)

    return general_algo_helper(sides)

def general_algorithm(sides):
    """ General algorithm for die simulation """
    return general_algorithm_debug(sides, False)

def roll_die_test(sides):
    """ Testing die rolls with debug versions """
    print(general_algorithm_debug(sides))

def main():
    """ script driver """
    for _ in range(0, 10):
        roll_die_test(4)

# running
main()
