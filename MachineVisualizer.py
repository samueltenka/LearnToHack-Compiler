import tkinter as tk
import NumberedTextbox
import Machine
import PrettyPrint

class MachineGUI:
    UPDATE_DELAY = 20 #ms
    def __init__(self, master, M):
        self.M = M

        self.controls_frame = tk.Frame(master, relief=tk.SUNKEN, background='black')
        self.lblRegs = tk.Label(self.controls_frame, text="Registers:", background='black',foreground='white',font = ("Courier",8))
        self.lblMemory = tk.Label(self.controls_frame, text="Memory:", background='black',foreground='white',
                                  font = ("Courier",8))
        self.lblCounts = tk.Label(self.controls_frame, text="[][]", background='black',foreground='white',
                          font = ("Courier",8))
        self.ent = tk.Entry(self.controls_frame, text='9.0', background='grey',foreground='white')
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
        self.ent.pack()
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
        self.M.execution=3
        #TODO: remove comments from program
        lines = self.ed.text.get('0.0',tk.END).split('\n')
        lines = [l.split('#')[0].strip() for l in lines]
        lines = [l for l in lines if l]
        M.load_program(lines, float(self.ent.get()))
    def turnoff(self):
        self.on=False

    def step(self):
        if self.on:
           #print("woah!")
           self.M.step()
           if M.execution == -1:
               self.on = False
           self.instr_count += 1
           self.update()
        self.pane.after(self.__class__.UPDATE_DELAY, self.step)
    def update(self): # shows registers, and only first 8*8=64 el.s of memory
        self.lblRegs['text'] = "Registers:\t" + ''.join(PrettyPrint.pretty_print(r, minlen=8) for r in M.registers)
        self.lblMemory['text'] = "Memory:\n" + \
           '\n'.join(''.join(PrettyPrint.pretty_print(a, minlen=10) for a in M.memory[8*i:8*i+8]) for i in range(8))
        self.lblCounts['text'] = '[%d instructions so far] [about to execute address %s]' % (self.instr_count,self.M.execution)
        self.lblOut['text'] = str(self.M.memory[2])

window = tk.Tk()
window.title("Machine")
window.geometry("640x480")
window.wm_iconbitmap("MH.ico")
window.configure(background='black')

M = Machine.Machine(num_registers=8, num_addresses=64, debug=False)
MGUI = MachineGUI(window, M)
MGUI.update()

window.mainloop()
