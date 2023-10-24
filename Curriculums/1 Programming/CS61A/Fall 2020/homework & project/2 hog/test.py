FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    if score == 0:
        return 6
    else:
        i = 1
        while i <= 100 - score:
            pi = (pi - (pi%10)) / 10
            i += 1
    # END PROBLEM 2
    return int(pi % 10)
print(free_bacon(44))