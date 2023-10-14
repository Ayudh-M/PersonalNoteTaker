import tkinter as tk

recording = False

def button_click(e):
    global recording
    if recording:
        label.config(text="Press the Button to Record")
        recording = False
        canvas.itemconfig(button_shape, fill="red")
    else:
        label.config(text="Recording...")
        recording = True
        canvas.itemconfig(button_shape, fill="blue")

root = tk.Tk()
root.title("App UI")

label = tk.Label(root, text="Press the Button to Record")
label.pack()

canvas = tk.Canvas(root, width=50, height=50)
canvas.pack()

button_shape = canvas.create_oval(5, 5, 45, 45, fill="red")

canvas.tag_bind(button_shape, "<Button-1>", button_click)

root.mainloop()