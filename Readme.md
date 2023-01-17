# SBN Compiler
Compiles Single Instruction-Set Computer (SIC) assembly code into machine code. The only instruction allowed is SBN (Subtract and Branch if Negative). This compiler was written in Python 3.9.0

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
    - <i>.start</i> - The first instruction
    - <i>.next</i> - The next instruction
    - <i>.exit</i> - Exit the program
- SBN instruction should always start in a new line
- Any line that does not start with SBN will be treated as comment

