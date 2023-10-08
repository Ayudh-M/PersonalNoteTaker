import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Personal Note Taker")  # Set window title

# Add a label
label = tk.Label(root, text="Welcome Press record to start recording", font=("Arial", 16))
label.pack(pady=20)  # Add some padding

# Add a button
button = tk.Button(root, text="Record", command=lambda: label.config(text="Hello, Tkinter!"))
button.pack(pady=20)  # Add some padding

# Start the main event loop
root.mainloop()
