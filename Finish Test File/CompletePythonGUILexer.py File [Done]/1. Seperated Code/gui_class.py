from tkinter import *
from tkinter import ttk
from token_parse import CutOneLineTokens, accept_token, multi, math, exp, if_exp, comparison_exp, print_exp, clear_treeview, parser

class MyFirstGUI:
    def __init__(self, root):
        self.master = root
        self.master.title("GUI: Delta Version 12.13")

        self.inputlabel = Label(self.master, text="Source Code Input:")
        self.inputlabel.grid(row=0, column=0, sticky=W)

        self.outputlabel = Label(self.master, text="Token Output:")
        self.outputlabel.grid(row=0, column=2, sticky=W)

        self.parselabel = Label(self.master, text="Parse Tree:")
        self.parselabel.grid(row=0, column=4, sticky=W)

        self.visualizationtreelabel = Label(self.master, text=" Treeview(hierarchical)")
        self.visualizationtreelabel.grid(row=2, column=2, sticky=W)

        self.currentlabel = Label(self.master, text="Current Processing Line:")
        self.currentlabel.grid(row=4, column=0, sticky=W)

        self.copyinput = Text(self.master, width=55, height=30)
        self.copyinput.grid(row=1, column=0, columnspan=2, sticky=E)

        self.pasteoutput = Text(self.master, width=40, height=30)
        self.pasteoutput.grid(row=1, column=2, columnspan=2, sticky=E)

        self.currentoutput = Entry(self.master)
        self.currentoutput.grid(row=4, column=1, sticky=E)

        self.parseoutput = Text(self.master, width=55, height=30)
        self.parseoutput.grid(row=1, column=4, columnspan=2, sticky=E)

        self.visualizationtreeoutput = ttk.Treeview(self.master)
        self.visualizationtreeoutput.grid(row=3, column=2, sticky=E)

        self.nextline = Button(self.master, text="Next Line", command=self.NextLine)
        self.nextline.grid(row=5, column=0, sticky=W)

        self.quitbutton = Button(self.master, text="Quit", command=self.QuitProgram)
        self.quitbutton.grid(row=5, column=3, columnspan=3, sticky=E)

        self.counter = 0
        self.Mytokens = []
        self.inToken = ("empty", "empty")

    def NextLine(self):
        clear_treeview(self)
        getuserinput = self.copyinput.get("1.0", "end-1c")
        lines = getuserinput.split('\n')

        if self.counter < len(lines):
            currentlines = lines[self.counter]
            self.pasteoutput.insert("end", f"--------------------Below is case--------------------\n{currentlines}\n\n")
            gettokenlist = CutOneLineTokens(self, currentlines)

            if gettokenlist:
                self.pasteoutput.insert("end", "\n\n".join(gettokenlist) + "\n\n")
                self.currentoutput.delete(0, "end")
                self.counter += 1
                self.currentoutput.insert(0, self.counter)
                parser(self)
            else:
                print("The list is empty")
        else:
            print("Working Progress on the error")

    def QuitProgram(self):
        self.master.destroy()
        self.master.quit()
