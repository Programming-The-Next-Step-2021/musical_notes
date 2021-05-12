
# Loading and initializing
from tkinter import *
from PIL import ImageTk, Image



class game_notes:
    """
    This package will help you learn to recognize musical notes. Run the program and it will give you a note in musical notation.
    Next, type the letter of the note you think it corresponds to. The program will then tell you whether you're right or wrong.
    Press enter to move onto the next note. When you're done practicing, hit the escape key to finish your session. 
    The program will show you your average accuracy, and the accuracy for separate notes. Good luck!
    """
    def __init__(self):
        root = Tk()
        root.title('notes_test')
        root.geometry("500x500")

        root.mainloop()
