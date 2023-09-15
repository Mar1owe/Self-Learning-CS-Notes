Key concepts: Binary numbers, binary addition, the two's complement method, half-adders, full-adders, n-bit adders, counters, Arithmetic Logic Unit (ALU), combinational logic. 

# Binary Numbers
Maximum with *k* bits is  
$1 +2 +4 + ... + 2^{k-1} = 2^k-1 $

Binary -> Decimal
Decimal -> Binary

# Binary Addition
Half Adder - adds two bits  
->
Full Adder - Add three bits  
->
Adder - Adds two numbers (2 16-bits buses)
# Negative Numbers
**2's Complement**  
Represent negative numbers $-x$ using the positive number $2^n-x$.
```
0000 0
0001 1
0010 2
0011 3
0100 4
0101 5
0110 6
0111 7
1000 -8 (8)
1001 -7 (9)
1010 -6 (10)
1011 -5 (11)
1100 -4 (12)
1101 -3 (13)
1110 -2 (14)
1111 -1 (15)
```

```
-2   14   1110
+    +    +
-3   13   1101

-5   11   11011
          ^
          1011
```

## Computing $-x$
Input: $x$  
Output: $-x$  

Idea: $2^n-x = 1 + (2^n-1) -x$

For example: input $4$
```
 1111
-
 0100
------
 1011
+
    1
------
1100
```
Output $-4$
# Arithmetic Logic Unit
The ALU computes a function on the two inputs, and outputs the result.  
## The Hack ALU
pre-setting the x input  
zx: if zx then x=0  
nx: if nx then x=!x  

pre-setting the y input  
zy: if zy then y=0  
ny: if ny then y=!y

selecting between computing `+` or `&`  
f: if f then out=x+y else out=x&y  

post-setting the output  
no: if no then out=!out

Resulting ALU output
out: out(x,y)=