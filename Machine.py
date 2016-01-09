#Michigan Hackers Presentation on Compilers
import EnsureVersion3

'''
instructions:
load	    A B	  R[B] <-- M[R[A]]
store	    A B	  R[B] --> M[R[A]]
copy		A B	  R[B] <--  R[A]
set		    A B	    B  -->  R[A]
branchif0	A B	   PC  <--   R[A] if R[B]==0
branchifneg	A B	   PC  <--   R[A] if R[B] < 0
jump		A B	   PC  <--   R[A] (so B is dummy var.)
add		    A B	  R[B] <-- R[B] + R[A]
sub		    A B	  R[B] <-- R[B] - R[A]
mul		    A B	  R[B] <-- R[B] * R[A]
div		    A B	  R[B] <-- R[B] / R[A]
mod		    A B	  R[B] <-- R[B] % R[A]
Note: program might also contain literal numbers in addition to instructions.
Machine halts when program counter reaches -1.

Machine Specifics:
Each memory address contains a float or program instruction.
Floats are rounded to integers when interpreted as addresses.
The program counter starts at 4.
The first 4 memory addresses are IO devices:
0           [Input, e.g. temperature sensor]
1           [Input, e.g. joystick]
2           [Output, e.g. LED]
3           [Output, e.g. motor]
4&beyond    [Program then data]
'''

class Machine:
   PRECISION = 0.0001
   def __init__(self, num_addresses, num_registers):
      self.memory = [0.0 for i in range(num_addresses)]
      self.registers = [0.0 for i in range(num_registers)]
      self.program_counter = None
   def load_program(self, lines, inputs=(0.0,0.0)):
       self.memory[:2] = inputs
       for i in range(len(lines)):
           self.memory[4+i] = lines[i] if ' ' in lines[i] else eval(lines[i])
       self.program_counter = 4
   def print_mem(self, l=8):
      print('memory', ' '.join(str(s).replace(' ','_') for s in self.memory[:l])+'. . .')
      print('registers', self.registers)
   def step(self):
      instr = self.memory[self.program_counter]
      print("instr ", self.program_counter, instr)
      command, arg0, arg1 = instr.split(' ')
      getattr(self,command)(eval(arg0),eval(arg1))
      self.program_counter += 1
   def at_end(self):
       return self.program_counter == -1

   def load(self, r, r_): self.registers[r_] = self.memory[int(self.registers[r])]
   def store(self, r, r_): self.memory[int(self.registers[r])] = self.registers[r_]
   def copy(self, r, r_): self.registers[r_] = self.registers[r]
   def set(self, r, f): self.registers[r] = f

   def branchif0(self, r, r_):
       if self.registers[r_]==0.0: self.jump(r)
   def branchifneg(self, r, r_):
       if self.registers[r_] < 0.0: self.jump(r)
   def jump(self, r, dummy):
       #subtract 1 to counter end-of-cycle PC increment:
       self.program_counter = int(self.registers[r])-1

   def add (self, r, r_): self.registers[r_] += self.registers[r]
   def sub (self, r, r_): self.registers[r_] -= self.registers[r]
   def mul (self, r, r_): self.registers[r_] *= self.registers[r]
   def div (self, r, r_): self.registers[r_] /= self.registers[r]
   def mod (self, r, r_): self.registers[r_] = self.registers[r_] % self.registers[r]
   '''Beware of floating point modulo: 0.0 != 3.50 % 0.10 == 0.09999999999999992 != 0.10'''
