import os
import tkinter as tk
import threading
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.ttk import *
from ccs_utils import convert_size

file_path = ""
file_name = ""
file_size = 0

root = tk.Tk()
root.resizable(False, False)
root.title("CoolCheckSums")
root.geometry("600x375")


# Minsize

def show_about():
    about_window = Toplevel()
    about_window.geometry('300x55')
    about_window.title("About CoolCheckSums")
    about_label1 = ttk.Label(about_window, text="/CoolCheckSums\\", anchor="c").pack(side=TOP)
    about_label2 = ttk.Label(about_window, text="______/Made By ItsPedram\\______", anchor="c").pack(side=TOP)
    about_label3 = ttk.Label(about_window, text="/Available Under AGPL-3.0 License\\", anchor="c").pack(side=TOP)


def disable_inputs():
    select_new_file_btn["state"] = DISABLED
    calculate_btn["state"] = DISABLED
    select_hash["state"] = DISABLED
    get_arg["state"] = DISABLED
    compare_arg["state"] = DISABLED
    checksum_entry["state"] = DISABLED
    file_menu.entryconfig("Open File", state="disabled")
    file_menu.entryconfig("Save As", state="disabled")


def enable_inputs():
    select_new_file_btn["state"] = ACTIVE
    calculate_btn["state"] = ACTIVE
    select_hash["state"] = ACTIVE
    get_arg["state"] = ACTIVE
    compare_arg["state"] = ACTIVE
    checksum_entry["state"] = ACTIVE
    file_menu.entryconfig("Open File", state="active")
    file_menu.entryconfig("Save Output As", state="active")


def open_file():
    global file_name, file_size, file_path
    file_selector = filedialog.askopenfile()
    if file_selector:
        program_output.delete('1.0', END)
        file_path = os.path.abspath(file_selector.name)
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        program_output.insert(END,
                              str(f"FileName: {file_name}\nFile_Size: {convert_size(file_size)}\nFile Path: {file_path}"
                                  ))


def save_as():
    global save_file_path
    file_types = [('All Files', '*.*'), ('Text Document', '.txt')]
    file_selector = filedialog.asksaveasfile(filetypes=file_types)
    if file_selector:
        save_file_path = os.path.abspath(file_selector.name)
        file = open(save_file_path, "w")
        for line in program_output.get('1.0', 'end-1c').splitlines():
            if line:
                file.write(str(line) + "\n")


def toggle_entry():
    if int(type_value.get()) == 2:
        entry_label.place(x=0, y=354)
        checksum_entry.place(x=125, y=354)

    else:
        entry_label.place_forget()
        checksum_entry.place_forget()


def calculate():
    
    disable_inputs()
    # if type_value.get() == 0:
    #     pass
    # t1 = threading.Thread(target=print_square, args=(10,))
    # calc_text.set("Calculating...")
    # disable_buttons()


background_canvas = tk.Canvas(root, height=300, width=600, bg="#C1C1C1").pack()
secondary_background_frame = tk.Frame(root, bg="#FFFFFF")
secondary_background_frame.place(relwidth=0.95, relheight=0.77, relx=0.025, rely=0.022)

menu_toolbar = Menu(root)
root.config(menu=menu_toolbar)
file_menu = Menu(menu_toolbar, tearoff=False)
menu_toolbar.add_cascade(label="File", menu=file_menu)
menu_toolbar.add_command(label="About", command=show_about)

file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save Output As", command=save_as)
file_menu.add_command(label="Exit", command=root.destroy)

scroll = Scrollbar(secondary_background_frame)
scroll.pack(side=RIGHT, fill=Y)
program_output = Text(secondary_background_frame, yscrollcommand=scroll.set, width=70)
program_output.pack(side=LEFT, fill=BOTH)
scroll.config(command=program_output.yview)

entry_label_text = StringVar()
entry_label_text.set("Enter Your CheckSum: ")
entry_label = Label(root, textvariable=entry_label_text)

checksum_entry = Entry(root, width=78)

select_new_file_btn = Button(root, text='Select File', style='W.TButton', command=open_file)
select_new_file_btn.pack(side=LEFT, padx=10, pady=10)

calc_text = StringVar()
calculate_btn = Button(root, text='Calculate', textvariable=calc_text, style='W.TButton', command=calculate)
calculate_btn.pack(side=LEFT)
calc_text.set("Calculate")

hash_types = ["MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "All/Auto"]
select_hash = ttk.Combobox(background_canvas, values=hash_types)
select_hash.set("Select The Hash Type")
select_hash.pack(side=LEFT, padx=10, pady=10)

type_value = IntVar()
get_arg = Radiobutton(background_canvas, text="-get", variable=type_value, value=1, command=toggle_entry)
get_arg.pack(side=LEFT, padx=10, pady=10)
compare_arg = Radiobutton(background_canvas, text="-compare", variable=type_value, value=2, command=toggle_entry)
compare_arg.pack(side=LEFT, padx=10, pady=10)

exit_button = Button(root, text='Quit', style='W.TButton', command=root.destroy)
exit_button.pack(side=RIGHT, padx=10, pady=10)

root.mainloop()
