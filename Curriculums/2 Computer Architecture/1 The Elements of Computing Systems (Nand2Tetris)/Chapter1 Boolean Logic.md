> "The only kind of learning which significantly influences behavior is self-discovered or self appropriated--truth that has been assimilated in experience" --Psychologist Carl Rogers

Every general-purpose computer--every PC, smartphones, or server--is a Nand to Tetris machine

ALU : Arithmetic Logic Unit
RAM : Random Access Memory

*Church-Turing conjecture*

computer platform used: Hack
high-level language implemented: Jack

A Computer System is built by breaking the system into "modules"  
module design: an acquired art

"Hardware Discription Language" in appendix 2 (1 hour learning)
We will test the correctness of the HDL programs by using a software-based hardware simulator, just like how hardware engineers work.

---
# Boolean Algebra
Two state binary values: 1 and 0.

## Boolean Operators
{And, Or, Not} is one of various subsets that can express any Boolean function, and any of these three and be expressed using **Nand** (proof in appendix 1)
> Nand(x,y) is equivalent to Not(And(x,y))

## Boolean Functions
To define boolean functions, use a *truth table* or *Boolean expressions*

## Truth Tables and Boolean Expressions

Truth table: convenient means for describing states of nature  
Boolean expression: convenient formalism for realizing the description in silicon

The ability of simplifing Boolean expressions is important.
# Logic Gates
 gate - transistor - silicon - chip

**Primitive and Composite Gates**  
Any given logic gate can be viewed from two different perspectives: internal and external, interface and implementation

All logic gates have the same input and output data types: 0's and 1's, so they can be combined to form *composite gates*

Two perspectives: internal (***implementation***, for builders), external (***interface***, for users)

Logic design: Given a
gate abstraction (also referred to as *specification*, or interface), find an
efficient way (meaning as few gates as possible) to implement it using other gates that were already
implemented.
# Hardware Construction
## Hardware Description Language (HDL)

an HDL definition of a chip = a *header* section + a *parts* section

# Specification
