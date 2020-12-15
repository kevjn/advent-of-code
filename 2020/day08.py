#!/usr/bin/env python3.9
import itertools as it
import re
from collections import defaultdict

class Computer:
    ops = {
        'nop': lambda self, x: None,
        'acc': lambda self, x: setattr(self, 'acc', self.acc + x),
        'jmp': lambda self, x: setattr(self, 'pc', self.pc + (x-1))
    }

    def __init__(self):
        self.pc = 0
        self.acc = 0
        self.memory = set()

    def run(self, prog):
        _exit = False

        while not _exit:
            op, arg = prog[self.pc].split()

            if self.pc in self.memory:
                # infinite loop
                return False

            self.memory.add(self.pc)

            self.pc += 1
            self.ops[op](self, int(arg))

            _exit = self.pc == len(prog)

        return _exit


program = [line.rstrip() for line in open('in1')]

c = Computer()
c.run(program)

print(c.acc)

for i, instr in enumerate(program):
    _program = program.copy()
    if instr.startswith('jmp'):
        _program[i] = instr.replace('jmp', 'nop')
    elif instr.startswith('nop'):
        _program[i] = instr.replace('nop', 'jmp')

    c = Computer()
    if c.run(_program):
        print(c.acc)
        break