
# Loading and initializing
from tkinter import *
from PIL import ImageTk, Image
from random import randint

def imagegen(numb, imagelist):
    return "musical_notes/musicalnotes/" + imagelist[numb]+".png"



class game_notes:
    """
    This package will help you learn to recognize musical notes. Run the program and it will give you a note in musical notation.
    Next, type the letter of the note you think it corresponds to. The program will then tell you whether you're right or wrong.
    Press enter to move onto the next note. When you're done practicing, hit the escape key to finish your session. 
    The program will show you your average accuracy, and the accuracy for separate notes. Good luck!
    """
    def __init__(self):
        # Loading and initializing

        root = Tk()
        root.title('notes_test')
        root.geometry("700x500")

        # Creating the answer function:
        def start_note_practice_answer ():
            answer_label.config(text=answer_box.get())
    
        # Creating flashcards:
        def start_note_practice ():
            # Hide the previous frames
            hide_other_frames()
            # Start the note practice screen
            start_note_practice_frame.pack(fill= BOTH, expand=1)
            my_label = Label(start_note_practice_frame, text = "Note practice").pack()
            # List of all the different notes that will be in the test:
            notes_list = ['C_test', 'C1_test', 'D_test', 'D1_test', 'E_test', 'E1_test', 'F_test', 'F1_test', 'G_test', 'G1_test', 'A_test', 'A1_test', 'B_test', 'B1_test']

            # Random number generator:
            randnumb = randint(0, len(notes_list)-1)
            randnote = "musical_notes/musicalnotes/" + notes_list[randnumb]+".png"

            # Creating images:
            global note_image
            note_image = ImageTk.PhotoImage(Image.open(randnote))
            show_note = Label(start_note_practice_frame, image=note_image)
            show_note.pack(pady=15)

            # Answer form:
            global answer_box
            answer_box = Entry(start_note_practice_frame, font = ("Calibri", 18))
            answer_box.pack(pady=15)

            # Button to show a new note:
            passbutton = Button(start_note_practice_frame, text = "I don't know!", command = start_note_practice)
            passbutton.pack(pady=10)

            # Button to input answer:
            ansbutton = Button(start_note_practice_frame, text = "Answer", command = start_note_practice_answer)
            ansbutton.pack(pady=5)

            # Feedback:
            global answer_label
            answer_label = Label(start_note_practice_frame, text = "", font = ("Calibri", 18))
            answer_label.pack(pady=15)
        # Creating Infoboxes
        def note_infobox():
            hide_other_frames()
            note_infobox_frame.pack(fill=BOTH, expand=1)
            my_label = Label(note_infobox_frame, text = "Information").pack()

        # Hiding other frames, including what's in previous similar frames:
        def hide_other_frames():
            for widget in start_note_practice_frame.winfo_children():
                widget.destroy()
            for widget in note_infobox_frame.winfo_children():
                widget.destroy()
            start_note_practice_frame.pack_forget()
            note_infobox_frame.pack_forget()

        # Creating a menu
       
        main_menu = Menu(root)
        root.config(menu = main_menu)

        # Creating menu items
        notes_menu = Menu(main_menu)
        main_menu.add_cascade(label = "Note practice", menu = notes_menu)
        notes_menu.add_command(label = "Practice", command = start_note_practice)
        notes_menu.add_command(label = "Information", command = note_infobox)
        notes_menu.add_separator()
        notes_menu.add_command(label = "Exit", command = root.quit)

        # Creating frames
        start_note_practice_frame = Frame(root, width = 700, height = 500)
        note_infobox_frame = Frame(root, width = 500, height = 500)

        root.mainloop()

