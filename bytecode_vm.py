class BytecodeVM:
  def __init__(self, program):
    self.program = program  # list of (op, arg)
    self.stack = []
    self.ip = 0

  def run(self):
    while self.ip < len(self.program):
      op, arg = self.program[self.ip]
      self.ip += 1

      if op == 'PUSH_INT' or op == 'PUSH_FLOAT' or op == 'PUSH_STR':
        self.stack.append(arg)
      elif op == 'ADD':
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a + b)
      elif op == 'SUB':
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a - b)
      elif op == 'MUL':
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a * b)
      elif op == 'DIV':
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a / b)
      elif op == 'MOD':
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a % b)
      elif op == 'POW':
        b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a ** b)
      elif op == 'PRINT':
        val = self.stack.pop(); print(val)
      elif op == 'POP':
        self.stack.pop()
      elif op == 'HALT':
        break
      else:
        raise RuntimeError(f'Unknown opcode: {op}')

    return self.stack[:]  # final stack snapshot


