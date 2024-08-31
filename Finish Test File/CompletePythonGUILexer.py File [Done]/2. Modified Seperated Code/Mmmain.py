from tkinter import Tk
from new_gui_class import CustomLexerGUI

if __name__ == '__main__':
    main_window = Tk()
    lexer_gui = CustomLexerGUI(main_window)
    main_window.mainloop()
