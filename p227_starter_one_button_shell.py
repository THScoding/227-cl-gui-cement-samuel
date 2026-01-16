import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

def retreive_url():
    url = url_entry.get()
    return url

# Modify the do_command function:
# to use the new button as needed
def do_command(command):
    global command_textbox
    
      # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()
            
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()
  
def Submit(command):
    if confirm_var.get():
        res = messagebox.askquestion(
            "Confirm Command",
            f"Are you sure you want to run '{command}'?"
        )
        if res != "yes":
            return
    do_command(command)


root = tk.Tk()
confirm_var = tk.BooleanVar(value=True)
frame = tk.Frame(root)
frame.pack()

# set up buttons to run commands
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=10)

confirm_cb = tk.Checkbutton(
    btn_frame,
    text="Confirm",
    variable=confirm_var,
    bg="black",
    fg="white",
    selectcolor="black",
    font=("Times New Roman", 11)
)
confirm_cb.pack(side=tk.LEFT, padx=10)


ping_btn = tk.Button(
    btn_frame,
    text="Ping",
    command=lambda: Submit("ping"),
    font=("Times New Roman", 12),
    bg="red",
    activebackground="purple"
)
ping_btn.pack(side=tk.LEFT, padx=5)

tracert_btn = tk.Button(
    btn_frame,
    text="Tracert",
    command=lambda: Submit("tracert"),
    font=("Times New Roman", 12),
    bg="purple2",
    activebackground="purple"
)
tracert_btn.pack(side=tk.LEFT, padx=5)

nslookup_btn = tk.Button(
    btn_frame,
    text="Nslookup",
    command=lambda: Submit("nslookup"),
    font=("Times New Roman", 12),
    bg="blue",
    activebackground="purple"
)
nslookup_btn.pack(side=tk.LEFT, padx=5)



# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("Times New Roman", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="gumby",
    fg="mediumpurple",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()



#CHECKBUTTON
#Create frame and function for CheckButton, place it next to ping


#IP_CONFIG
#Create Frame and make a function that isn't meant to use URL like the do_button. place it to the left or the right to ping
#Make sure that it has the output

save_btn = tk.Button(frame, text="Save", command=mSave)
save_btn.pack()

root.mainloop()
