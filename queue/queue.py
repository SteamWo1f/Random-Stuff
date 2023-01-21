# ___ _  _ _ ____       ___  ____ ____ ____ ____ ____ _  _       _ _ _ ____ ____       _  _ ____ ___  ____       
#  |  |__| | [__        |__] |__/ |  | | __ |__/ |__| |\/|       | | | |__| [__        |\/| |__| |  \ |___      
#  |  |  | | ___]       |    |  \ |__| |__] |  \ |  | |  |       |_|_| |  | ___]       |  | |  | |__/ |___
# ___  _   _    ____ ___ ____ ____ _  _ _ _ _ ____ _    ____ 
# |__]  \_/     [__   |  |___ |__| |\/| | | | |  | |    |___ 
# |__]   |      ___]  |  |___ |  | |  | |_|_| |__| |___ |    

#(Font: Cybermedium from http://patorjk.com/software/taag/)

import tkinter as tk

root = tk.Tk()
root.title("Queue Form")
root.geometry('600x725+50+50')

def add_item():
    item = name_entry.get() + ' - ' + time_entry.get()
    if item:
        queue_list.insert('end', item)
        with open("queue.txt", "a") as f:
            f.write(item + "\n")

def load_queue():
    with open("queue.txt", "r") as f:
        for line in f:
            queue_list.insert("end", line.strip())

def remove_item():
    if queue_list.curselection():
        # remove the selected item from the listbox
        queue_list.delete(queue_list.curselection())
        # open the queue.txt file in write mode
        with open("queue.txt", "w") as f:
            # write the remaining items in the listbox to the file
            for item in queue_list.get(0, "end"):
                f.write(item + "\n")



#def show_credits():
#    credits_window = tk.Toplevel(root)
#    credits_window.title("Credits")
#    credits_label = tk.Label(credits_window, text="This program created by SteamWolf")
#    credits_label.pack()
#    close_button = tk.Button(credits_window, text="Close", command=credits_window.destroy)
#    close_button.pack()


# Create "Credits" button
#credits_button = tk.Button(root, text="Credits", command=show_credits, font=("Arial", 8), width=10, height=1)
#credits_button.place(x=260, y=715, anchor="w")


# Create "Print Queue" label
queue_label = tk.Label(root, text="Print Queue", font=("Arial", 20, "bold"), fg='blue')
queue_label.place(x=300, y=50, anchor="center")

# Create "Name" label and entry
name_label = tk.Label(root, text="Name:")
name_label.config(font=("Arial", 14), fg='black')
name_label.place(x=335, y=100, anchor="e")
name_entry = tk.Entry(root, width=30, font=("Arial", 14))
name_entry.place(x=135, y=130, anchor="w")

# Create "Time" label and entry
time_label = tk.Label(root, text="Print Time:")
time_label.config(font=("Arial", 14), fg='black')
time_label.place(x=352, y=160, anchor="e")
time_entry = tk.Entry(root, width=30, font=("Arial", 14))
time_entry.place(x=135, y=190, anchor="w")

# Create "Add" button
add_button = tk.Button(root, text="Add", command=add_item, font=("Arial", 14), relief=tk.GROOVE, bg='green', width=10, height=1)
add_button.place(x=250, y=250, anchor="e")

# Create "Remove" button
remove_button = tk.Button(root, text="Remove", command=remove_item, font=("Arial", 14), relief=tk.GROOVE, bg='red', width=10, height=1)
remove_button.place(x=350, y=250, anchor="w")

# Create "Queue" Listbox
queue_list = tk.Listbox(root, font=("Arial", 14))
queue_list.place(x=300, y=500, anchor="center", width=250, height=400)



#create_widgets()
load_queue()
root.mainloop()