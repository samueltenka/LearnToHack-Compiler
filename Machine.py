#Michigan Hackers Presentation on Compilers
import EnsureVersion3

'''
instructions:
jumpif0 <address#> <register#>
load <address#> <register#>
store <address#> <register#>
swap <register#> <register#>
copy <register#> <register#>
add <register#> <register#>
subtract <register#> <register#>
multiply <register#> <register#>
divide <register#> <register#>
modulo <register#> <register#>
compare <register#> <register#>
<note: program might also contain literal numbers in addition to instructions>
Program execution ends when the program counter reaches -1.

machine specifics:
a list of instructions and floats,
the zeroth of which is 0.0,
the next one, a sensor input [or keyboard state],
the next one, a motor output [or monitor state],
and the remaining program and variable space.
'''

class Machine:
   def __init__(self, num_addresses, num_registers, debug=False):
      self.memory = [0.0 for i in range(num_addresses)]
      self.registers = [0.0 for i in range(num_registers)]
      self.execution = 3 #TODO: find better name for this: it's the address of the next instruction to execute
      self.debug = debug
   def load_program(self, lines, inp=0.0):
       self.memory[1] = inp
       for i in range(len(lines)):
           self.memory[3+i] = lines[i] if ' ' in lines[i] else eval(lines[i])
   def print_mem(self, l=8):
      print('memory', ' '.join(str(s).replace(' ','_') for s in self.memory[:l])+'. . .')
      print('registers', self.registers)
   def run(self):
      while self.execution != -1:
          if self.debug:
             self.print_mem()
          self.step()
      self.print_mem()
   def step(self):
      instr = self.memory[self.execution]
      print("instr ", self.execution, instr)
      command, arg0, arg1 = instr.split(' ')
      getattr(self,command)(eval(arg0),eval(arg1))
      self.execution += 1

   def jumpif0(self, a, r):
      if self.registers[r]==0.0:
         self.execution = a-1 #minus one since we always increment
   def load(self, a, r): self.registers[r] = self.memory[a]
   def store(self, a, r): self.memory[a] = self.registers[r]
   def swap(self, r, r_): self.registers[r],self.registers[r_] = self.registers[r_],self.registers[r]
   def copy(self, r, r_): self.registers[r_] = self.registers[r]
   def add     (self, r, r_): self.registers[r_] += self.registers[r]
   def subtract(self, r, r_): self.registers[r_] -= self.registers[r]
   def multiply(self, r, r_): self.registers[r_] *= self.registers[r]
   def divide  (self, r, r_): self.registers[r_] /= self.registers[r]
   def modulo  (self, r, r_): self.registers[r_] = float(int(self.registers[r_])%int(self.registers[r]))
   def compare (self, r, r_):
      diff = self.registers[r_] - self.registers[r]
      self.registers[r_] = -1.0 if diff<0.0 else \
                           +1.0 if diff>0.0 else 0.0
