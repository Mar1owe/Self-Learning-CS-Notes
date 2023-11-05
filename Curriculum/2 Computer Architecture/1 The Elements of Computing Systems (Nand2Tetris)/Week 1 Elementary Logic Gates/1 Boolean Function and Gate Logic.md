# Boolean Logic
Boolean Values: 0 and 1

Boolean Operations:
- x And y  
- x Or y  
- NOT(x)  

Boolean Expressions:  
Not(0 OR (1 AND 1)) = NOT(1)

Boolean Functions:  
two ways to describe: formula, truth table  
f(x,y,z) = (x AND y) OR (NOT(x) AND z)

Boolean Identities:  
1. Commutative Laws
    - (x AND y) = (y AND x)
    - (x OR y) = (y OR x)
2. Associative Laws
    - (x AND (y AND z)) = ((x AND y) AND z)
    - (x OR (y OR z)) = ((x OR y) OR z)
3. Distributive Laws
    - (x AND (y OR z)) = (x AND y) OR (x AND z)
    = (x OR (y AND z)) = (x OR y) AND (x OR Z)
4. De Morgan Laws
    - NOT(x AND y) = NOT(x) OR NOT(y)
    - NOT(x OR y) = NOT(X) AND NOT(y)

Boolean Algebra:  
NOT(NOT(x) AND NOT(x OR y)) =  
NOT(NOT(x) AND (NOT(x) AND NOT(y))) =  
NOT((NOT(x) AND NOT(x)) AND NOT(y)) =  
NOT(NOT(x) AND NOT (y)) =  
NOT(NOT(x)) OR NOT(NOT(y)) =  
x OR y
# Boolean Functions Synthesis
Truth table to boolean expression:  
Given a truth table, we pay attention to every output that is "1", write a expression that satisfies that row. We do this to every "1" output and `OR` them together.

**Any Boolean function can be represented using an expression containing AND, OR and NOT opeartions.**

(x NAND y) = NOT(x AND y)

**Any Boolean function can be represented using an expression containing only NAND operations.**

(1) NOT(x) = (x NAND x)
(2) (x AND y) = NOT(x NAND y)
# Logic Gates
## Gate Logic
- A technique for implementing Boolean functions using logic gates.
- Logic gates:
    - Elementary (NAND, AND, OR, NOT)
    - Composite (MUX, ADDER)


Gate Interface / Gate Implementation:  
Two perspectives: internal (***implementation***, for builders), external (***interface***, for users)

Circuit implementation
- This course does not deal with physical implementations
- Circuits, transistors, relays, ... these are EE, not CS
# Hardware Description Language(HDL)
- HDL is a functional / declarative language
- The order of HDL statements is indignificant
- Before using a chip part, you must know its interface

The most common HDLs: VHDL, Verilog
# Hardware Simulation
Simulation options:  
- Interactive
- Script-based
- With / without output and compare files

The logic of a typical test script
- Initialize
    - Load an HDL file
    - Create an empty output file
    - List the names of the pins whose values will be writtent the output file
- Repeat
    - set-eval-output

Simulation-with-compare-file logic:  
- When each `output` command is executed, the outputted line is compared to the corresponding line in th compare file.
- If the two lines are not the same, the simulator throws a comparison error.

Behavioral simulation:  
- The chip logic can be implemented in some high-level language
- Enables high-level planning and testing of a hardware architecture before writing any HDL code

Hardware construction projects:  
- The players (first approximation):
    - System architects
    - Developers
- The system architect decides which chips are needed
- For each chip, the architect creates
    - a chip API
    - a test script
    - a compare file
- Given the resources, the developers can build the chips.
# Multi-bit Buses
**Array of Bits**
- Sometimes we manipulate "together" an array of bits
- It is conceptually convenient to think about such a group of bits as a single entity, sometime termed "bus"
- HDLs will usually provide some convenient notation for handling these buses.

**Sub-buses**
- Buses can be composed from (and broken into) sub-buses.
- Some syntactic choices of our HDL
    - Overlaps of sub-buses are allowed on output bused of parts
    - Width of internal pins is deduced automatically
    - "false" and "true" may be used as buses of any width