from aoc import *
from aocasm import *
from copy import deepcopy
      
class DayEight:

  asmCPU = None
  prog = []

  def __init__(self, mem):
    self.asmCPU = AoCASM(deepcopy(mem))
    self.prog = deepcopy(mem)

  def partOne(self):
    try:
      return self.asmCPU.run()
    except LoopError as e:
      return e

  def partTwo(self):
    for i in range(len(self.prog)):
      try:
        prog = deepcopy(self.prog)
        op, arg = prog[i].split()
        if op == "nop":
          prog[i] = "".join(["jmp ", arg])
        elif op == "jmp":
          prog[i] = "".join(["nop ", arg])
        self.asmCPU.loadProg(deepcopy(prog))
        return self.asmCPU.run()
      except LoopError as e:
        pass