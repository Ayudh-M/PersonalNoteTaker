import tkinter as tk
from appUtils import Recorder as recorder
from apis import ChatGPTAPI as chat 
from apis import VoiceToTextConverter as vtt

class App:
    def __init__(self, root):
        self.recorder = recorder()  # Create an instance of Recorder
        self.chat = chat(9)
        self.vtt = vtt(9)

        label = tk.Label(root, text="Hello, Tkinter!")
        self.recorder.setLabel = label
        label.pack()
        # Button uses the record method from recorder instance as command
        button = tk.Button(root, text="Record", command=self.recorder.startRecording)
        button.pack()


# Initialize Tkinter and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
