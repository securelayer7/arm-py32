import sys
from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection

def relocations(bin_file):
    with open(bin_file, 'rb') as f:
        e = ELFFile(f)
        for section in e.iter_sections():
            if isinstance(section, RelocationSection):
                print(f'{section.name}:')
                symbol_table = e.get_section(section['sh_link'])
                for relocation in section.iter_relocations():
                    symbol = symbol_table.get_symbol(relocation['r_info_sym'])
                    addr = hex(relocation['r_offset'])
                    print(f'{symbol.name} {addr}')


if __name__ == '__main__':
    try:
        relocations(sys.argv[1])
    except IndexError:
        print('error: requires an argument')
        sys.exit()
