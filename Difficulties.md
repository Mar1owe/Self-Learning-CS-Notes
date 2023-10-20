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
```
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