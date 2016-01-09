class Parser:
   def __init__(self, text):
      self.toks = text.split()
      self.pos = 0
   def peek(self):
      return None if \
      self.pos>=len(self.toks) \
      else self.toks[self.pos]
   def rec(self, tok):
      assert(self.peek()==tok)
      self.pos += 1
   def rec_atom(self):
      if self.peek() == '(':
         self.rec('(')
         self.rec_expr()
         self.rec(')')
         print('copy 2 0')
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
         print('mul 0 1')
   def rec_expr(self):
      self.rec_term()
      while self.peek() == '+':
         self.rec('+')
         print('copy 0 2')
         self.rec_term()
         print('add 0 2')

P = Parser('1.0 + 2.0 * 3.0 + 4.0 * ( 5.0 + 6.0 )')
P.rec_expr()
