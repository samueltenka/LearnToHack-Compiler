import Machine

def readfile(filename):
    with open(filename,'r') as f:
        return f.read()

lines = readfile('MachineCode01.test').strip().split('\n')
lines = [l.split('#')[0].strip() for l in lines] #remove line-comments such as this one
print(lines)
num_registers, num_addresses = lines[0].split()
M = Machine.Machine(eval(num_registers), eval(num_addresses), debug=False)
M.print_mem()
M.load_program(lines[2:], float(input()))
M.run()
