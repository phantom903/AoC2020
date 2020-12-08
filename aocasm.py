from copy import deepcopy

class LoopError(Exception):
  pass

class AoCASM:

  mem = []
  halted = False
  acc = 0
  ptr = 0
  opsDone = []

  def __init__(self, mem):
    self.mem = deepcopy(mem)
    self.halted = False
    self.acc = 0
    self.ptr = 0
    self.opsDone.clear()

  def loadProg(self, mem):
    self.mem.clear()
    self.mem = deepcopy(mem)
    self.halted = False
    self.acc = 0
    self.ptr = 0
    self.opsDone.clear()

  def run(self):
    while not self.halted:
      op, arg = self.mem[self.ptr].split()
      if self.ptr in self.opsDone:
        raise LoopError("Infinite loop detected, acc: " + str(self.acc) + ", ptr: " + str(self.ptr) + ", op: " + self.mem[self.ptr])
        self.halted = True
      else:
        self.opsDone.append(self.ptr)
        if op == "nop":
          self.ptr += 1
        elif op == "acc":
          self.acc += int(arg)
          self.ptr += 1
        elif op == "jmp":
          self.ptr += int(arg)
          if self.ptr < 0:
            raise LoopError("Less than zero")
            self.halted = True
        if self.ptr >= len(self.mem):
          return self.acc
