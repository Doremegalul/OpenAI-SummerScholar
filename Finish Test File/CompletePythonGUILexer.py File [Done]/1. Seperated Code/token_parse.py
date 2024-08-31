import re

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
        print("child node (internal): int")
        self.parseoutput.insert("end", "child node (internal): int" + "\n")
        print("   int has child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "   int has child node (token):" + self.inToken[1] + "\n")

        sub_token_node_id = token_node_id + 'levelA-4-1'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text='int')

        under_sub_token_node_id = sub_token_node_id + 'levelA-5-1'
        self.visualizationtreeoutput.insert(sub_token_node_id, 'end', under_sub_token_node_id, text=self.inToken[1])

        accept_token(self)

    elif self.inToken[0] == "lit_float":
        print("child node (internal): float")
        self.parseoutput.insert("end", "child node (internal): float" + "\n")
        print("   float has child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "   float has child node (token):" + self.inToken[1] + "\n")

        sub_token_node_id = token_node_id + 'levelA-4-5'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text='float')

        under_sub_token_node_id = sub_token_node_id + 'levelA-5-4'
        self.visualizationtreeoutput.insert(sub_token_node_id, 'end', under_sub_token_node_id, text=self.inToken[1])

        accept_token(self)

    if self.inToken[1] == "*":
        print("child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "child node (token):" + self.inToken[1] + "\n")
        sub_token_node_id = token_node_id + 'levelA-4-2'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text='op')

        under_sub_token_node_id = sub_token_node_id + 'levelA-5-2'
        self.visualizationtreeoutput.insert(sub_token_node_id, 'end', under_sub_token_node_id, text=self.inToken[1])

        accept_token(self)
        if self.inToken[0] == "lit_float":
            print("child node (internal): float")
            self.parseoutput.insert("end", "child node (internal): float" + "\n")
            print("   float has child node (token):" + self.inToken[1])
            self.parseoutput.insert("end", "   float has child node (token):" + self.inToken[1] + "\n")

            sub_token_node_id = token_node_id + 'levelA-4-3'
            self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text='float')

            under_sub_token_node_id = sub_token_node_id + 'levelA-5-3'
            self.visualizationtreeoutput.insert(sub_token_node_id, 'end', under_sub_token_node_id, text=self.inToken[1])
            accept_token(self)

def math(self):
    print("\n----parent node math, finding children nodes:")
    self.parseoutput.insert("end", "\n" + "----parent node math, finding children nodes:" + "\n")

    key_node_id = 'levelA-2-4'
    self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='math')

    if self.inToken[0] == "lit_int" or self.inToken[0] == "lit_float":
        print("child node (internal): multi")
        self.parseoutput.insert("end", "child node (internal): multi" + "\n")

        token_node_id = key_node_id + '_' + 'levelA-3-1'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='multi')

        multi(self, token_node_id)
        if self.inToken[0] == "lit_int":
            print("child node (internal): int")
            self.parseoutput.insert("end", "child node (internal): int" + "\n")
            print("   int has child node (token):" + self.inToken[1])
            self.parseoutput.insert("end", "   int has child node (token):" + self.inToken[1] + "\n")

            accept_token(self)

        if self.inToken[0] == "lit_float":
            print("child node (internal): float")
            self.parseoutput.insert("end", "child node (internal): float" + "\n")
            print("   float has child node (token):" + self.inToken[1])
            self.parseoutput.insert("end", "   float has child node (token):" + self.inToken[1] + "\n")

            accept_token(self)

        if self.inToken[1] == "+":
            print("\n----parent node math, finding children nodes:")
            self.parseoutput.insert("end", "\n" + "----parent node math, finding children nodes:" + "\n")
            print("   op has child node (token):" + self.inToken[1])
            self.parseoutput.insert("end", "   op has child node (token):" + self.inToken[1] + "\n")

            token_node_id = key_node_id + '_' + 'levelB-3-2'
            self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='op')
            sub_token_node_id = token_node_id + 'levelB-4-2'
            self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=self.inToken[1])

            accept_token(self)

            print("\n----parent node math, finding children nodes:")
            self.parseoutput.insert("end", "\n" + "----parent node math, finding children nodes:" + "\n")
            print("child node (internal): multi")
            self.parseoutput.insert("end", "child node (internal): multi" + "\n")

            token_node_id = key_node_id + '_' + 'levelB-3-3'
            self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='multi')

            multi(self, token_node_id)
        else:
            print("error, you need + after the int in the math")
            self.parseoutput.insert("end", "error, you need + after the int in the math" + "\n")
    else:
        print("error, math expects float or int")
        self.parseoutput.insert("end", "error, math expects float or int" + "\n")

def exp(self):
    print("\n----parent node exp, finding children nodes:")
    self.parseoutput.insert("end", "----parent node exp, finding children nodes: " + "\n")

    typeT, token = self.inToken
    if_token = token
    print_token = token

    self.visualizationtreeoutput.insert('', 'end', 'level1', text="exp")

    if token == "if":
        print("child node (internal): key")
        self.parseoutput.insert("end", "child node (internal): key" + "\n")
        print("   key has child node (token):" + token)
        self.parseoutput.insert("end", "   key has child node (token): " + token + "\n")

        key_node_id = 'levelC-2-1'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='key')

        token_node_id = key_node_id + '_' + 'levelC-3-1'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=token)

        accept_token(self)

        print("child node (internal): if_exp")
        self.parseoutput.insert("end", "child node (internal): if_exp" + "\n")

        print("child node (internal): comparision_exp")
        self.parseoutput.insert("end", "child node (internal): comparision_exp" + "\n")

        print("child node (internal): if_exp")
        self.parseoutput.insert("end", "child node (internal): if_exp" + "\n")

        if_exp(self)
    elif token == "print":
        print("child node (internal): id")
        self.parseoutput.insert("end", "child node (internal): id" + "\n")
        print("   key has child node (token):" + token)
        self.parseoutput.insert("end", "   key has child node (token): " + token + "\n\n")

        key_node_id = 'levelD-2-1'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='id')

        token_node_id = key_node_id + '_' + 'levelD-3-1'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=token)

        accept_token(self)

        print("child node (internal): print_exp")
        self.parseoutput.insert("end", "child node (internal): print_exp" + "\n")
        print_exp(self)

    elif typeT == "key":
        print("child node (internal): key")
        self.parseoutput.insert("end", "child node (internal): key" + "\n")
        print("   key has child node (token):" + token)
        self.parseoutput.insert("end", "   key has child node (token): " + token + "\n")

        key_node_id = 'levelA-2-1'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='key')

        token_node_id = key_node_id + '_' + token
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=token)

        accept_token(self)

    elif typeT == "id":
        print("child node (internal): identifier")
        self.parseoutput.insert("end", "\nchild node (internal): identifier" + "\n")
        print("   identifier has child node (token):" + token)
        self.parseoutput.insert("end", "   identifier has child node (token): " + token + "\n")
        accept_token(self)
    else:
        print("expect identifier as the first element of the expression!\n")
        self.parseoutput.insert("end", "expect identifier as the first element of the expression!" + "\n")
        return

    typeT, token = self.inToken
    if typeT == "id":
        print("child node (internal): identifier")
        self.parseoutput.insert("end", "child node (internal): identifier" + "\n")
        print("   identifier has child node (token):" + token)
        self.parseoutput.insert("end", "   identifier has child node (token): " + token + "\n")

        key_node_id = 'levelA-2-2'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='id')

        token_node_id = key_node_id + '_' + "levelA-2-2"
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=token)

        accept_token(self)

    if self.inToken[1] == "=":
        print("child node (token):" + self.inToken[1])
        self.parseoutput.insert("end", "child node (token):" + self.inToken[1] + "\n")

        key_node_id = 'levelA-2-3'
        self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='op')

        token_node_id = key_node_id + '_' + "levelA-3-2"
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text=self.inToken[1])

        accept_token(self)

        print("Child node (internal): math")
        self.parseoutput.insert("end", "Child node (internal): math" + "\n")
        math(self)

    elif if_token == "if":
        return

    elif print_token == "print":
        return

    else:
        print("expect = as the second element of the expression!")
        self.parseoutput.insert("end", "expect = as the second element of the expression!" + "\n")
        return

def if_exp(self):
    print("\n----parent node if_exp, finding children nodes:")
    self.parseoutput.insert("end", "\n" + "----parent node if_exp, finding children nodes: " + "\n")
    typeT, token = self.inToken

    key_node_id = 'levelC-2-2'
    self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='if_exp')

    if typeT == "key":
        print("child node (internal): key")
        self.parseoutput.insert("end", "child node (internal): key" + "\n")
        print("   key has child node (token):" + token)
        self.parseoutput.insert("end", "   key has child node (token): " + token + "\n")
        accept_token(self)

    typeT, token = self.inToken
    if typeT == "sep":
        print("child node (internal): separator")
        self.parseoutput.insert("end", "child node (internal): separator")
        print("   separator has child node (token):" + token + "\n")
        self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelC-3-2'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

        sub_token_node_id = token_node_id + 'levelC-4-1'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=self.inToken[1])

        accept_token(self)

    comparison_exp(self)

    print("\n----parent node if_exp, finding children nodes:")
    self.parseoutput.insert("end", "\n" + "----parent node if_exp, finding children nodes: " + "\n")

    key_node_id = 'levelC-4-4'
    self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='if_exp')

    typeT, token = self.inToken
    if typeT == "sep":
        print("child node (internal): separator")
        self.parseoutput.insert("end", "child node (internal): separator" + "\n")
        print("   separator has child node (token):" + token)
        self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelC-3-6'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

        sub_token_node_id = token_node_id + 'levelC-4-5'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=self.inToken[1])

        accept_token(self)

    typeT, token = self.inToken
    if typeT == "sep":
        print("child node (internal): separator")
        self.parseoutput.insert("end", "child node (internal): separator" + "\n")
        print("   separator has child node (token):" + token)
        self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelC-3-7'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

        sub_token_node_id = token_node_id + 'levelC-4-6'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=self.inToken[1])

        accept_token(self)

def comparison_exp(self):
    print("\n----parent node comparison_exp, finding children nodes:")
    self.parseoutput.insert("end", "\n" + "----parent node comparison_exp, finding children nodes: " + "\n")
    typeT, token = self.inToken

    key_node_id = 'levelB-3-3'
    self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='comparison_exp')

    if typeT == "id":
        print("child node (internal): identifier")
        self.parseoutput.insert("end", "child node (internal): identifier" + "\n")
        print("   identifier has child node (token):" + token)
        self.parseoutput.insert("end", "   identifier has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelC-3-3'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text="id")

        sub_token_node_id = token_node_id + 'levelC-4-2'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

        accept_token(self)

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

        accept_token(self)

    typeT, token = self.inToken
    if typeT == "id":
        print("child node (internal): identifier")
        self.parseoutput.insert("end", "child node (internal): identifier" + "\n")
        print("   identifier has child node (token):" + token)
        self.parseoutput.insert("end", "   identifier has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelC-3-5'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text="id")

        sub_token_node_id = token_node_id + 'levelC-4-4'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

        accept_token(self)

def print_exp(self):
    print("\n----parent node print_exp, finding children nodes:")
    self.parseoutput.insert("end", "----parent node print_exp, finding children nodes: " + "\n")

    key_node_id = 'levelD-2-2'
    self.visualizationtreeoutput.insert('level1', 'end', key_node_id, text='print_exp')

    typeT, token = self.inToken
    if typeT == "sep":
        print("child node (internal): separator")
        self.parseoutput.insert("end", "child node (internal): separator" + "\n")
        print("   separator has child node (token):" + token)
        self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelD-3-2'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

        sub_token_node_id = token_node_id + 'levelD-4-1'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

        accept_token(self)

    typeT, token = self.inToken
    if typeT == "sep":
        print("child node (internal): separator")
        self.parseoutput.insert("end", "child node (internal): separator")
        print("   separator has child node (token):" + token)
        self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelD-3-3'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

        sub_token_node_id = token_node_id + 'levelD-4-2'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

        accept_token(self)

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

        accept_token(self)

    typeT, token = self.inToken
    if typeT == "sep":
        print("child node (internal): separator")
        self.parseoutput.insert("end", "child node (internal): separator" + "\n")
        print("   separator has child node (token):" + token)
        self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelD-3-5'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

        sub_token_node_id = token_node_id + 'levelD-4-4'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

        accept_token(self)

    typeT, token = self.inToken
    if typeT == "sep":
        print("child node (internal): separator")
        self.parseoutput.insert("end", "child node (internal): separator" + "\n")
        print("   separator has child node (token):" + token)
        self.parseoutput.insert("end", "   separator has child node (token): " + token + "\n")

        token_node_id = key_node_id + '_' + 'levelD-3-6'
        self.visualizationtreeoutput.insert(key_node_id, 'end', token_node_id, text='sep')

        sub_token_node_id = token_node_id + 'levelD-4-5'
        self.visualizationtreeoutput.insert(token_node_id, 'end', sub_token_node_id, text=token)

        accept_token(self)

def clear_treeview(self):
    for item in self.visualizationtreeoutput.get_children():
        self.visualizationtreeoutput.delete(item)

def parser(self):
    self.parseoutput.insert("end", f"--------------------Below is case--------------------\n{self.Mytokens}\n\n")

    self.inToken = self.Mytokens.pop(0)
    exp(self)
    if self.inToken[1] == ";":
        print("\nparse tree building success!")
        self.parseoutput.insert("end", "\n" + "parse tree building success!" + "\n\n")
