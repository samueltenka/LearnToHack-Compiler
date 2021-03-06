'''
Thanks to Robert@pytrash (see link below)
http://tkinter.unpythonic.net/wiki/A_Text_Widget_with_Line_Numbers
'''

from tkinter import *

root = Tk()

class EditorClass(object):
    UPDATE_PERIOD = 30 #ms
    editors = []
    updateId = None
    def __init__(self, master):
        self.__class__.editors.append(self)
        self.lineNumbers = ''
        # A frame to hold the three components of the widget.
        self.frame = Frame(master, bd=2, relief=SUNKEN)
        # The widgets vertical scrollbar
        self.vScrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.vScrollbar.pack(fill='y', side=RIGHT)
        # The Text widget holding the line numbers.
        self.lnText = Text(self.frame,
                width = 4,
                padx = 4,
                highlightthickness = 0,
                takefocus = 0,
                bd = 0,
                background = 'black',
                foreground = 'grey',
                state='disabled'
        )
        self.lnText.pack(side=LEFT, fill='y')
        # The Main Text Widget
        self.text = Text(self.frame,
                undo=True,
                foreground='white',
                insertbackground='green',
                background = 'black'
        )
        self.text.pack(side=LEFT, fill=BOTH, expand=1)
        self.text.config(yscrollcommand=self.vScrollbar.set)
        self.vScrollbar.config(command=self.text.yview)
        if self.__class__.updateId is None:
            self.updateAllLineNumbers()

    def getLineNumbers(self):
        line = '2'
        col= ''
        ln = ''
        # assume each line is at least 6 pixels high
        step = 6
        nl = '\n'
        lineMask = '    %s\n'
        indexMask = '@0,%d'
        for i in range(0, self.text.winfo_height(), step):
            ll, cc = self.text.index( indexMask % i).split('.')
            print(ll,cc)
            ll = str(2+int(ll))
            if line == ll:
                if col != cc:
                    col = cc
                    ln += nl
            else:
                line, col = ll, cc
                ln += (lineMask % line)[-5:]
        return ln
    def updateLineNumbers(self):
        tt = self.lnText
        ln = self.getLineNumbers()
        if self.lineNumbers != ln:
            self.lineNumbers = ln
            tt.config(state='normal')
            tt.delete('1.0', END)
            tt.insert('1.0', self.lineNumbers)
            tt.config(state='disabled')
    @classmethod
    def updateAllLineNumbers(cls):
        if len(cls.editors) < 1:
            cls.updateId = None
            return
        for ed in cls.editors:
            ed.updateLineNumbers()
        cls.updateId = ed.text.after(
            cls.UPDATE_PERIOD,
            cls.updateAllLineNumbers)


def demo(noOfEditors, noOfLines):
    pane = PanedWindow(root, orient=HORIZONTAL, opaqueresize=True)
    for e in range(noOfEditors):
        ed = EditorClass(root)
        pane.add(ed.frame)
    s = 'line %s'
    s = '\n'.join( s%i for i in range(1, noOfLines+1) )
    for ed in EditorClass.editors:
        ed.text.insert(END, s)
    pane.pack(fill='both', expand=1)
    root.title("Example - Line Numbers For Text Widgets")


if __name__ == '__main__':

    demo(1,9)
    mainloop()
