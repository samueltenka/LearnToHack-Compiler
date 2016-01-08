import EnsureVersion3

def is_number(string):
   return string and (string[0] in '0123456789.')
def is_identifier(string):
   return string and (string[0] in 'abcdefghijklmnopqrstuvwxyz')

class Parser:
   def __init__(self, program_text):
      self.tokenized = program_text.split()
      self.index = 0
      self.variable_addresses = {'input':0, 'output':1}
      self.number_addresses = dict([])
      self.next_free_address = 3
      self.machine_code = []
   def peek(self):
      return self.tokenized[self.index]
   def match(self, token):
      assert(self.peek() == token)
      self.index += 1
   def at_end(self):
      return self.index >= len(self.tokenized)
   def gen_code(self,instr,a,r):
      self.machine_code.append(instr+' '+str(a)+' '+str(r))
   def use_next_free_address(self):
      nfa = self.next_free_address
      self.next_free_address += 1
      return nfa

   def match_number(self):
      num=float(self.peek())
      if num not in self.number_addresses:
         self.number_addresses[num] = self.use_next_free_address()
      self.gen_code('load',self.number_addresses[num],0)
      self.match(self.peek())
   def match_variable(self):
      var=self.peek()
      if var not in self.variable_addresses:
         self.variable_addresses[var] = self.use_next_free_address()
         self.next_free_address += 1
      self.gen_code('load',self.variable_addresses[var],0)
      self.match(self.peek())
   def match_factor(self):
      if is_number(self.peek()): self.match_number()
      elif is_identifier(self.peek()): self.match_identifier()
      else:
         temp1 = self.use_next_free_address()
         temp2 = self.use_next_free_address()
         self.gen_code('store',temp1,1)
         self.gen_code('store',temp2,2)
         self.match('(')
         self.match_expression()
         self.match(')')
         self.gen_code('load',temp1,1)
         self.gen_code('load',temp2,2)
   def match_term(self):
      self.match_factor()
      while not self.at_end() and self.peek() in ['*']:
         self.match('*')
         self.gen_code('swap',0,1)
         self.match_factor()
         self.gen_code('multiply',0,1)
   def match_expression(self):
      self.match_term()
      while not self.at_end() and self.peek() in ['+']:
         self.match('+')
         self.gen_code('swap',0,2)
         self.match_term()
         self.gen_code('add',0,2)
   def match_statement(self):
      pass
   def match_assignment(self):
      #self.match_variable() #generates unnecessary load statement
      var=self.peek(); assert(is_variable(var)); self.match(var)
      self.match('=')
      self.match_expression()
      self.gen_code('store',self.variable_addresses[var],0)
      #NOTE: notation easier to parse: expr->varname (assignment written backward)
   def match_if(self):
      self.match('if')
      self.match('(')
      self.match(')')
      self.match_statement()
   def match_while(self):
      pass
