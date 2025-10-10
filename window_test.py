import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("400x500")
tehx = ""
def button_function():
    print("button pressed")
    tehx += "Button pressed "


button = ctk.CTkButton(master=app,text="Button", command=button_function)
button.place(relx=0.5,rely=0.5,anchor = ctk.CENTER)

# textbox = ctk.CTkTextbox(app,border_color="blue",value=)
# textbox.place(relx=1,rely=1,anchor=ctk.CENTER)

la = ctk.CTkLabel(app,text=tehx,bg_color="black")
la.place(relx=0.2,rely=0.6,anchor=ctk.CENTER)
app.mainloop()

import tkinter as tk
from tkinter import filedialog

def upload_file():
    file_path = filedialog.askopenfilename(title="Select Profile Picture", filetypes=[("Text File", ('*.txt')), ("All files", "*.*")])
    print("Selected File:", file_path)

root = tk.Tk()
open_button = tk.Button(root, text="Open File", command= upload_file)
open_button.pack(pady=10)
root.mainloop()