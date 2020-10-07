"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""


    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.reg[7] = 0xF4
        self.hlt = False

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value

    def load(self, filename):
        """Load a program into memory."""
        print("LOADING...")

        address = 0

        with open(filename) as file_pointer:
            for line in file_pointer:
                line_split = line.split("#")
                num = line_split[0].strip()
                if num == '':
                    continue
                value = int(num, 2)
                self.ram_write(value, address)
                address += 1

        print("LOADING COMPLETE")


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while not self.hlt:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read( self.pc + 1 )
            operand_b = self.ram_read( self.pc + 2 )
            self.exe_instruction(IR, operand_a, operand_b)

    # executes the instructions given, takes the instruction register
    # and the next two line of machine code to operate
    def exe_instruction(self, IR, operand_a, operand_b):
        """Run the instructions"""
        print("EXECUTING INSTRUCTIONS...")
        if IR == HLT:
            print("HLT: TRUE\nEXITING...")
            self.hlt = True
        elif IR == LDI:
            print("LDI...")
            self.reg[operand_a] = operand_b
            self.pc += 3
        elif IR == PRN:
            print( "PRN REG:    ", self.reg[operand_a] )
            self.pc += 2
        elif IR == MUL:
            print("MUL...")
            mul_value = self.reg[operand_a] * self.reg[operand_b]
            self.reg[operand_a] = mul_value
            self.pc += 3
        else:
            print("INVALID COMMAND... EXITING...")
            sys.exit(1)

"""
        elif IR == PUSH:
            reg[SP] -= 1
            reg_to_get_value_in = memory[pc + 1]
            value_in_register = reg[reg_to_get_value_in]
            memory[reg[SP]] = value_in_register
            pc += 2
        elif IR == POP:
            top_value_in_stack = memory[reg[SP]]
            reg_to_store_in = memory[pc + 1]
            reg[reg_to_store_in] = top_value_in_stack
            reg[SP += 1]
            pc += 2
"""
