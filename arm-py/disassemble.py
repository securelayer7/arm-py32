# disassemble.py
# displays disassembly of the entire .text section

import sys
from elftools.elf.elffile import ELFFile
from capstone import *

def disassemble(bin_file):
    with open(bin_file, 'rb') as f:
        elf = ELFFile(f)
        code = elf.get_section_by_name('.text')
        ops = code.data()                 # returns a bytestring with the opcodes
        addr = code['sh_addr']            # starting address of `.text`
        md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
        for i in md.disasm(ops, addr):    # looping through each opcode
            print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")

if __name__ == '__main__':
    try:
        disassemble(sys.argv[1])
    except IndexError:
        print('error: requires an argument')
        sys.exit()
