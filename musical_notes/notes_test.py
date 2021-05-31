# To-do: note validation, remember answers and give score

# Loading and initializing
from tkinter import *
from PIL import ImageTk, Image
from random import randint
from playsound import playsound
import time


class random_image:
    # Random number generator:
    def __init__ (inputlist):
        randnumb = randint(0, len(inputlist)-1)
        return randnumb


class game_notes(Tk):
    """
    This package will help you learn to recognize musical notes. Run the program and it will give you a note in musical notation.
    Next, type the letter of the note you think it corresponds to. The program will then tell you whether you're right or wrong and what your score for that note is.
    Press enter to move onto the next note. When you're done practicing, click exit in the menu to shut off the program.
    The program will show you your average accuracy, and the accuracy for separate notes. Good luck!

    -- initializing: musical_notes.game_notes()
    """
    

    def __init__(self):
        # Loading and initializing:---------------------------------------------------------------------------------------------------------------------------------
        global root
        root = Tk()
        root.title('notes_test')
        root.geometry("700x600")
        global notes_list, tones_list, scoredict, tone_scoredict
        notes_list = ['C', 'C1', 'D', 'D1', 'E', 'E1', 'F', 'F1', 'G', 'G1', 'A', 'A1', 'B', 'B1']        
        scoredict = {} #preallocation.
        for note in notes_list:
                scoredict[note] = 0
        tones_list = ['C', 'C1', 'D', 'D1', 'E', 'E1', 'F', 'F1', 'G', 'G1', 'A', 'A1', 'B', 'B1']
        tone_scoredict = {} # for the tone recognition part. preallocation
        for tone in tones_list:
            tone_scoredict[tone] = 0
        """
        The following part concerns the code for the note recognition training. it consists of a function to draw random notes and the interface to operate in.
        Start the game by typing python --> import musical_notes --> musical_notes.game_notes() in your terminal and select the training mode of your choice.
        """ 
        # Create randomized notes:----------------------------------------------------------------------------------------------------------------------------------
        def random_note(): #function that draws a random note when you need it
            global notes_list, check_notes
            
            # Creating a random note to draw:-------------------------------------------------------------------
            global randnumb, randnote, note_image
            randnumb = randint(0, len(notes_list)-1)
            randnote = "musical_notes/musicalnotes/" + notes_list[randnumb]+".png"
            global check_note
            check_note = notes_list[randnumb]
            check_note = ''.join([i for i in check_note if not i.isdigit()])
            # Creating images:----------------------------------------------------------------------------------
            global note_image
            note_image = ImageTk.PhotoImage(Image.open(randnote))
            show_note.config(image=note_image, bg = "white")
         
        # Creating the answer function:------------------------------------------------------------------------------------------------------------------------------
        def start_note_practice_answer ():
            answer = answer_box.get()
            answer = ''.join([i for i in answer if not i.isdigit()]) # Removes all the numbers for different octaves from the answer inputs. We use two octaves in the program, and want either the higher or lower note (C or C1, for example), to be accepted.
            if answer == check_note:
                scoredict[notes_list[randnumb]] += 1 #add one to the score for that note if it's correct.
                response = "Correct! The answer is " + check_note + ". Your score for the note " + notes_list[randnumb] + " is " + str(scoredict[notes_list[randnumb]])    
            else:
                scoredict[notes_list[randnumb]] -= 1 #subtract one from the score for that note of the answer is incorrect.
                response = "Incorrect. The right answer is " + check_note + ". Your score for the note " + notes_list[randnumb] + " is " + str(scoredict[notes_list[randnumb]])
            answer_label.config(text=response)
            answer_label.pack(pady=15)
            root.update_idletasks()
            # Clearing the answer box:---------------------------------------------------------------------------
            time.sleep(2)
            answer_box.delete(0, 'end')
            answer_label.pack_forget()
            random_note()
    
        # Creating flashcards for notes:-----------------------------------------------------------------------------------------------------------------------------
        def start_note_practice ():
            # Hide the previous frames:--------------------------------------------------------------------------
            hide_other_frames()
            # Start the note practice screen:--------------------------------------------------------------------
            start_note_practice_frame.pack(fill= BOTH, expand=1)
            my_label = Label(start_note_practice_frame, text = "Note practice").pack()
            global show_note
            show_note = Label(start_note_practice_frame)
            show_note.pack(pady=15)
            random_note()
            
            # Answer form:----------------------------------------------------------------------------------------
            global answer_box
            answer_box = Entry(start_note_practice_frame, font = ("Calibri", 18), bd = 3)
            answer_box.pack(pady=15)

            # Button to show a new note:--------------------------------------------------------------------------
            passbutton = Button(start_note_practice_frame, text = "I don't know!", command = start_note_practice)
            passbutton.pack(pady=10)

            # Button to input answer:-----------------------------------------------------------------------------
            ansbutton = Button(start_note_practice_frame, text = "Answer", command = start_note_practice_answer)
            ansbutton.pack(pady=5)

            # Feedback:-------------------------------------------------------------------------------------------
            global answer_label
            answer_label = Label(start_note_practice_frame, text = "", font = ("Calibri", 18), bg = "white")
            answer_label.pack(pady=15)


        # Hiding other frames, including what's in previous similar frames:-----------------------------------------------------------------------------------------
        def hide_other_frames():
            for widget in start_note_practice_frame.winfo_children(): #whenever a frame is selected from the menu, all other previously selected frames have to be closed down.
                widget.destroy()
            for widget in note_infobox_frame.winfo_children(): #frame close info
                widget.destroy()
            for widget in start_tone_practice_frame.winfo_children(): #frame close tones
                widget.destroy()
            start_note_practice_frame.pack_forget()
            note_infobox_frame.pack_forget()
            start_tone_practice_frame.pack_forget()

        # Create randomized tones:----------------------------------------------------------------------------------------------------------------------------------
        def random_tone():
            '''
            This part concerns the creation of the flashcards for practicing tonal recognition.
            It is similar to the program used for note recognition, but instead of pictures of notes, we import piano sounds for the different tones.
            '''
            # Creating a random tone to play:-------------------------------------------------------------------------
            global randnumb
            randnumb = randint(0, len(tones_list)-1) #drawing a random number for the tones list.
            randtone = "musical_notes/musicaltones/" + tones_list[randnumb]+".mp3" #selecting the tone sounds
            
            global check_tone
            check_tone = tones_list[randnumb] # we want the program to accept an anser regardless of the octave: C1 should be transformed to C:
            check_tone = ''.join([i for i in check_tone if not i.isdigit()])
            # Creating images:
            global tone_sound
            tone_sound = playsound(randtone)
         
        # Creating the answer function:----------------------------------------------------------------------------------------------------------------------------
        def start_tone_practice_answer ():
            global response
            answer = tone_answer_box.get()
            answer = ''.join([i for i in answer if not i.isdigit()]) # Removes all the numbers for different octaves from the answer inputs
            if answer == check_tone:
                tone_scoredict[tones_list[randnumb]] += 1 #add one to the score for that tone
                response = "Correct! The answer is " + check_tone + ". Your score for the tone " + tones_list[randnumb] + " is " + str(tone_scoredict[tones_list[randnumb]])   
            else:
                tone_scoredict[tones_list[randnumb]] -= 1 # subtract one from the score for that tone.
                response = "Incorrect. The right answer is " + check_tone + ". Your score for the tone " + tones_list[randnumb] + " is " + str(tone_scoredict[tones_list[randnumb]])
            tone_answer_label.config(text=response)
            tone_answer_label.pack(pady=15)
            root.update_idletasks()
           # Clearing the answer box:
            time.sleep(2)
            tone_answer_label.pack_forget()
            tone_answer_box.delete(0, 'end') # Remove everything that was typed into the answer box as soon as answer is selected
            root.update_idletasks() #updates the graphical interface before returning to the main loop.
            
            random_tone()
        # Creating flashcards for tones:----------------------------------------------------------------------------------------------------------------------------
        def start_tone_practice ():
            # Hide the previous frames
            hide_other_frames()
            # Start the note practice screen
            start_tone_practice_frame.pack(fill= BOTH, expand=1)
            tone_label = Label(start_tone_practice_frame, text = "Tone practice").pack()
            global show_tone
            show_tone = Label(start_tone_practice_frame)
            root.update_idletasks()
            random_tone()
            
            # Answer form:
            global tone_answer_box
            tone_answer_box = Entry(start_tone_practice_frame, font = ("Calibri", 18), bd = 3)
            tone_answer_box.pack(pady=15)

            # Button to show a new note:
            tone_passbutton = Button(start_tone_practice_frame, text = "I don't know!", command = start_tone_practice)
            tone_passbutton.pack(pady=10)

            # Button to input answer:
            tone_ansbutton = Button(start_tone_practice_frame, text = "Answer", command = start_tone_practice_answer)
            tone_ansbutton.pack(pady=5)

            # Feedback:
            global tone_answer_label
            tone_answer_label = Label(start_tone_practice_frame, text = "", font = ("Calibri", 18), bg = "white")
            tone_answer_label.pack(pady=15)

        # Creating Infobox------------------------------------------------------------------------------------------------------------------------------------------
        def note_infobox():
            hide_other_frames()
            note_infobox_frame.pack(fill=BOTH, expand=1)
            my_label = Label(note_infobox_frame, text = "Information").pack()
            T = Text(note_infobox_frame, height = 15, width = 80, wrap = WORD, font = ("Calibri", 12), bg = "white")
            infotext = """This tool can be used to either learn to read musical notes or to develop pitch memory.
            
Start by clicking on Training on the top left of the pop-up window and select either Note Practice to practice learning notes, or Tone Practice to learn to recognize different tones! 
The program will show you your live score for a note or tone after you've given your answer for that note or tone so that you can keep track of your progress. 

Done practicing? Either close the program by clicking the standard shut down cross, or select Exit from the Training drop-down menu. Good luck!"""
            T.insert(INSERT, infotext)
            T.pack()
            
            

        # Creating an overarching menu:--------------------------------------------------------------------------------------------------------------------------
        main_menu = Menu(root)
        root.config(menu = main_menu)

        # Creating menu items:-----------------------------------------------------------------------------------------------------------------------------------
        notes_menu = Menu(main_menu)
        main_menu.add_cascade(label = "Menu", menu = notes_menu)
        notes_menu.add_command(label = "Note Practice", command = start_note_practice)
        notes_menu.add_command(label = "Tone practice", command = start_tone_practice)
        notes_menu.add_command(label = "Information", command = note_infobox)
        notes_menu.add_separator()
        notes_menu.add_command(label = "Exit", command = root.destroy)



        # Creating frames:---------------------------------------------------------------------------------------------------------------------------------------
        start_note_practice_frame = Frame(root, width = 700, height = 500, bg = "white")
        start_tone_practice_frame = Frame(root, width = 700, height = 500, bg = "white")
        note_infobox_frame = Frame(root, width = 700, height = 500)

        root.mainloop()