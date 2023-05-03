from tkinter import *
from random import randint
root = Tk()
root.geometry("500x300")
root.title("Number Guessing Game")

attempts = 3

random_num = randint(1, 10)
def Guess():
    global text
    global attempts
    attempts -=1
    entry_val = int(num_entry.get())
    if entry_val == random_num:
        text.set("You Win")
    elif attempts == 0:
        text.set("You Lost!")
    elif entry_val < random_num:
        text.set("Go High")
    elif entry_val > random_num :
        text.set("Go Low")
    if entry_val > 10:
        text.set("please enter a number within range")




heading = Label(root, text="Number Guessing Game", font=("CenturyGothic", 15, "bold"))
heading.pack()

lbl_intro = Label(root, text="!Guess A Number Between 1 to 10!")
lbl_intro.pack()

lbl_number = Label(root, text="Guess Number")
lbl_number.pack()

num_entry = Entry(root, font=("lucida", 30, "bold"), border=10, bg="crimson", fg="White")
num_entry.pack()


cal_btn = Button(root, text="Guess", width=50, height=2, bg="black", font=("lucida", 13, "bold"), fg="White", relief=RIDGE, command=Guess)
cal_btn.pack(pady=10)

btn_exit = Button(root, text="Exit", width=50, height=2, bg="black", font=("lucida", 13, "bold"), fg="White", relief=RIDGE, command=root.destroy)
btn_exit.pack()


text = StringVar()
text.set("3 Attempts remaining!")


guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()
