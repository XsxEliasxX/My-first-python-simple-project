#IMPORTING LIBRARYS
import keyboard
import tkinter as tk

#CREATING FUNCTIONS, EVENTS AND EVENT HANDLERS

type_count = 0
def on_press(key):
    global type_count
    type_count += 1
    key_label.config(text=key)
    num_label.config(text=str(type_count))


keyboard.on_press(on_press)

def start_monitoring():
    pass

def resetFunction():
    global type_count
    type_count = 0
    num_label.config(text=str(type_count))

#CREATING THE WINDOW AND THE WIDGETS
root = tk.Tk()
root.title("Keys per type")
root.geometry("200x200")
root.config(bg="light blue")
key_label = tk.Label(root,text="Keys")
reset_button = tk.Button(root,text="Reset numbers",command=resetFunction)
num_label = tk.Label(root,text="")

#INITIATING PROGRAMS
key_label.pack()
num_label.pack()
reset_button.pack()
root.mainloop()