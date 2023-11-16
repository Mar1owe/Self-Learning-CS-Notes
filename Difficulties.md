# Programming
1. 
Define a function `cycle` that takes in three functions `f1`, `f2`, `f3`, as arguments. `cycle` will return another function that should take in an integer argument `n` and return another function. That final function should take in an argument `x` and cycle through applying `f1`, `f2`, and `f3` to `x`, depending on what `n` was. Here's what the final function should do to `x` for a few values of n:

`n = 0`, return `x`  
`n = 1`, apply `f1` to `x`, or return `f1(x)`  
`n = 2`, apply `f1` to `x` and then `f2` to the result of that, or return `f2(f1(x))`  
`n = 3`, apply `f1` to `x`, `f2` to the result of applying `f1`, and then `f3` to the result of applying `f2`, or `f3(f2(f1(x)))`  
`n = 4`, start the cycle again applying `f1`, then `f2`, then `f3`, then `f1` again, or `f1(f3(f2(f1(x))))`
    And so forth.
    
Hint: most of the work goes inside the most nested function.
```Python
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def apply_functions(x, n):
        if n == 0:
            return x
        elif n == 1:
            return f1(x)
        elif n == 2:
            return f2(f1(x))
        elif n == 3:
            return f3(f2(f1(x)))
        else:
            composed_function = compose_functions(f1, f2, f3, n)
            return composed_function(x)

    def compose_functions(f1, f2, f3, n):
        if n == 0:
            return lambda x: x
        elif n == 1:
            return f1
        elif n == 2:
            return lambda x: f2(f1(x))
        elif n == 3:
            return lambda x: f3(f2(f1(x)))
        else:
            return lambda x: compose_functions(f1, f2, f3, n - 3)(f3(f2(f1(x))))

    return lambda n: lambda x: apply_functions(x, n)

```

2. 
```Python
def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def count_partitions(n, current_coin):
        if n == 0:
            return 1
        if n < 0 or current_coin is None:
            return 0
        # Include the current coin and move to the next larger coin, or exclude the current coin
        with_current_coin = count_partitions(n - current_coin, current_coin)
        without_current_coin = count_partitions(n, next_largest_coin(current_coin))
        return with_current_coin + without_current_coin

    return count_partitions(total, 1)
```

3. 
```Python
def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(s,t):
        if s == t[0]:
            return len(t)
        else:
            return helper(s,t[1::])

    if not w1:
        return w2
    else:
        i = len(w2) - helper(w1[0],w2)
        return add_chars(w1[1::],w2[:i]+w2[i+1:])
```

4. 
Write a function that takes in a list and returns the maximum product that
can be formed using nonconsecutive elements of the list. The input list will
contain only numbers greater than or equal to 1.
```Python
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
```