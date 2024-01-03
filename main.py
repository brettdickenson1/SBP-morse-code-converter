from tkinter import *

# ---------------------------- Morse Code Generator ------------------------------- #

#Morse Code Generator Project
def generate_morse_code():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.']

    matched_indexes = []

    enteredText = password_entry.get()

    print(enteredText)

    for value in letters:
        if value in enteredText:
            indexVal = letters.index(value)
            print(indexVal)
            matched_indexes.append(morse[indexVal])
            print(matched_indexes)
            mystring = ' '
            for x in matched_indexes:
                mystring += ' ' + x
            print(mystring)
            canvas.itemconfig(card_title, text=mystring, fill="black")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=250, height=300)
canvas.grid(row=0, column=1)
card_front_img = PhotoImage(file="images/morsecode.png")
card_background = canvas.create_image(120, 70, image=card_front_img)
card_title = canvas.create_text(120, 150, text="Morse Code", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

#Labels
password_label = Label(text="Entered Text:")
password_label.grid(row=3, column=0)

#Entries
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_entry.focus()


# Buttons
generate_password_button = Button(text="Generate Password", command=generate_morse_code)
generate_password_button.grid(row=3, column=2)

window.mainloop()
