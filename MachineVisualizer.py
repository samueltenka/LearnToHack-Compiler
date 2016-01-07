import tkinter as tk
import NumberedTextbox
import Machine

class MachineGUI:
    UPDATE_DELAY = 20 #ms
    def __init__(self, master, M):
        self.M = M

        self.controls_frame = tk.Frame(master, relief=tk.SUNKEN, background='black')
        self.lblRegs = tk.Label(self.controls_frame, text="Registers:", background='black',foreground='white')
        self.lblMemory = tk.Label(self.controls_frame, text="Memory:", background='black',foreground='white')

        self.on = False
        def turnon(): self.on=True
        def turnoff(): self.on=False
        self.btnRun = tk.Button(self.controls_frame, text="Run", background='black',foreground='white', command=turnon)
        self.btnStop = tk.Button(self.controls_frame, text="Stop", background='black',foreground='white', command=turnoff)

        self.lblRegs.pack()
        self.lblMemory.pack()
        self.btnRun.pack(side=tk.LEFT)
        self.btnStop.pack(side=tk.RIGHT)
        self.controls_frame.pack()

        self.pane = tk.PanedWindow(master, orient=tk.HORIZONTAL, opaqueresize=True)
        self.ed = NumberedTextbox.EditorClass(window)

        self.pane.add(self.ed.frame)
        self.pane.pack(fill='both', expand=1)

        self.step()
    def step(self):
        if self.on:
           print("woah!")
           #self.M.step()
           self.update()
        self.pane.after(self.__class__.UPDATE_DELAY, self.step)
    def update(self): # shows registers, and only first 8*4=32 el.s of memory
        self.lblRegs['text'] = "Registers:\t" + '\t'.join(str(r) for r in M.registers)
        self.lblMemory['text'] = "Memory:\n" + '\n'.join('\t'.join(str(a) for a in M.memory[8*i:8*i+8]) for i in range(4))

window = tk.Tk()
window.title("Machine")
window.geometry("640x480")
window.wm_iconbitmap("MH.ico")
window.configure(background='black')

M = Machine.Machine(num_registers=8, num_addresses=1024, debug=False)
MGUI = MachineGUI(window, M)
MGUI.update()

window.mainloop()
