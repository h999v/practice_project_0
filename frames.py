import tkinter as tk
import tkinter.messagebox as ms
from tkinter import filedialog as fd


win = tk.Tk()
win.resizable(False, False)
win.geometry("803x400")
win.title("Блокнот")


def open_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Открыть файл',
        initialdir='/',
        filetypes=filetypes
    )

    with open(filename, 'r') as fic:
        fileread = fic.read()

    txt_enter.insert('0.0', fileread)


def save_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*')
    )

    get_content = txt_enter.get(0.0, 'end')

    filename = fd.asksaveasfilename(
        title='Сохранить файл',
        initialdir='/',
        filetypes=filetypes
    )

    ms.showinfo(
        title='Info',
        message=filename
    )

    with open(filename, 'w+') as fiv:
        fiv.write(get_content)


def clear():
    txt_enter.delete(0.0, 'end')


frm_function = tk.Frame(borderwidth=5, width=20, relief="ridge", bg='gray')
frm_function.grid(sticky='ns')

btn_open = tk.Button(master=frm_function, text="Открыть", width=20, command=open_file)
btn_open.grid(column=0, row=0)
btn_new = tk.Button(master=frm_function, text="Новый", width=20, command=clear)
btn_new.grid(column=0, row=1)
btn_save = tk.Button(master=frm_function, text="Сохранить", width=20, command=save_file)
btn_save.grid(column=0, row=2)

frm_enter = tk.Frame(borderwidth=5, relief="ridge")
frm_enter.grid(row=0, column=1)

scroll_bar = tk.Scrollbar(master=frm_enter, orient='vertical')
txt_enter = tk.Text(master=frm_enter, height=24, width=88, yscrollcommand=scroll_bar.set)
txt_enter.pack(side='left', fill='both')
scroll_bar.config(command=txt_enter.yview)
scroll_bar.pack(side='right', fill='y')

win.mainloop()
