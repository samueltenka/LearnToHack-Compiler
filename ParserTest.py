from Parser import Parser

program = '1 * ( 2 + 3 * 4 + 5 ) + 6 * 7'
P = Parser(program)
P.match_expression()
for mc in P.machine_code:
    print(mc)
