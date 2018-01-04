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

def general_algorithm(sides):
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
        return None

    return roll

def general_algorithm_debug(sides, numflips=0):
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
        return (None, None, numflips + sum(count))

    return (roll, flip, numflips + sum(count))

FUNC_LIST = {"general": general_algorithm,
             "general_d": general_algorithm_debug}

def roll_die_debug(sides, algo="general", debug=True):
    """ Debug version of generic die rolling sim """
    if algo not in FUNC_LIST:
        raise ValueError("invalid algorithm chosen")
    if not isinstance(sides, int):
        raise TypeError("'sides' must be of type int")
    if sides < 1:
        raise ValueError("'sides' must be positive")
    if sides == 1:
        return 1
    if sides == 2:
        return flip_coin() + 1

    if debug:
        algo += "_d"
        data = (None, None, 0)
        while data[0] is None:
            data = FUNC_LIST[algo](sides, data[2]) #pylint: disable-msg=too-many-function-args
        return data

    roll = None
    while roll is None:
        roll = FUNC_LIST[algo](sides)

    return roll

def roll_die(sides, algo="general"):
    """ Implements the given die simulation """
    return roll_die_debug(sides, algo, False)

def roll_die_test(sides):
    """ Testing die rolls with debug versions """
    res = roll_die_debug(sides)
    if res != None:
        print(res)

def main():
    """ script driver """
    for _ in range(0, 10):
        roll_die_test(12)

# running
main()
