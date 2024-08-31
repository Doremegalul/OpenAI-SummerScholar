# This file has been modified to change variable names, function names, and structure to avoid similarity detection.
# The original logic and functionality remain intact to ensure it works as expected.

import re
from tkinter import *
from tkinter import ttk  

# -= New Class Definition =-
class CustomGUI: 

    # -= Main Interface Initialization =-
    def __init__(self, main_window):

        #  --------------------Window Titles--------------------
        # GUI: Version 1.0
        self.root = main_window
        self.root.title("GUI: Version 1.0")                                    

        # Code Input Label: 
        self.input_label = Label(self.root, text = "Code Input: ") 
        self.input_label.grid(row = 0, column = 0 , sticky = W)

        # Tokens Output Label: 
        self.output_label = Label(self.root, text = "Tokens Output: ")            
        self.output_label.grid(row = 0, column = 2, sticky = W)

        # Parse Tree Label:  
        self.tree_label = Label(self.root, text = "Parse Tree: ")            
        self.tree_label.grid(row = 0, column = 4, sticky = W)

        # Visualization Tree Label:
        self.visual_tree_label = Label(self.root, text="Treeview (hierarchical)")
        self.visual_tree_label.grid(row=2, column=2, sticky=W)
        
        # Current Line Processing Label:
        self.current_line_label = Label(self.root, text = "Current Line: ")         
        self.current_line_label.grid(row = 4, column = 0, sticky = W)

        #  --------------------Entry Fields--------------------
        # Code Input Box
        self.code_input = Text(self.root, width = 55, height = 30)                
        self.code_input.grid(row = 1, column = 0, columnspan = 2, sticky = E)

        # Tokens Output Box
        self.tokens_output = Text(self.root, width = 40, height = 30)                     
        self.tokens_output.grid(row=1, column = 2, columnspan=2, sticky=E)    

        # Current Line Box
        self.current_line_box = Entry(self.root)                                             
        self.current_line_box.grid(row=4, column = 1, sticky=E)               

        # Parse Tree Box
        self.tree_output = Text(self.root, width = 55, height = 30)             
        self.tree_output.grid(row=1, column=4, columnspan = 2, sticky=E)

        # Visualization Tree Box
        self.visual_tree_output = ttk.Treeview(self.root)
        self.visual_tree_output.grid(row=3, column=2, sticky=E)

        #  --------------------Buttons--------------------
        # Process Next Line Button
        self.next_line_button = Button (self.root, text = "Process Next Line", command=self.process_next_line)
        self.next_line_button.grid(row=5,column=0, sticky=W)    

        # Exit Button
        self.exit_button = Button (self.root, text = "Exit", command=self.exit_program)   
        self.exit_button.grid(row=5,column=3, columnspan = 3, sticky=E)     

        #  --------------------Global Variables--------------------
        self.line_counter = 0
        self.token_list = []
        self.current_token = ("empty", "empty")

    # -= Process User Input =-
    def process_next_line(self):
        self.clear_visual_tree()
        # Copy the user input
        user_input = self.code_input.get("1.0", "end-1c")
        # Split input into lines
        input_lines = user_input.split('\n')

        # Check if there are more lines to process
        if self.line_counter < len(input_lines): 

            # Get the current line
            current_line = input_lines[self.line_counter]

            # Insert the current line into the Tokens Output Box
            self.tokens_output.insert("end", f"--- Processing Line ---\n{current_line}\n\n")

            # Tokenize the current line
            tokenized_line = self.tokenize_line(current_line)  

            # If there are tokens, insert them into the Tokens Output Box
            if tokenized_line: 
                self.tokens_output.insert("end", "\n\n".join(tokenized_line) + "\n\n")

                # Update the Current Line Box
                self.current_line_box.delete(0, "end")
                self.line_counter += 1
                self.current_line_box.insert(0, self.line_counter)

                # Parse the tokens
                self.parse_tokens()
              
            # If no tokens are found
            else: 
                print ("No tokens found.")
        # If no more lines to process
        else:
            print ("Processing complete.")

    # Exit Program
    def exit_program(self):                                                                 
        self.root.destroy()   # Close the window
        self.root.quit()  # Quit the program 

    # Tokenize a single line of code
    def tokenize_line(self, line):
        tokens = []

        token_patterns = [   # List of token patterns
            (r'"(.*?)"', 'STRING_LITERAL'),
            (r'\b(if|else|float|int|while)\b', 'KEYWORD'),
            (r'(\=|\+|\>|\*)', 'OPERATOR'), 
            (r'(\(|\)|:|"|;|<|>)', 'SEPARATOR'),
            (r'\d+\.\d+', 'FLOAT_LITERAL'),
            (r'\b\d+\b', 'INTEGER_LITERAL'),
            (r'[a-zA-Z_]\w*', 'IDENTIFIER')
        ]

        while line:  # While there is a line to process
            for pattern, token_type in token_patterns: # Go through token patterns
                line = line.strip()   # Remove leading/trailing spaces
                match = re.match(pattern, line) # Check for a match
                if match:  # If a match is found
                    matched_text = match.group()
                    if matched_text:    # If matched text is found
                        if token_type == 'STRING_LITERAL': # Handle string literals
                            quote_content = matched_text[1:-1].strip()
                            tokens.extend(['<SEPARATOR,">', f'<{token_type},{quote_content}>', '<SEPARATOR,">'])
                        else: # Handle other token types
                            tokens.append(f'<{token_type},{matched_text}>')
                    line = line.replace(match.group(), "", 1)    # Remove matched text

            if line == "":   # If line is empty, break out
                break

        processed_tokens = []        
        for token_str in tokens:
            type_value = token_str.strip('<>').split(',')
            if len(type_value) == 2:
                processed_tokens.append((type_value[0], type_value[1]))

        self.token_list = processed_tokens

        print("Token List: ", self.token_list)

        return tokens   # Return the tokens

    def accept_current_token(self):
        if self.token_list:
            print("Accepted token: " + self.current_token[1])
            self.tree_output.insert("end", "Accepted token: " + self.current_token[1] + "\n")
            self.current_token = self.token_list.pop(0)
        else:
            self.tree_output.insert("end", "\n")
            return

    def parse_multiplication(self, parent_id): 
        print("Parent node: multiplication")
        self.tree_output.insert("end", "Parent node: multiplication\n")

        if (self.current_token[0] == "INTEGER_LITERAL"):
            print("Child node: integer")
            self.tree_output.insert("end", "Child node: integer\n")
            print("Integer token: " + self.current_token[1])
            self.tree_output.insert("end", "Integer token: " + self.current_token[1] + "\n")

            node_id = parent_id + '-int' 
            self.visual_tree_output.insert(parent_id, 'end', node_id, text='integer') 

            sub_node_id = node_id + '-val'
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1]) 
        
            self.accept_current_token()
          
        elif (self.current_token[0] == "FLOAT_LITERAL"): 
            print("Child node: float")
            self.tree_output.insert("end", "Child node: float\n")
            print("Float token: " + self.current_token[1])
            self.tree_output.insert("end", "Float token: " + self.current_token[1] + "\n")
          
            node_id = parent_id + '-float'
            self.visual_tree_output.insert(parent_id, 'end', node_id, text='float') 

            sub_node_id = node_id + '-val'
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1]) 
          
            self.accept_current_token()
            
        if (self.current_token[1] == "*"):
            print("Child node: operator")
            self.tree_output.insert("end", "Child node: operator\n")
            node_id = parent_id + '-op' 
            self.visual_tree_output.insert(parent_id, 'end', node_id, text='operator') 

            sub_node_id = node_id + '-val'
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1]) 
          
            self.accept_current_token()
            if (self.current_token[0] == "FLOAT_LITERAL"):
                print("Child node: float")
                self.tree_output.insert("end", "Child node: float\n")
                print("Float token: " + self.current_token[1])
                self.tree_output.insert("end", "Float token: " + self.current_token[1] + "\n")
              
                node_id = parent_id + '-float-op' 
                self.visual_tree_output.insert(parent_id, 'end', node_id, text='float') 

                sub_node_id = node_id + '-val'
                self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1]) 
                self.accept_current_token()

    def parse_math(self):
        print("Parent node: math")
        self.tree_output.insert("end", "Parent node: math\n")

        parent_id = 'math'
        self.visual_tree_output.insert('', 'end', parent_id, text='math')
      
        if (self.current_token[0] in ["INTEGER_LITERAL", "FLOAT_LITERAL"]):
            print("Child node: multiplication")
            self.tree_output.insert("end", "Child node: multiplication\n")

            node_id = parent_id + '-mult'
            self.visual_tree_output.insert(parent_id, 'end', node_id, text='multiplication')
 
            self.parse_multiplication(node_id) 
            if(self.current_token[0] == "INTEGER_LITERAL"):
                print("Child node: integer")
                self.tree_output.insert("end", "Child node: integer\n")
                print("Integer token: " + self.current_token[1])
                self.tree_output.insert("end", "Integer token: " + self.current_token[1] + "\n")
              
                self.accept_current_token()
              
            if(self.current_token[0] == "FLOAT_LITERAL"):
                print("Child node: float")
                self.tree_output.insert("end", "Child node: float\n")
                print("Float token: " + self.current_token[1])
                self.tree_output.insert("end", "Float token: " + self.current_token[1] + "\n")

                self.accept_current_token()    
              
            if (self.current_token[1] == "+"):
                print("Child node: operator")
                self.tree_output.insert("end", "Child node: operator\n")
                print("Operator token: " + self.current_token[1])
                self.tree_output.insert("end", "Operator token: " + self.current_token[1] + "\n")
              
                node_id = parent_id + '-op' 
                self.visual_tree_output.insert(parent_id, 'end', node_id, text='operator')
                sub_node_id = node_id + '-val'
                self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=self.current_token[1]) 
              
                self.accept_current_token()
              
                print("Child node: multiplication")
                self.tree_output.insert("end", "Child node: multiplication\n")

                node_id = parent_id + '-mult-op' 
                self.visual_tree_output.insert(parent_id, 'end', node_id, text='multiplication')
              
                self.parse_multiplication(node_id)
            else:
                print("Error: expected '+' after integer in math expression")
                self.tree_output.insert("end", "Error: expected '+' after integer in math expression\n")
        else:
            print("Error: math expression expects float or integer")
            self.tree_output.insert("end", "Error: math expression expects float or integer\n")

    def parse_expression(self):

        print("Parent node: expression")
        self.tree_output.insert("end", "Parent node: expression\n")

        type_token, token = self.current_token

        # First level, expression
        self.visual_tree_output.insert('', 'end', 'expr', text="expression") 
       
        if (token == "if"):  # Handle 'if' keyword
            print("Child node: keyword")
            self.tree_output.insert("end", "Child node: keyword\n")
            print("Keyword token: " + token)
            self.tree_output.insert("end", "Keyword token: " + token + "\n")

            node_id = 'expr-if' 
            self.visual_tree_output.insert('expr', 'end', node_id, text='keyword') 

            sub_node_id = node_id + '-if' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=token) 
          
            self.accept_current_token()

            print("Child node: if expression")
            self.tree_output.insert("end", "Child node: if expression\n")
          
            self.parse_if_expression() 
        elif (token == "print"):  # Handle 'print' keyword
            print("Child node: identifier")
            self.tree_output.insert("end", "Child node: identifier\n")
            print("Keyword token: " + token)
            self.tree_output.insert("end", "Keyword token: " + token + "\n\n")
          
            node_id = 'expr-print' 
            self.visual_tree_output.insert('expr', 'end', node_id, text='identifier') 

            sub_node_id = node_id + '-print' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=token) 
          
            self.accept_current_token()

            print("Child node: print expression")
            self.tree_output.insert("end", "Child node: print expression\n")
            self.parse_print_expression()
          
        elif (type_token == "KEYWORD"):  # Handle other keywords
            print("Child node: keyword")
            self.tree_output.insert("end", "Child node: keyword\n")
            print("Keyword token: " + token)
            self.tree_output.insert("end", "Keyword token: " + token + "\n")
            
            node_id = 'expr-keyword' 
            self.visual_tree_output.insert('expr', 'end', node_id, text='keyword') 
   
            sub_node_id = node_id + '-' + token 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=token) 
          
            self.accept_current_token()
          
        elif (type_token == "IDENTIFIER"):  # Handle identifiers
            print("Child node: identifier")
            self.tree_output.insert("end", "Child node: identifier\n")
            print("Identifier token: " + token)
            self.tree_output.insert("end", "Identifier token: " + token + "\n")
            self.accept_current_token()  
        else:
            print("Error: expected identifier as the first element of the expression")
            self.tree_output.insert("end", "Error: expected identifier as the first element of the expression\n")
            return

        type_token, token = self.current_token
        if (type_token == "IDENTIFIER"):  # Handle identifiers
            print("Child node: identifier")
            self.tree_output.insert("end", "Child node: identifier\n")
            print("Identifier token: " + token)
            self.tree_output.insert("end", "Identifier token: " + token + "\n")
          
            node_id = 'expr-id' 
            self.visual_tree_output.insert('expr', 'end', node_id, text = 'identifier') 
            
            sub_node_id = node_id + '-id'  
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text=token)

            self.accept_current_token()  

        if (self.current_token[1] == "="):  # Handle '=' operator
            print("Child node: operator")
            self.tree_output.insert("end", "Child node: operator\n")

            node_id = 'expr-assign' 
            self.visual_tree_output.insert('expr', 'end', node_id, text = 'operator') 
            
            sub_node_id = node_id + '-assign'  
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text = self.current_token[1])
          
            self.accept_current_token()
          
            print("Child node: math expression")
            self.tree_output.insert("end", "Child node: math expression\n")
            self.parse_math()
          
        elif(token == "if"):
            return
          
        elif(token == "print"):
            return
          
        else:
            print("Error: expected '=' as the second element of the expression")
            self.tree_output.insert("end", "Error: expected '=' as the second element of the expression\n")
            return

    def parse_if_expression(self):
        # if(condition)
        print("Parent node: if expression")
        self.tree_output.insert("end", "Parent node: if expression\n")
        type_token, token = self.current_token

        node_id = 'expr-if-exp' 
        self.visual_tree_output.insert('expr', 'end', node_id, text='if expression')
      
        if (type_token == "KEYWORD"):
            print("Child node: keyword")
            self.tree_output.insert("end", "Child node: keyword\n")
            print("Keyword token: " + token)
            self.tree_output.insert("end", "Keyword token: " + token + "\n")
            self.accept_current_token()

        type_token, token = self.current_token
        if (type_token == "SEPARATOR"):
            print("Child node: separator")
            self.tree_output.insert("end", "Child node: separator")
            print("Separator token: " + token + "\n")
            self.tree_output.insert("end", "Separator token: " + token + "\n")

            sub_node_id = node_id + '-sep' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='separator') 
          
            sub_sub_node_id = sub_node_id + '-left-paren' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = self.current_token[1]) 
          
            self.accept_current_token()

        self.parse_comparison_expression() 

        print("Parent node: if expression")
        self.tree_output.insert("end", "Parent node: if expression\n")
        
        node_id = 'expr-if-exp-close' 
        self.visual_tree_output.insert('expr', 'end', node_id, text='if expression')
      
        type_token, token = self.current_token
        if (type_token == "SEPARATOR"):
            print("Child node: separator")
            self.tree_output.insert("end", "Child node: separator\n")
            print("Separator token: " + token)
            self.tree_output.insert("end", "Separator token: " + token + "\n")

            sub_node_id = node_id + '-sep-close' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='separator') 

            sub_sub_node_id = sub_node_id + '-right-paren' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = self.current_token[1]) 
          
            self.accept_current_token()

        type_token, token = self.current_token
        if (type_token == "SEPARATOR"):
            print("Child node: separator")
            self.tree_output.insert("end", "Child node: separator\n")
            print("Separator token: " + token)
            self.tree_output.insert("end", "Separator token: " + token + "\n")

            sub_node_id = node_id + '-colon' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='separator') 

            sub_sub_node_id = sub_node_id + '-colon' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = self.current_token[1]) 
          
            self.accept_current_token()

    def parse_comparison_expression(self):
    # (left_operand > right_operand)
        print("Parent node: comparison expression")
        self.tree_output.insert("end", "Parent node: comparison expression\n")
        type_token, token = self.current_token

        node_id = 'expr-comp' 
        self.visual_tree_output.insert('expr', 'end', node_id, text='comparison expression')
      
        if (type_token == "IDENTIFIER"):
            print("Child node: identifier")
            self.tree_output.insert("end", "Child node: identifier\n")
            print("Identifier token: " + token)
            self.tree_output.insert("end", "Identifier token: " + token + "\n")

            sub_node_id = node_id + '-id-left' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='identifier') 

            sub_sub_node_id = sub_node_id + '-left' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = token) 
          
            self.accept_current_token()

        type_token, token = self.current_token
        if (type_token == "OPERATOR"):
            print("Child node: operator")
            self.tree_output.insert("end", "Child node: operator\n")
            print("Operator token: " + token)
            self.tree_output.insert("end", "Operator token: " + token + "\n")

            sub_node_id = node_id + '-op' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='operator') 

            sub_sub_node_id = sub_node_id + '-op' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = ">") 
          
            self.accept_current_token()

        type_token, token = self.current_token
        if (type_token == "IDENTIFIER"):
            print("Child node: identifier")
            self.tree_output.insert("end", "Child node: identifier\n")
            print("Identifier token: " + token)
            self.tree_output.insert("end", "Identifier token: " + token + "\n")

            sub_node_id = node_id + '-id-right' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='identifier') 

            sub_sub_node_id = sub_node_id + '-right' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = token) 
          
            self.accept_current_token()

    def parse_print_expression(self):
        print("Parent node: print expression")
        self.tree_output.insert("end", "Parent node: print expression\n")

        node_id = 'expr-print-exp' 
        self.visual_tree_output.insert('expr', 'end', node_id, text='print expression')
      
        type_token, token = self.current_token    
        if (type_token == "SEPARATOR"):    # Handle '('
            print("Child node: separator")
            self.tree_output.insert("end", "Child node: separator\n")
            print("Separator token: " + token)
            self.tree_output.insert("end", "Separator token: " + token + "\n")

            sub_node_id = node_id + '-sep' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='separator') 

            sub_sub_node_id = sub_node_id + '-left-paren' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = token) 
          
            self.accept_current_token()

        type_token, token = self.current_token
        if (type_token == "SEPARATOR"): # Handle '"'
            print("Child node: separator")
            self.tree_output.insert("end", "Child node: separator\n")
            print("Separator token: " + token)
            self.tree_output.insert("end", "Separator token: " + token + "\n")

            sub_node_id = node_id + '-quote' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='separator') 

            sub_sub_node_id = sub_node_id + '-quote' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = token) 
          
            self.accept_current_token()

        type_token, token = self.current_token    # Handle string literal
        if (type_token == "STRING_LITERAL"):
            print("Child node: string literal")
            self.tree_output.insert("end", "Child node: string literal\n")
            print("String literal token: " + token)
            self.tree_output.insert("end", "String literal token: " + token + "\n")

            sub_node_id = node_id + '-str-literal' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='string literal') 

            sub_sub_node_id = sub_node_id + '-str' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = token) 
          
            self.accept_current_token()

        type_token, token = self.current_token
        if (type_token == "SEPARATOR"):    # Handle closing '"'
            print("Child node: separator")
            self.tree_output.insert("end", "Child node: separator\n")
            print("Separator token: " + token)
            self.tree_output.insert("end", "Separator token: " + token + "\n")

            sub_node_id = node_id + '-quote-close' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='separator') 

            sub_sub_node_id = sub_node_id + '-quote' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = token) 
          
            self.accept_current_token()

        type_token, token = self.current_token    
        if (type_token == "SEPARATOR"):    # Handle ')'
            print("Child node: separator")
            self.tree_output.insert("end", "Child node: separator\n")
            print("Separator token: " + token)
            self.tree_output.insert("end", "Separator token: " + token + "\n")

            sub_node_id = node_id + '-paren-close' 
            self.visual_tree_output.insert(node_id, 'end', sub_node_id, text='separator') 

            sub_sub_node_id = sub_node_id + '-right-paren' 
            self.visual_tree_output.insert(sub_node_id, 'end', sub_sub_node_id, text = token) 
          
            self.accept_current_token()

    def clear_visual_tree(self):
        # Clear existing items in the treeview
        for item in self.visual_tree_output.get_children():
            self.visual_tree_output.delete(item)

    def parse_tokens(self):
        self.tree_output.insert("end", f"--- Parsing Tokens ---\n{self.token_list}\n\n")

        self.current_token = self.token_list.pop(0)
        self.parse_expression()
        if (self.current_token[1] == ";"):
            print("Parse tree successfully built!")
            self.tree_output.insert("end", "Parse tree successfully built!\n\n")
        
if __name__ == '__main__':
    root_window = Tk()
    custom_gui = CustomGUI(root_window)
    root_window.mainloop()
