# SBN Compiler
> Compiles Single Instruction-Set Computer (SIC) assembly code into machine code. The only instruction allowed is `SBN` (Subtract and Branch if Negative). This compiler was written in Python 3.9.0

## Usage
```sh
python compile.py <input file> <output file>
```

## Compiler design specifications
The `SBN` code should be a text file with the following specifications:
- The only instruction allowed is `SBN`
- Jump address are denoted as <i>.label</i>
- There should not be two labels with the same name
- There are few reserved jump addresses:
    - <i>.start</i> - Address of first instruction, which is always <b>0</b>
    - <i>.next</i> - Address of next instruction, i.e. address of current instruction + 3
    - <i>.exit</i> - Jumps to <i>Terminate Instruction</i>
        - <i>Terminate Instruction</i> is an implicit instruction that is automatically added to the end of the program which always jump to address <b>1000</b>
- `SBN` instruction should always start in a new line
- If a `SBN` parameter is a number then it is treated as an address, not as a variable. Though, it is recommended to use variables instead of numbers as it makes the code more readable and less error prone
- Any line that does not start with `SBN` will be ignored
- Use // to comment
- `SBN` instruction parameters can be separated using comma or space
- This compiler is case insensitive. So `SBN`, `sbn`, `SbN`, etc. are all valid. Variables and labels are case also case insensitive
- The whole program should be in a single file


## Input File Format
> All the variables used in the program must be declared and initialised before the start of the `SBN` instructions. All the variable are treated as `int`. Variables and arrays can be declared in multiple lines. Memory addresses are allocated sequentially after the <i>Terminate Instruction</i> (last instruction added automatically to terminate the program).
### Variable Declaration Syntax
```<variable> = <value> [, <variable> = <value>, ...]```

Example:<br>
```A = 10, B = 20, C = 30```

### Array Declaration Syntax
```<variable>[<size>] = {<value>, <value>, ...}```

Example:<br>
```arr[5] = {1, 2, 3, 4, 5}```




## SBN Instruction
> Syntax:
```
SBN <variable> <variable> <jump address>
```
> The `SBN` instruction is defined as follows:

Consider the following `SBN` instruction-
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


