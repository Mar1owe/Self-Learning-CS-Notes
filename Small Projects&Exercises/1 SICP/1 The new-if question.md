**`Lisp Scheme`**  
Source: SICP Exercise 1.6

Question:  
Alyssa P. Hacker doesn’t see why `if` needs to be provided as a special form. “Why can’t I just define it as an ordinary procedure in terms of cond?” she asks. Alyssa’s friend Eva Lu Ator claims this can indeed be done, and she defines a new version of `if`:
```Lisp
(define (new-if predicate 
                then-clause 
                else-clause)
  (cond (predicate then-clause)
        (else else-clause)))
```
Eva demonstrates the program for Alyssa:
```Lisp
(new-if (= 2 3) 0 5)
5

(new-if (= 1 1) 0 5)
0
```
Delighted, Alyssa uses new-if to rewrite the square-root program:
```Lisp
(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x) x)))
```
What happens when Alyssa attempts to use this to compute square roots? Explain. 

Solution:  
`if ` is a special form, it first evaluates the predicate, and if that gives a false, the interpreter will then evaluate the else-clause.  
When using `cond`, the interpreter evaluates both of the consequences.  
That is why when Alyssa tries to use the `new-if`, the procedure will call itself again and again until it run out memory.