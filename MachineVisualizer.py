import tkinter
window = tkinter.Tk()
window.title("Machine")
window.geometry("640x480")
window.wm_iconbitmap("MH.ico")

lblRegs = tkinter.Label(window, text="Registers: ")
lblMemory = tkinter.Label(window, text="Memory: ")
btnRun = tkinter.Button(window, text="Run")
btnStop = tkinter.Button(window, text="Stop")
entProgram = tkinter.Entry(window, text="<enter program here>")

lblRegs.pack()
lblMemory.pack()
btnRun.pack()
btnStop.pack()
entProgram.pack()

window.mainloop()
