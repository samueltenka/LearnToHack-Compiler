import tkinter as tk
import NumberedTextbox
import Machine
import PrettyPrint as PP

class MachineGUI:
    UPDATE_DELAY = 50 #ms
    def __init__(self, master, M):
        self.M = M

        self.controls_frame = tk.Frame(master, relief=tk.SUNKEN, background='black')
        self.lblRegs = tk.Label(self.controls_frame, text="Registers:", background='black',foreground='white',font = ("Courier",8))
        self.lblMemory = tk.Label(self.controls_frame, text="Memory:", background='black',foreground='white',
           font = ("Courier",8))
        self.lblCounts = tk.Label(self.controls_frame, text="[][]", background='black',foreground='white',
           font = ("Courier",8))
        self.ents = [tk.Entry(self.controls_frame, background='grey',foreground='white') for i in range(2)]
        self.lblOut = tk.Label(self.controls_frame, text="[][]", background='black',foreground='white',
                  font = ("Courier",8))

        self.on = False
        self.instr_count = 0
        self.btnRun = tk.Button(self.controls_frame, text="Run", background='black',foreground='white', command=self.turnon)
        self.btnStop = tk.Button(self.controls_frame, text="Stop", background='black',foreground='white', command=self.turnoff)

        self.lblRegs.pack()
        self.lblMemory.pack()
        self.lblCounts.pack()
        self.btnRun.pack(side=tk.LEFT)
        for e in self.ents: e.pack()
        self.lblOut.pack()
        self.btnStop.pack(side=tk.RIGHT)
        self.controls_frame.pack()

        self.pane = tk.PanedWindow(master, orient=tk.HORIZONTAL, opaqueresize=True)
        self.ed = NumberedTextbox.EditorClass(window)

        self.pane.add(self.ed.frame)
        self.pane.pack(fill='both', expand=1)

        self.step()

    def turnon(self):
        self.on=True
        self.instr_count = 0
        self.M.program_counter=4
        lines = self.ed.text.get('0.0',tk.END).split('\n')
        lines = [l.split('#')[0].strip() for l in lines]
        lines = [l for l in lines if l]
        inputs = [e.get() for e in self.ents]
        M.load_program(lines, [0.0,0.0] if inputs==['',''] else [eval(i) for i in inputs])
    def turnoff(self):
        self.on=False

    def step(self):
        if self.on:
           self.M.step()
           self.instr_count += 1
           self.render()
           if M.at_end(): self.turnoff()
        self.pane.after(self.__class__.UPDATE_DELAY, self.step)
    def render(self, octas_of_memory=8):
        self.lblRegs['text'] = "Registers:\t" + ''.join(PP.pretty_print(r, minlen=8) for r in M.registers)
        self.lblMemory['text'] = "Memory:\n" + \
           '\n'.join(''.join(PP.pretty_print(a, minlen=10) for a in M.memory[8*i:8*i+8]) for i in range(octas_of_memory))
        self.lblCounts['text'] = '[%d instructions so far] [about to execute address %s]' % (self.instr_count,self.M.program_counter)
        self.lblOut['text'] = str(self.M.memory[2:4])

window = tk.Tk()
window.title("Machine")
window.geometry("640x480")
window.wm_iconbitmap("MH.ico")
window.configure(background='black')

M = Machine.Machine(num_registers=8, num_addresses=64)
MGUI = MachineGUI(window, M)
MGUI.render()

window.mainloop()
