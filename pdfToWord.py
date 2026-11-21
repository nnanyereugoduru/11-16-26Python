import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from pdf2docx import Converter
from tkinter import messagebox

def clear():
    name_o.set("")
def load():
    path = filedialog.askopenfilename(
        title="choose",
        filetypes=[("only pdf", "*.pdf")]
    )
    if path:
        name_o.set(path)
       
def convert():
    try:
        path = name_o.get()
        doc_path = os.path.splitext(path)[0] + ".docx"
        cv = Converter(path)
        cv.convert(doc_path)
        cv.close()
        messagebox.showinfo("Done", f"Saved: \n\n {doc_path}")
    except Exception as e:
        print(f"error \n\n\n\n{e}")

            
root = tk.Tk()
root.geometry("400x120")
root.title("simple pdf converter")
body = ttk.Frame(root)
body.pack(padx=10,pady=10,fill='x')

ttk.Label(body, text='path').grid(row=0,column=0,pady=2)

name_o = tk.StringVar()
entry = ttk.Entry(body, textvariable=name_o,width=35)
entry.grid(row=0, column=1,padx=4,pady=4)

ttk.Button(body, text='clear', command=clear).grid(row=1,column=0,pady=2)
ttk.Button(body, text='file choice', command=load).grid(row=2,column=0,pady=2)

ttk.Button(body, text='convert', command=convert).grid(row=2,column=1,pady=2)

root.mainloop()