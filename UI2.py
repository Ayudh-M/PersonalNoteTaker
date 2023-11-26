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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.status_label = Label(text='Idle')

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

        self.add_widget(layout)

    def start_recording(self, instance):
        # Placeholder for start recording logic
        self.status_label.text = 'Recording...'

    def stop_recording(self, instance):
        # Placeholder for stop recording logic
        self.status_label.text = 'Idle'

    def open_notes(self, instance):
        self.manager.current = 'notes_screen'

class NotesScreen(Screen):
    def __init__(self, **kwargs):
        super(NotesScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        notes_label = Label(text='Notes')
        back_button = Button(text='Back to Main Screen')
        back_button.bind(on_press=self.go_back)

        layout.add_widget(notes_label)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_screen'

class LectureApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(NotesScreen(name='notes_screen'))

        return sm

if __name__ == '__main__':
    LectureApp().run()
