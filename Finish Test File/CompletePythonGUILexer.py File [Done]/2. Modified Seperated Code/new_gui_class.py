from tkinter import *
from tkinter import ttk
from new_token_parse import tokenize_line, accept_new_token, process_multiplication, process_math, process_expression, process_if_expression, process_comparison_expression, process_print_expression, clear_visualization, parse_all_tokens

class CustomLexerGUI:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Custom Lexer GUI: Version 1.0")

        self.label_code_input = Label(self.main_window, text="Source Code Input:")
        self.label_code_input.grid(row=0, column=0, sticky=W)

        self.label_token_output = Label(self.main_window, text="Token Output:")
        self.label_token_output.grid(row=0, column=2, sticky=W)

        self.label_parse_tree = Label(self.main_window, text="Parse Tree:")
        self.label_parse_tree.grid(row=0, column=4, sticky=W)

        self.label_visual_tree = Label(self.main_window, text="Visualization Tree (hierarchical)")
        self.label_visual_tree.grid(row=2, column=2, sticky=W)

        self.label_current_line = Label(self.main_window, text="Current Processing Line:")
        self.label_current_line.grid(row=4, column=0, sticky=W)

        self.text_code_input = Text(self.main_window, width=55, height=30)
        self.text_code_input.grid(row=1, column=0, columnspan=2, sticky=E)

        self.text_token_output = Text(self.main_window, width=40, height=30)
        self.text_token_output.grid(row=1, column=2, columnspan=2, sticky=E)

        self.entry_current_line = Entry(self.main_window)
        self.entry_current_line.grid(row=4, column=1, sticky=E)

        self.text_parse_tree = Text(self.main_window, width=55, height=30)
        self.text_parse_tree.grid(row=1, column=4, columnspan=2, sticky=E)

        self.tree_visual_output = ttk.Treeview(self.main_window)
        self.tree_visual_output.grid(row=3, column=2, sticky=E)

        self.button_next_line = Button(self.main_window, text="Next Line", command=self.process_next_line)
        self.button_next_line.grid(row=5, column=0, sticky=W)

        self.button_quit = Button(self.main_window, text="Quit", command=self.exit_program)
        self.button_quit.grid(row=5, column=3, columnspan=3, sticky=E)

        self.line_counter = 0
        self.tokens = []
        self.current_token = ("empty", "empty")

    def process_next_line(self):
        clear_visualization(self)
        user_input = self.text_code_input.get("1.0", "end-1c")
        input_lines = user_input.split('\n')

        if self.line_counter < len(input_lines):
            current_line = input_lines[self.line_counter]
            self.text_token_output.insert("end", f"--- Processing Line ---\n{current_line}\n\n")
            token_list = tokenize_line(self, current_line)

            if token_list:
                self.text_token_output.insert("end", "\n".join(token_list) + "\n\n")
                self.entry_current_line.delete(0, "end")
                self.line_counter += 1
                self.entry_current_line.insert(0, self.line_counter)
                parse_all_tokens(self)
            else:
                print("The token list is empty.")
        else:
            print("No more lines to process.")

    def exit_program(self):
        self.main_window.destroy()
        self.main_window.quit()
