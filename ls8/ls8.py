#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

"""
###############
### ALU OPS ###
###############

ADD = 10100000 00000aaa 00000bbb
SUB = 10100001 00000aaa 00000bbb
MUL = 10100010 00000aaa 00000bbb
DIV = 10100011 00000aaa 00000bbb
MOD = 10100100 00000aaa 00000bbb

INC = 01100101 00000rrr
DEC = 01100110 00000rrr

CMP = 10100111 00000aaa 00000bbb

AND = 10101000 00000aaa 00000bbb
NOT = 01101001 00000rrr
OR  = 10101010 00000aaa 00000bbb
XOR = 10101011 00000aaa 00000bbb
SHL = 10101100 00000aaa 00000bbb
SHR = 10101101 00000aaa 00000bbb

################
### MUTATORS ###
################

CALL = 01010000 00000rrr
RET = 00010001

INT = 01010010 00000rrr
IRET = 00010011

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

NOP = 00000000

HLT = 00000001 

LDI = 10000010 00000rrr iiiiiiii

LD = 10000011 00000aaa 00000bbb
ST = 10000100 00000aaa 00000bbb

PUSH = 01000101 00000rrr
POP = 01000110 00000rrr

PRN = 01000111 00000rrr
PRA = 01001000 00000rrr
"""


pc = 0
running = True

memory = [

]

def ram_read():
    pass

def ram_write():
    pass


cpu.load()
cpu.run()
