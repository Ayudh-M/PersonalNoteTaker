import tkinter as tk
class Recorder:
    def __init__(self, label = None):
        self.label = label
    
    def startRecording(self):
        if self.label is not None:
            self.label.config(text="Recording...")

    def setLabel(self,label):
        self.label = label
    