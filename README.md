# Architecture Simulator
A python based compiler that compiles code for a virtual machine that simulates the architecture.
(Python for compiling? Umm, because that's like the only language I know.)

The architecture is based on an instruction set with only ONE instruction, namely 'assign'.

All calculations will be performed by a special circuit called OP (short for operator).
This circuit is a grid of registers.
The rows depict inputs, while columns depict outputs.
Each register in the grid will define if there is a connection between the respective I/O.

There is also a fetch circuit that does all the assigning.

(More info will be added later.)
