# arm-py32
> Python scripts to disassemble 32-bit ARM binaries

## Usage

### `disassemble.py <bin>`

Use this to view the disassembly of the `.text` section. If need be, modify the script to point to other sections.

```python
# line 11
code = elf.get_section_by_name('.data')
```

### `relocations.py <bin>`

This is a generic script for all ELF files, to view relocation entries.

### `sections.py <bin>`

Again, a generic script for all ELF files. This will list out all the sections present, along with their offsets.
