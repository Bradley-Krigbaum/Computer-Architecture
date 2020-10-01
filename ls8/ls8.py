#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

"""
###############
### ALU OPS ###
###############

#     CODE     REG A    REG B
ADD = 10100000 00000aaa 00000bbb
SUB = 10100001 00000aaa 00000bbb
MUL = 10100010 00000aaa 00000bbb
DIV = 10100011 00000aaa 00000bbb
MOD = 10100100 00000aaa 00000bbb

#     CODE     REG
INC = 01100101 00000rrr
DEC = 01100110 00000rrr

#     CODE     REG A    REG B
CMP = 10100111 00000aaa 00000bbb

#     CODE     REG A    REG B
AND = 10101000 00000aaa 00000bbb

#     CODE     REG
NOT = 01101001 00000rrr

#     CODE     REG A    REG B
OR  = 10101010 00000aaa 00000bbb
XOR = 10101011 00000aaa 00000bbb
SHL = 10101100 00000aaa 00000bbb
SHR = 10101101 00000aaa 00000bbb

################
### MUTATORS ###
################

#      CODE     REG
CALL = 01010000 00000rrr
RET = 00010001

#     CODE     REG
INT = 01010010 00000rrr
IRET = 00010011

#     CODE     REG
JMP = 01010100 00000rrr
JEQ = 01010101 00000rrr
JNE = 01010110 00000rrr
JGT = 01010111 00000rrr
JLT = 01011000 00000rrr
JLE = 01011001 00000rrr
JGE = 01011010 00000rrr

#############
### OTHER ###
#############

#     CODE 0
NOP = 00000000

#     CODE 1
HLT = 00000001 

# IM-8bv:   immediate 8-bit value
#     CODE     REG      IM-8bv
LDI = 10000010 00000rrr iiiiiiii

#    CODE     REG A    REG B
LD = 10000011 00000aaa 00000bbb
ST = 10000100 00000aaa 00000bbb

#      CODE     REG
PUSH = 01000101 00000rrr
POP = 01000110 00000rrr

#     CODE     REG
PRN = 01000111 00000rrr
PRA = 01001000 00000rrr
"""



cpu.load()
cpu.run()
