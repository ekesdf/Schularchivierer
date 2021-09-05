from tkinter import filedialog, Tk, Button, Label

window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("800x800")

window.config(background="white")


def browseFiles():

    filename = filedialog.askopenfilename(initialdir="/home/yolo/Schreibtisch",
                                          title="Select a File",
                                          filetypes=(("all files", "*.*"),
                                                     ("", ".*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=50,
                            height=4,
                            fg="blue")

button_explore = Button(window, text="Browse Files", command=browseFiles)

button_exit = Button(window, text="Exit", command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=2, row=1)

button_explore.grid(column=2, row=2)

button_exit.grid(column=2, row=3)

window.mainloop()