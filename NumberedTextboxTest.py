'''
Thanks to Robert@pytrash (see link below)
http://tk.unpythonic.net/wiki/A_Text_Widget_with_Line_Numbers
'''

import tkinter as tk
import NumberedTextbox

root = tk.Tk()

def demo(noOfLines):
    pane = tk.PanedWindow(root, orient=tk.HORIZONTAL, opaqueresize=True)
    ed = NumberedTextbox.EditorClass(root)
    pane.add(ed.frame)
    s = 'line %s'
    s = '\n'.join( s%i for i in range(3, noOfLines+3) )
    ed.text.insert(tk.END, s)
    pane.pack(fill='both', expand=1)
    root.title("Example - Line Numbers For Text Widgets")

if __name__ == '__main__':
    demo(9)
    tk.mainloop()
