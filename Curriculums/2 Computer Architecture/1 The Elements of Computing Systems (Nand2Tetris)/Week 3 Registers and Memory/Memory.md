The computer's *main* memory unit: Random Access Memory, or RAM
# Sequential Logic
Combinatorial: *out[t] = function(in[t])*  
Sequential: *out[t] = function(in[t-1])*

We think about time in digital circuits. We break time into integer time steps and we look at what happens sequentially.
# Flip Flops
**Remembering State**  
We need a gate called Filp-Flops that remembers 0 or 1 by flipping between these two possible states to remember one bit of information from t-1 so that it can be used at time t.

**The "Clocked Data Flip Flop" (DFF)**
out[t] = in[t-1]

**1-Bit Register**  
Goal: remember an input bit "forever": until requested to load a new value.  
If load(t-1) then out(t)=in(t-1) else out(t)=out(t-1)
# Memory Units
**RAM / Read Logic**
To read Register i:
    
    set address = i

Result:

    out emits the state of Register i

To set Register i to v:

    set address = i
    set in = v
    set load = 1

Result:

    The state of Register i becomes v
    From the next cycle onward, out emits v
# Counters
Program Counter

Reset: fetch the first instruction `PC = o`  
Next: fetch the next instruction `PC++`  
Goto: fetch instruction n `PC = n`