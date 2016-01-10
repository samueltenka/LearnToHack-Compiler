class Parser:
   def __init__(self, text):
      self.toks = text.split()
      self.pos = 0
   def peek(self):
      return None if \
      self.pos>=len(self.toks) \
      else self.toks[self.pos]
   def init_stack(self):
       print('set 6 1.0')
       print('set 7 50.0') # TODO: ensure beyond program
   def store_state(self):
       print('store 7 0')
       print('add 6 7')
       print('store 7 1')
       print('add 6 7')
       print('store 7 2')
       print('add 6 7')
   def load_state(self):
       print('copy 0 3')
       print('sub 6 7')
       print('load 7 2')
       print('sub 6 7')
       print('load 7 1')
       print('sub 6 7')
       print('load 7 0')
       print('copy 3 0')
   def rec(self, tok):
      assert(self.peek()==tok)
      self.pos += 1
   def rec_atom(self):
      if self.peek() == '(':
         self.store_state()
         self.rec('(')
         self.rec_expr()
         self.rec(')')
         self.load_state()
      else:
         num = self.peek()
         print('set 0 '+num)
         self.rec(num)
   def rec_term(self):
      self.rec_atom()
      while self.peek() == '*':
         self.rec('*')
         print('copy 0 1')
         self.rec_atom()
         print('mul 1 0')
   def rec_expr(self):
      self.rec_term()
      while self.peek() == '+':
         self.rec('+')
         print('copy 0 2')
         self.rec_term()
         print('add 2 0')
   def rec_program(self):
       self.init_stack()
       self.rec_expr()

P = Parser('1.0 + 2.0 * 3.0 + 4.0 * ( 5.0 + 6.0 )')
P.rec_program()
