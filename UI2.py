# import tkinter as tk
# import Recorder as recorder
# from tkinter import messagebox

# recording = recorder.Recorder().getRecordingStatus

# def button_click(e):
#     global recording
#     if not recording:
#         label.config(text="Press the Button to Record")
#         recording = False
#         recorder.Recorder().setRecordingStatus(False)
#         canvas.itemconfig(button_shape, fill="red")
#     else:
#         label.config(text="Recording...")
#         recording = True
#         recorder.Recorder().setRecordingStatus(True)
#         recorder.Recorder().RecordAndConvertToText()
#         canvas.itemconfig(button_shape, fill="blue")

# root = tk.Tk()
# root.title("App UI")

# label = tk.Label(root, text="Press the Button to Record")
# label.pack()

# canvas = tk.Canvas(root, width=50, height=50)
# canvas.pack()

# button_shape = canvas.create_oval(5, 5, 45, 45, fill="red")

# canvas.tag_bind(button_shape, "<Button-1>", button_click)

# root.mainloop()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LectureApp(App):
    def build(self):
        self.status_label = Label(text='Idle')

        layout = BoxLayout(orientation='vertical')
        record_button = Button(text='Start Recording')
        record_button.bind(on_press=self.start_recording)
        stop_button = Button(text='Stop Recording')
        stop_button.bind(on_press=self.stop_recording)
        notes_button = Button(text='Open Notes')
        notes_button.bind(on_press=self.open_notes)

        layout.add_widget(self.status_label)
        layout.add_widget(record_button)
        layout.add_widget(stop_button)
        layout.add_widget(notes_button)

        return layout

    def start_recording(self, instance):
        # Placeholder for start recording logic
        self.status_label.text = 'Recording...'

    def stop_recording(self, instance):
        # Placeholder for stop recording logic
        self.status_label.text = 'Idle'

    def open_notes(self, instance):
        # Placeholder for opening notes
        self.status_label.text = 'Notes Open'

if __name__ == '__main__':
    LectureApp().run()