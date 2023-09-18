The computer's *main* memory unit: Random Access Memory, or RAM
# Sequential Logic
Combinatorial: *out[t] = function(in[t])*  
Sequential: *out[t] = function(in[t-1])*

We think about time in digital circuits. We break time into integer time steps and we look at what happens sequentially.
# Flip Flops
**Remembering State**  
We need a gate called Filp-Flops that remembers 0 or 1 by flipping between these two possible states to remember one bit of information from t-1 so that it can be used at time t.

**1-Bit Register**  
If load(t-1) then out(t)=in(t-1) else out(t)=out(t-1)