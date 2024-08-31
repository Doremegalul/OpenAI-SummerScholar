import re

def tokenize_line(self, line):
    tokens = []

    token_patterns = [
        (r'"(.*?)"', 'lit_string'),
        (r'\b(if|else|float|int|while)\b', 'key'),
        (r'(\=|\+|\>|\*)', 'op'),
        (r'(\(|\)|:|"|;|<|>)', 'sep'),
        (r'\d+\.\d+', 'lit_float'),
        (r'\b\d+\b', 'lit_int'),
        (r'[a-zA-Z]+[a-zA-Z0-9]', 'id')
    ]

    while line:
        for pattern, token_type in token_patterns:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                matched_text = match.group()
                if matched_text:
                    if token_type == 'lit_string':
                        quote_content = matched_text[1:-1].strip()
                        tokens.extend(['<sep,">', f'<{token_type},{quote_content}>', '<sep,">'])
                    else:
                        tokens.append(f'<{token_type},{matched_text}>')
                line = line.replace(match.group(), "", 1)

        if line == "":
            break

    processed_tokens = []
    for token_str in tokens:
        type_value = token_str.strip('<>').split(',')
        if len(type_value) == 2:
            processed_tokens.append((type_value[0], type_value[1]))

    self.tokens = processed_tokens
    print("Token list: ", self.tokens)
    return tokens

def accept_new_token(self):
    if self.tokens:
        print("Accepted token: " + self.current_token[1])
        self.text_parse_tree.insert("end", "Accepted token: " + self.current_token[1] + "\n")
        self.current_token = self.tokens.pop(0)
    else:
        self.text_parse_tree.insert("end", "\n")
        return

def process_multiplication(self, parent_id):
    print("Parent node: multiplication")
    self.text_parse_tree.insert("end", "Parent node: multiplication\n")

    if self.current_token[0] == "lit_int":
        print("Child node: integer")
        self.text_parse_tree.insert("end", "Child node: integer\n")
        print("Integer token: " + self.current_token[1])
        self.text_parse_tree.insert("end", "Integer token: " + self.current_token[1] + "\n")

        node_id = parent_id + 'levelA-4-1'
        self.tree_visual_output.insert(parent_id, 'end', node_id, text='int')

        sub_node_id = node_id + 'levelA-5-1'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1])

        accept_new_token(self)

    elif self.current_token[0] == "lit_float":
        print("Child node: float")
        self.text_parse_tree.insert("end", "Child node: float\n")
        print("Float token: " + self.current_token[1])
        self.text_parse_tree.insert("end", "Float token: " + self.current_token[1] + "\n")

        node_id = parent_id + 'levelA-4-5'
        self.tree_visual_output.insert(parent_id, 'end', node_id, text='float')

        sub_node_id = node_id + 'levelA-5-4'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1])

        accept_new_token(self)

    if self.current_token[1] == "*":
        print("Child node: operator")
        self.text_parse_tree.insert("end", "Child node: operator\n")
        node_id = parent_id + 'levelA-4-2'
        self.tree_visual_output.insert(parent_id, 'end', node_id, text='op')

        sub_node_id = node_id + 'levelA-5-2'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1])

        accept_new_token(self)
        if self.current_token[0] == "lit_float":
            print("Child node: float")
            self.text_parse_tree.insert("end", "Child node: float\n")
            print("Float token: " + self.current_token[1])
            self.text_parse_tree.insert("end", "Float token: " + self.current_token[1] + "\n")

            node_id = parent_id + 'levelA-4-3'
            self.tree_visual_output.insert(parent_id, 'end', node_id, text='float')

            sub_node_id = node_id + 'levelA-5-3'
            self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1])
            accept_new_token(self)

def process_math(self):
    print("Parent node: math")
    self.text_parse_tree.insert("end", "Parent node: math\n")

    parent_id = 'levelA-2-4'
    self.tree_visual_output.insert('level1', 'end', parent_id, text='math')

    if self.current_token[0] in ["lit_int", "lit_float"]:
        print("Child node: multiplication")
        self.text_parse_tree.insert("end", "Child node: multiplication\n")

        node_id = parent_id + 'levelA-3-1'
        self.tree_visual_output.insert(parent_id, 'end', node_id, text='multi')

        process_multiplication(self, node_id)
        if self.current_token[0] == "lit_int":
            print("Child node: integer")
            self.text_parse_tree.insert("end", "Child node: integer\n")
            print("Integer token: " + self.current_token[1])
            self.text_parse_tree.insert("end", "Integer token: " + self.current_token[1] + "\n")

            accept_new_token(self)

        if self.current_token[0] == "lit_float":
            print("Child node: float")
            self.text_parse_tree.insert("end", "Child node: float\n")
            print("Float token: " + self.current_token[1])
            self.text_parse_tree.insert("end", "Float token: " + self.current_token[1] + "\n")

            accept_new_token(self)

        if self.current_token[1] == "+":
            print("Child node: operator")
            self.text_parse_tree.insert("end", "Child node: operator\n")
            print("Operator token: " + self.current_token[1])
            self.text_parse_tree.insert("end", "Operator token: " + self.current_token[1] + "\n")

            node_id = parent_id + 'levelB-3-2'
            self.tree_visual_output.insert(parent_id, 'end', node_id, text='op')
            sub_node_id = node_id + 'levelB-4-2'
            self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1])

            accept_new_token(self)

            print("Child node: multiplication")
            self.text_parse_tree.insert("end", "Child node: multiplication\n")

            node_id = parent_id + 'levelB-3-3'
            self.tree_visual_output.insert(parent_id, 'end', node_id, text='multi')

            process_multiplication(self, node_id)
        else:
            print("Error: expected '+' after integer in math expression")
            self.text_parse_tree.insert("end", "Error: expected '+' after integer in math expression\n")
    else:
        print("Error: math expression expects float or integer")
        self.text_parse_tree.insert("end", "Error: math expression expects float or integer\n")

def process_expression(self):
    print("Parent node: expression")
    self.text_parse_tree.insert("end", "Parent node: expression\n")

    type_token, token = self.current_token

    self.tree_visual_output.insert('', 'end', 'expr', text="expression")

    if token == "if":
        print("Child node: keyword")
        self.text_parse_tree.insert("end", "Child node: keyword\n")
        print("Keyword token: " + token)
        self.text_parse_tree.insert("end", "Keyword token: " + token + "\n")

        node_id = 'expr-if'
        self.tree_visual_output.insert('expr', 'end', node_id, text='keyword')

        sub_node_id = node_id + '-if'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=token)

        accept_new_token(self)

        print("Child node: if expression")
        self.text_parse_tree.insert("end", "Child node: if expression\n")

        process_if_expression(self)
    elif token == "print":
        print("Child node: identifier")
        self.text_parse_tree.insert("end", "Child node: identifier\n")
        print("Keyword token: " + token)
        self.text_parse_tree.insert("end", "Keyword token: " + token + "\n\n")

        node_id = 'expr-print'
        self.tree_visual_output.insert('expr', 'end', node_id, text='identifier')

        sub_node_id = node_id + '-print'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=token)

        accept_new_token(self)

        print("Child node: print expression")
        self.text_parse_tree.insert("end", "Child node: print expression\n")
        process_print_expression(self)

    elif type_token == "key":
        print("Child node: keyword")
        self.text_parse_tree.insert("end", "Child node: keyword\n")
        print("Keyword token: " + token)
        self.text_parse_tree.insert("end", "Keyword token: " + token + "\n")

        node_id = 'expr-keyword'
        self.tree_visual_output.insert('expr', 'end', node_id, text='keyword')

        sub_node_id = node_id + '-' + token
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=token)

        accept_new_token(self)

    elif type_token == "id":
        print("Child node: identifier")
        self.text_parse_tree.insert("end", "Child node: identifier\n")
        print("Identifier token: " + token)
        self.text_parse_tree.insert("end", "Identifier token: " + token + "\n")
        accept_new_token(self)
    else:
        print("Error: expected identifier as the first element of the expression")
        self.text_parse_tree.insert("end", "Error: expected identifier as the first element of the expression\n")
        return

    type_token, token = self.current_token
    if type_token == "id":
        print("Child node: identifier")
        self.text_parse_tree.insert("end", "Child node: identifier\n")
        print("Identifier token: " + token)
        self.text_parse_tree.insert("end", "Identifier token: " + token + "\n")

        node_id = 'expr-id'
        self.tree_visual_output.insert('expr', 'end', node_id, text='identifier')

        sub_node_id = node_id + '-id'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=token)

        accept_new_token(self)

    if self.current_token[1] == "=":
        print("Child node: operator")
        self.text_parse_tree.insert("end", "Child node: operator\n")

        node_id = 'expr-assign'
        self.tree_visual_output.insert('expr', 'end', node_id, text='operator')

        sub_node_id = node_id + '-assign'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1])

        accept_new_token(self)

        print("Child node: math expression")
        self.text_parse_tree.insert("end", "Child node: math expression\n")
        process_math(self)

    elif token == "if":
        return

    elif token == "print":
        return

    else:
        print("Error: expected '=' as the second element of the expression")
        self.text_parse_tree.insert("end", "Error: expected '=' as the second element of the expression\n")
        return

def process_if_expression(self):
    print("Parent node: if expression")
    self.text_parse_tree.insert("end", "Parent node: if expression\n")
    type_token, token = self.current_token

    node_id = 'expr-if-exp'
    self.tree_visual_output.insert('expr', 'end', node_id, text='if expression')

    if type_token == "key":
        print("Child node: keyword")
        self.text_parse_tree.insert("end", "Child node: keyword\n")
        print("Keyword token: " + token)
        self.text_parse_tree.insert("end", "Keyword token: " + token + "\n")
        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "sep":
        print("Child node: separator")
        self.text_parse_tree.insert("end", "Child node: separator")
        print("Separator token: " + token + "\n")
        self.text_parse_tree.insert("end", "Separator token: " + token + "\n")

        sub_node_id = node_id + '-sep'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='separator')

        sub_sub_node_id = sub_node_id + '-left-paren'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=self.current_token[1])

        accept_new_token(self)

    process_comparison_expression(self)

    print("Parent node: if expression")
    self.text_parse_tree.insert("end", "Parent node: if expression\n")

    node_id = 'expr-if-exp-close'
    self.tree_visual_output.insert('expr', 'end', node_id, text='if expression')

    type_token, token = self.current_token
    if type_token == "sep":
        print("Child node: separator")
        self.text_parse_tree.insert("end", "Child node: separator\n")
        print("Separator token: " + token)
        self.text_parse_tree.insert("end", "Separator token: " + token + "\n")

        sub_node_id = node_id + '-sep-close'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='separator')

        sub_sub_node_id = sub_node_id + '-right-paren'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=self.current_token[1])

        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "sep":
        print("Child node: separator")
        self.text_parse_tree.insert("end", "Child node: separator\n")
        print("Separator token: " + token)
        self.text_parse_tree.insert("end", "Separator token: " + token + "\n")

        sub_node_id = node_id + '-colon'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='separator')

        sub_sub_node_id = sub_node_id + '-colon'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=self.current_token[1])

        accept_new_token(self)

def process_comparison_expression(self):
    print("Parent node: comparison expression")
    self.text_parse_tree.insert("end", "Parent node: comparison expression\n")
    type_token, token = self.current_token

    node_id = 'expr-comp'
    self.tree_visual_output.insert('expr', 'end', node_id, text='comparison expression')

    if type_token == "id":
        print("Child node: identifier")
        self.text_parse_tree.insert("end", "Child node: identifier\n")
        print("Identifier token: " + token)
        self.text_parse_tree.insert("end", "Identifier token: " + token + "\n")

        sub_node_id = node_id + '-id-left'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='identifier')

        sub_sub_node_id = sub_node_id + '-left'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=token)

        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "op":
        print("Child node: operator")
        self.text_parse_tree.insert("end", "Child node: operator\n")
        print("Operator token: " + token)
        self.text_parse_tree.insert("end", "Operator token: " + token + "\n")

        sub_node_id = node_id + '-op'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='operator')

        sub_sub_node_id = sub_node_id + '-op'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=">")

        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "id":
        print("Child node: identifier")
        self.text_parse_tree.insert("end", "Child node: identifier\n")
        print("Identifier token: " + token)
        self.text_parse_tree.insert("end", "Identifier token: " + token + "\n")

        sub_node_id = node_id + '-id-right'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='identifier')

        sub_sub_node_id = sub_node_id + '-right'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=token)

        accept_new_token(self)

def process_print_expression(self):
    print("Parent node: print expression")
    self.text_parse_tree.insert("end", "Parent node: print expression\n")

    node_id = 'expr-print-exp'
    self.tree_visual_output.insert('expr', 'end', node_id, text='print expression')

    type_token, token = self.current_token
    if type_token == "sep":
        print("Child node: separator")
        self.text_parse_tree.insert("end", "Child node: separator\n")
        print("Separator token: " + token)
        self.text_parse_tree.insert("end", "Separator token: " + token + "\n")

        sub_node_id = node_id + '-sep'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='separator')

        sub_sub_node_id = sub_node_id + '-left-paren'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=token)

        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "sep":
        print("Child node: separator")
        self.text_parse_tree.insert("end", "Child node: separator\n")
        print("Separator token: " + token)
        self.text_parse_tree.insert("end", "Separator token: " + token + "\n")

        sub_node_id = node_id + '-quote'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='separator')

        sub_sub_node_id = sub_node_id + '-quote'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=token)

        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "lit_string":
        print("Child node: string literal")
        self.text_parse_tree.insert("end", "Child node: string literal\n")
        print("String literal token: " + token)
        self.text_parse_tree.insert("end", "String literal token: " + token + "\n")

        sub_node_id = node_id + '-str-literal'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='string literal')

        sub_sub_node_id = sub_node_id + '-str'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=token)

        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "sep":
        print("Child node: separator")
        self.text_parse_tree.insert("end", "Child node: separator\n")
        print("Separator token: " + token)
        self.text_parse_tree.insert("end", "Separator token: " + token + "\n")

        sub_node_id = node_id + '-quote-close'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='separator')

        sub_sub_node_id = sub_node_id + '-quote'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=token)

        accept_new_token(self)

    type_token, token = self.current_token
    if type_token == "sep":
        print("Child node: separator")
        self.text_parse_tree.insert("end", "Child node: separator\n")
        print("Separator token: " + token)
        self.text_parse_tree.insert("end", "Separator token: " + token + "\n")

        sub_node_id = node_id + '-paren-close'
        self.tree_visual_output.insert(node_id, 'end', sub_node_id, text='separator')

        sub_sub_node_id = sub_node_id + '-right-paren'
        self.tree_visual_output.insert(sub_node_id, 'end', sub_sub_node_id, text=token)

        accept_new_token(self)

def clear_visualization(self):
    for item in self.tree_visual_output.get_children():
        self.tree_visual_output.delete(item)

def parse_all_tokens(self):
    self.text_parse_tree.insert("end", f"--- Parsing Tokens ---\n{self.tokens}\n\n")

    self.current_token = self.tokens.pop(0)
    process_expression(self)
    if self.current_token[1] == ";":
        print("Parse tree successfully built!")
        self.text_parse_tree.insert("end", "Parse tree successfully built!\n\n")
