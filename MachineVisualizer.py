import tkinter as tk
import NumberedTextbox

class MachineGUI:
    def __init__(self, master):
        self.controls_frame = tk.Frame(master, relief=tk.SUNKEN, background='black')
        self.lblRegs = tk.Label(self.controls_frame, text="Registers:", background='black',foreground='white')
        self.lblMemory = tk.Label(self.controls_frame, text="Memory:", background='black',foreground='white')
        self.btnRun = tk.Button(self.controls_frame, text="Run", background='black',foreground='white')
        self.btnStop = tk.Button(self.controls_frame, text="Stop", background='black',foreground='white')

        self.lblRegs.pack()
        self.lblMemory.pack()
        self.btnRun.pack(side=tk.LEFT)
        self.btnStop.pack(side=tk.RIGHT)
        self.controls_frame.pack()

        self.pane = tk.PanedWindow(master, orient=tk.HORIZONTAL, opaqueresize=True)
        self.ed = NumberedTextbox.EditorClass(window)

        self.pane.add(self.ed.frame)
        self.pane.pack(fill='both', expand=1)
    def update_registers(self, registers):
        self.lblRegs['text'] = "Registers:\t" + '\t'.join(str(r) for r in registers)
    def update_memory(self, memory, l=16):
        self.lblMemory['text'] = "Memory:\t" + '  '.join(str(a) for a in memory[:l])


window = tk.Tk()
window.title("Machine")
window.geometry("640x480")
window.wm_iconbitmap("MH.ico")
window.configure(background='black')

MGUI = MachineGUI(window)
MGUI.update_registers([0.0]*8)

window.mainloop()
