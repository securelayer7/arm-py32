# sections.py
# displays all the sections present in the binary file

import sys
from elftools.elf.elffile import ELFFile


def sections(bin_file):
    with open(bin_file, 'rb') as f:
        e = ELFFile(f)
        for section in e.iter_sections():
            print(hex(section['sh_addr']), section.name, section['sh_size'])


if __name__ == '__main__':
    try:
        sections(sys.argv[1])
    except IndexError:
        print('error: requires an arguement')
        sys.exit()
