import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import speech_recognition as sr

class RecorderApp(App):
    def build(self):
        # This will automatically load the kv file
        return self.layout

    def toggle_recording(self):
        # Your existing toggle_recording logic
        pass

class RecorderApp(App):
    def build(self):
        self.recorder = Recorder()
        self.layout = BoxLayout(orientation='vertical')
        self.start_stop_button = Button(text='Start Recording')
        self.start_stop_button.bind(on_press=self.toggle_recording)
        self.text_display = TextInput(readonly=True, halign="left")
        self.layout.add_widget(self.start_stop_button)
        self.layout.add_widget(self.text_display)
        return self.layout

    def toggle_recording(self, instance):
        if self.recorder.getRecordingStatus():
            self.recorder.setRecordingStatus(False)
            instance.text = 'Start Recording'
            self.text_display.text = self.recorder.full_text
        else:
            self.recorder.setRecordingStatus(True)
            instance.text = 'Stop Recording'
            self.recorder.RecordAndConvertToText()

class Recorder:
    def __init__(self):
        self.r = sr.Recognizer()
        self.textList = []
        self.full_text = ""
        self.recordingStatus = False
    
    def getRecordingStatus(self):
        return self.recordingStatus
    
    def setRecordingStatus(self, status):
        self.recordingStatus = status

    def RecordAndConvertToText(self):
        try:
            while self.recordingStatus:
                with sr.Microphone() as source:
                    audio = self.r.listen(source)
                try:
                    currentLine = self.r.recognize_google(audio)
                    self.textList.append(currentLine)
                except sr.UnknownValueError:
                    pass  # or handle the error as you see fit
                except sr.RequestError as e:
                    pass  # or handle the error as you see fit
            self.full_text = "\n".join(self.textList)
        except KeyboardInterrupt:
            self.save_text_to_file("my_recorded_text.txt")

if __name__ == '__main__':
    RecorderApp().run()
