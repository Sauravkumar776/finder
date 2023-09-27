

from tkinter import filedialog, tk
import a2lparser  # You'll need to install a2lparser library

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def browse_a2l():
    a2l_path = filedialog.askopenfilename(filetypes=[("A2L Files", "*.a2l")])
    a2l_entry.delete(0, tk.END)
    a2l_entry.insert(0, a2l_path)

def find_variables():
    file_path = file_entry.get()
    a2l_path = a2l_entry.get()

    # Implement your logic to parse the files and find variables here
    # For example, you can use a2lparser library to parse the a2l file
    
    # Display the found variables (replace this with your actual logic)
    result_label.config(text="Variables found: Var1, Var2, Var3")

# Create the main window
root = tk.Tk()
root.title("Variable Finder")

# Create labels and entry fields
tk.Label(root, text="Variable File:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="A2L File:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
a2l_entry = tk.Entry(root, width=40)
a2l_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_a2l).grid(row=1, column=2, padx=5, pady=5)

# Create a "Run" button
run_button = tk.Button(root, text="Run", command=find_variables)
run_button.grid(row=2, column=0, columnspan=3, pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()


saurav kumar <saurav@tangentmotorsport.com>


saurav kumar <saurav@tangentmotorsport.com>
