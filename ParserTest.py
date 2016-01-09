from Parser import Parser

program = '1 * ( 2 + 3 * 4 + 5 ) + 6 * 7'
P = Parser(program)
P.match_expression()
P.write_constants_table()
for mc in P.machine_code:
    print(mc)
