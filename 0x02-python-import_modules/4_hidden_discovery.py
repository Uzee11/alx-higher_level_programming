#!/usr/bin/python3

import dis

def print_names():
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()
        instructions = dis.get_instructions(code)

        names = set()
        for instr in instructions:
            if instr.opname == 'LOAD_NAME' and not instr.argval.startswith('__'):
                names.add(instr.argval)

        for name in sorted(names):
            print(name)

if __name__ == "__main__":
    print_names()
