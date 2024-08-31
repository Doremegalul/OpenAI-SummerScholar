# Python Library
import re
from tkinter import *
from tkinter import ttk  

# -= class definition =-
class MyFirstGUI: 

    # -= Function Description: =-
    # This is the main GUI interface with titles, entry, buttons, and global variables
    def __init__(self, root):
        self.setup_gui(root)
        self.setup_entries()
        self.setup_buttons()
        self.setup_globals()

    def setup_gui(self, root):
        self.master = root
        self.master.title("GUI: Delta Version 12.13")

        self.inputlabel = Label(self.master, text="Source Code Input: ")
        self.inputlabel.grid(row=0, column=0, sticky=W)

        self.outputlabel = Label(self.master, text="Token Output: ")
        self.outputlabel.grid(row=0, column=2, sticky=W)

        self.parselabel = Label(self.master, text="Parse Tree: ")
        self.parselabel.grid(row=0, column=4, sticky=W)

        self.visualizationtreelabel = Label(self.master, text=" Treeview(hierarchical)")
        self.visualizationtreelabel.grid(row=2, column=2, sticky=W)

        self.currentlabel = Label(self.master, text="Current Processing Line: ")
        self.currentlabel.grid(row=4, column=0, sticky=W)

    def setup_entries(self):
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

    def setup_buttons(self):
        self.nextline = Button(self.master, text="Next Line", command=self.NextLine)
        self.nextline.grid(row=5, column=0, sticky=W)

        self.quitbutton = Button(self.master, text="Quit", command=self.QuitProgram)
        self.quitbutton.grid(row=5, column=3, columnspan=3, sticky=E)

    def setup_globals(self):
        self.counter = 0
        self.Mytokens = []
        self.inToken = ("empty", "empty")

    def NextLine(self):
        self.clear_treeview()
        getuserinput = self.copyinput.get("1.0", "end-1c")
        lines = getuserinput.split('\n')

        if self.counter < len(lines):
            currentlines = lines[self.counter]
            self.pasteoutput.insert("end", f"--------------------Below is case--------------------\n{currentlines}\n\n")
            gettokenlist = self.CutOneLineTokens(currentlines)

            if gettokenlist:
                self.pasteoutput.insert("end", "\n\n".join(gettokenlist) + "\n\n")
                self.currentoutput.delete(0, "end")
                self.counter += 1
                self.currentoutput.insert(0, self.counter)
                self.parser()
            else:
                print("The list is empty")
        else:
            print("Working Progress on the error")

    def QuitProgram(self):
        self.master.destroy()
        self.master.quit()

    def CutOneLineTokens(self, testStr):
        tokenList = []

        tokenPatterns = [
            (r'"(.*?)"', 'lit_string'),
            (r'\b(if)?(else)?(float)?(int)?(while)?\b', 'key'),
            (r'(\=)?(\+)?(\>)?(\*)?', 'op'),
            (r'(\(|\)|:|"|;|<|>)', 'sep'),
            (r'\d+\.\d+', 'lit_float'),
            (r'\b\d+\b', 'lit_int'),
            (r'[a-zA-Z]+[a-zA-Z0-9]', 'id')
        ]

        while testStr:
            for num, (pattern, token_type) in enumerate(tokenPatterns):
                testStr = testStr.strip()
                matchToken = re.match(pattern, testStr)
                if matchToken:
                    resultMatchToken = matchToken.group()
                    if resultMatchToken:
                        if token_type == 'lit_string':
                            quote = resultMatchToken[1:-1]
                            quote = quote.strip()
                            tokenList.extend(['<sep,">', f'<{token_type},{quote}>', '<sep,">'])
                        else:
                            tokenList.append(f'<{token_type},{resultMatchToken}>')
                    testStr = testStr.replace(matchToken.group(), "", 1)

            if testStr == "":
                break

        temp_Mytokens = []
        for token_string in tokenList:
            type_value = token_string.strip('<>').split(',')
            if len(type_value) == 2:
                temp_Mytokens.append((type_value[0], type_value[1]))

        self.Mytokens = temp_Mytokens

        print("Printing the list of Mytokens: ", self.Mytokens)
        print("Printing the list of tokenList: ", tokenList)

        return tokenList

    def accept_token(self):
        if self.Mytokens:
            print("     accept token from the list:" + self.inToken[1])
            self.parseoutput.insert("end", "     accept token from the list:" + self.inToken[1] + "\n")
            self.inToken = self.Mytokens.pop(0)
        else:
            self.parseoutput.insert("end", "\n")
            return

    def multi(self, token_node_id):
        print("----parent node multi, finding children nodes: " + "\n")
        self.parseoutput.insert("end", "\n" + "----parent node multi, finding children nodes: " + "\n")

        if self.inToken[0] == "lit_int":
            self.process_lit_int(token_node_id)
        elif self.inToken[0] == "lit_float":
            self.process_lit_float(token_node_id)

        if self.inToken[1] == "*":
            self.process_op(token_node_id)

    def process_lit_int(self, token_node_id):
        print("child node (internal): int")
        self.parseoutput.insert("end", "child node (internal): int" + "\n")
        print("   int has child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "   int has child node (token):" + self.inToken[1] + "\n")

        sub_token_node_id = token_node_id + 'levelA-4-1'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text='int')

        under_sub_token_node_id = sub_token_node_id + 'levelA-5-1'
        self.visualizationtreeoutput.insert(sub_token_node_id, 'end', under_sub_token_node_id, text=self.inToken[1])

        self.accept_token()

    def process_lit_float(self, token_node_id):
        print("child node (internal): float")
        self.parseoutput.insert("end", "child node (internal): float" + "\n")
        print("   float has child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "   float has child node (token):" + self.inToken[1] + "\n")

        sub_token_node_id = token_node_id + 'levelA-4-5'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text='float')

        under_sub_token_node_id = sub_token_node_id + 'levelA-5-4'
        self.visualizationtreeoutput.insert(sub_token_node_id, 'end', under_sub_token_node_id, text=self.inToken[1])

        self.accept_token()

    def process_op(self, token_node_id):
        print("child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "child node (token):" + self.inToken[1] + "\n")
        sub_token_node_id = token_node_id + 'levelA-4-2'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text='op')

        under_sub_token_node_id = sub_token_node_id + 'levelA-5-2'
        self.visualizationtreeoutput.insert(sub_token_node_id, 'end', under_sub_token_node_id, text=self.inToken[1])

        self.accept_token()
        if self.inToken[0] == "lit_float":
            self.process_lit_float(token_node_id)

    def math(self):
        print("\n----parent node math, finding children nodes:")
        self.parseoutput.insert("end", "\n" + "----parent node math, finding children nodes:" + "\n")

        key_node_id = 'levelA-2-4'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='math')

        if self.inToken[0] == "lit_int" or self.inToken[0] == "lit_float":
            self.process_math(key_node_id)
        else:
            print("error, math expects float or int")
            self.parseoutput.insert("end", "error, math expects float or int" + "\n")

    def process_math(self, key_node_id):
        print("child node (internal): multi")
        self.parseoutput.insert("end", "child node (internal): multi" + "\n")

        token_node_id = key_node_id + '_' + 'levelA-3-1'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='multi')

        self.multi(token_node_id)
        self.process_math_continuation(key_node_id)

    def process_math_continuation(self, key_node_id):
        if self.inToken[0] == "lit_int":
            self.process_lit_int(key_node_id)
        if self.inToken[0] == "lit_float":
            self.process_lit_float(key_node_id)

        if self.inToken[1] == "+":
            self.process_op_plus(key_node_id)
        else:
            print("error, you need + after the int in the math")
            self.parseoutput.insert("end", "error, you need + after the int in the math" + "\n")

    def process_op_plus(self, key_node_id):
        print("\n----parent node math, finding children nodes:")
        self.parseoutput.insert("end", "\n" + "----parent node math, finding children nodes:" + "\n")
        print("   op has child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "   op has child node (token):" + self.inToken[1] + "\n")

        token_node_id = key_node_id + '_' + 'levelB-3-2'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='op')
        sub_token_node_id = token_node_id + 'levelB-4-2'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=self.inToken[1])

        self.accept_token()

        print("\n----parent node math, finding children nodes:")
        self.parseoutput.insert("end", "\n" + "----parent node math, finding children nodes:" + "\n")
        print("child node (internal): multi")
        self.parseoutput.insert("end", "child node (internal): multi" + "\n")

        token_node_id = key_node_id + '_' + 'levelB-3-3'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='multi')

        self.multi(token_node_id)

    def exp(self):
        print("\n----parent node exp, finding children nodes:")
        self.parseoutput.insert("end", "----parent node exp, finding children nodes: " + "\n")

        typeT, token = self.inToken
        if_token = token
        print_token = token

        self.visualizationtreeoutput.insert('', 'end', 'level1', text="exp")

        if token == "if":
            self.process_if_exp()
        elif token == "print":
            self.process_print_exp()
        elif typeT == "key":
            self.process_key_exp(token)
        elif typeT == "id":
            self.process_id_exp(token)
        else:
            self.process_invalid_exp()

    def process_if_exp(self):
        print("child node (internal): key")
        self.parseoutput.insert("end", "child node (internal): key" + "\n")
        print("   key has child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "   key has child node (token): " + self.inToken[1] + "\n")

        key_node_id = 'levelC-2-1'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='key')

        token_node_id = key_node_id + '_' + 'levelC-3-1'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=self.inToken[1])

        self.accept_token()

        print("child node (internal): if_exp")
        self.parseoutput.insert("end", "child node (internal): if_exp" + "\n")
        self.if_exp()

    def process_print_exp(self):
        print("child node (internal): id")
        self.parseoutput.insert("end", "child node (internal): id" + "\n")
        print("   key has child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "   key has child node (token): " + self.inToken[1] + "\n\n")

        key_node_id = 'levelD-2-1'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='id')

        token_node_id = key_node_id + '_' + 'levelD-3-1'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=self.inToken[1])

        self.accept_token()

        print("child node (internal): print_exp")
        self.parseoutput.insert("end", "child node (internal): print_exp" + "\n")
        self.print_exp()

    def process_key_exp(self, token):
        print("child node (internal): key")
        self.parseoutput.insert("end", "child node (internal): key" + "\n")
        print("   key has child node (token):" + token)
        self.parseoutput.insert("end", "   key has child node (token): " + token + "\n")

        key_node_id = 'levelA-2-1'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='key')

        token_node_id = key_node_id + '_' + token
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=token)

        self.accept_token()

    def process_id_exp(self, token):
        print("child node (internal): identifier")
        self.parseoutput.insert("end", "\nchild node (internal): identifier" + "\n")
        print("   identifier has child node (token):" + token)
        self.parseoutput.insert("end", "   identifier has child node (token): " + token + "\n")
        self.accept_token()

    def process_invalid_exp(self):
        print("expect identifier as the first element of the expression!\n")
        self.parseoutput.insert("end", "expect identifier as the first element of the expression!" + "\n")
        return

    def if_exp(self):
        print("\n----parent node if_exp, finding children nodes:")
        self.parseoutput.insert("end", "\n" + "----parent node if_exp, finding children nodes: " + "\n")

        key_node_id = 'levelC-2-2'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='if_exp')

        self.process_if_exp_key()

        self.comparison_exp()

        self.process_if_exp_continuation(key_node_id)

    def process_if_exp_key(self):
        typeT, token = self.inToken
        if typeT == "key":
            print("child node (internal): key")
            self.parseoutput.insert("end", "child node (internal): key" + "\n")
            print("   key has child node (token):" + token)
            self.parseoutput.insert("end", "   key has child node (token): " + token + "\n")
            self.accept_token()

    def process_if_exp_continuation(self, key_node_id):
        print("\n----parent node if_exp, finding children nodes:")
        self.parseoutput.insert("end", "\n" + "----parent node if_exp, finding children nodes: " + "\n")

        self.process_if_exp_separator(key_node_id, 'levelC-3-6', 'levelC-4-5')

        self.process_if_exp_separator(key_node_id, 'levelC-3-7', 'levelC-4-6')

    def process_if_exp_separator(self, key_node_id, token_node_id_suffix, sub_token_node_id_suffix):
        typeT, token = self.inToken
        if typeT == "sep":
            print("child node (internal): separator")
            self.parseoutput.insert("end", "child node (internal): separator" + "\n")
            print("   separator has child node (token):" + token)
            self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

            token_node_id = key_node_id + '_' + token_node_id_suffix
            self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

            sub_token_node_id = token_node_id + sub_token_node_id_suffix
            self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

            self.accept_token()

    def comparison_exp(self):
        print("\n----parent node comparison_exp, finding children nodes:")
        self.parseoutput.insert("end", "\n" + "----parent node comparison_exp, finding children nodes: " + "\n")

        key_node_id = 'levelB-3-3'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='comparison_exp')

        self.process_comparison_exp_id(key_node_id)

        self.process_comparison_exp_op(key_node_id)

        self.process_comparison_exp_id(key_node_id)

    def process_comparison_exp_id(self, key_node_id):
        typeT, token = self.inToken
        if typeT == "id":
            print("child node (internal): identifier")
            self.parseoutput.insert("end", "child node (internal): identifier" + "\n")
            print("   identifier has child node (token):" + token)
            self.parseoutput.insert("end", "   identifier has child node (token): " + token + "\n")

            token_node_id = key_node_id + '_' + 'levelC-3-3'
            self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text="id")

            sub_token_node_id = token_node_id + 'levelC-4-2'
            self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

            self.accept_token()

    def process_comparison_exp_op(self, key_node_id):
        typeT, token = self.inToken
        if typeT == "op":
            print("child node (internal): operator")
            self.parseoutput.insert("end", "child node (internal): operator" + "\n")
            print("   operator has child node (token):" + token)
            self.parseoutput.insert("end", "   operator has child node (token): " + token + "\n")

            token_node_id = key_node_id + '_' + 'levelC-3-4'
            self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text="op")

            sub_token_node_id = token_node_id + 'levelC-4-3'
            self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=">")

            self.accept_token()

    def print_exp(self):
        print("\n----parent node print_exp, finding children nodes:")
        self.parseoutput.insert("end", "----parent node print_exp, finding children nodes: " + "\n")

        key_node_id = 'levelD-2-2'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='print_exp')

        self.process_print_exp_separator(key_node_id, 'levelD-3-2', 'levelD-4-1')
        self.process_print_exp_separator(key_node_id, 'levelD-3-3', 'levelD-4-2')

        self.process_print_exp_string_literal(key_node_id)

        self.process_print_exp_separator(key_node_id, 'levelD-3-5', 'levelD-4-4')
        self.process_print_exp_separator(key_node_id, 'levelD-3-6', 'levelD-4-5')

    def process_print_exp_separator(self, key_node_id, token_node_id_suffix, sub_token_node_id_suffix):
        typeT, token = self.inToken
        if typeT == "sep":
            print("child node (internal): separator")
            self.parseoutput.insert("end", "child node (internal): separator" + "\n")
            print("   separator has child node (token):" + token)
            self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

            token_node_id = key_node_id + '_' + token_node_id_suffix
            self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

            sub_token_node_id = token_node_id + sub_token_node_id_suffix
            self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

            self.accept_token()

    def process_print_exp_string_literal(self, key_node_id):
        typeT, token = self.inToken
        if typeT == "lit_string":
            print("child node (internal): string_literal")
            self.parseoutput.insert("end", "child node (internal): string_literal" + "\n")
            print("   string_literal has child node (token):" + token)
            self.parseoutput.insert("end", "   string_literal has child node (token): " + token + "\n")

            token_node_id = key_node_id + '_' + 'levelD-3-4'
            self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='string_literal')

            sub_token_node_id = token_node_id + 'levelD-4-3'
            self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

            self.accept_token()

    def clear_treeview(self):
        for item in self.visualizationtreeoutput.get_children():
            self.visualizationtreeoutput.delete(item)

    def parser(self):
        self.parseoutput.insert("end", f"--------------------Below is case--------------------\n{self.Mytokens}\n\n")
        self.inToken = self.Mytokens.pop(0)
        self.exp()
        if self.inToken[1] == ";":
            print("\nparse tree building success!")
            self.parseoutput.insert("end", "\n" + "parse tree building success!" + "\n\n")

if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()
