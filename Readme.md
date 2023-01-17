# SBN Compiler
> Compiles Single Instruction-Set Computer (SIC) assembly code into machine code. The only instruction allowed is SBN (Subtract and Branch if Negative). This compiler was written in Python 3.9.0

## Usage
```
python compile.py <input file> <output file>
```

## Compiler design specifications
The SBN code should be a text file with the following specifications:
- The only instruction allowed is SBN
- Jump address are denoted as <i>.label</i>
- There should not be two labels with the same name
- There are few reserved jump addresses:
    - <i>.start</i> - Address of first instruction, which is always <b>0</b>
    - <i>.next</i> - Address of next instruction, i.e. address of current instruction + 3
    - <i>.exit</i> - Jumps to <i>Terminate Instruction</i>
        - <i>Terminate Instruction</i> is an implicit instruction that is automatically added to the end of the program which always jump to address <b>1000</b>
- SBN instruction should always start in a new line
- Any line that does not start with SBN will be ignored
- Use // to comment
- SBN instruction parameters can be separated using comma or space
- This compiler is case insensitive. So SBN, sbn, SbN, etc. are all valid. Variables and labels are case also case insensitive
- The whole program should be in a single file


## Input File Format



## SBN Instruction
> Syntax:
```
SBN <variable> <variable> <jump address>
```
> The SBN instruction is defined as follows:

Consider the following SBN instruction-
```
SBN A B .loop
```
This will execute the following pseudo code:
```
A := A - B
if A < 0:
    goto .loop
else
    goto .next
```


