import tkinter as tk
import speech_recognition as sr

# Does both the recording and the speech recognition.
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
    
    def save_text_to_file(self, filename="recorded_text.txt"):
        # Save the recognized text to a file.
        # Args:
        # filename (str): The name of the file to save the text to.

        # Join the list of strings into a single string with line breaks
        self.full_text = "\n".join(self.textList)

        # Write the text to a file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.full_text)

    
    # Records small snippets and converts them to text.
    def RecordAndConvertToText(self):
        
        try:
            # Infinite loop to keep recording continuously as long as recordingStatus is True.
            while self.recordingStatus:  
                with sr.Microphone() as source:
                    print("Recording will start now")
                    audio = self.r.listen(source)
                try:
                    # for testing purposes, we're just using the default API key
                    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                    # instead of `r.recognize_google(audio)`
                    currentLine = self.r.recognize_google(audio)
                    print("Google Speech Recognition thinks you said and it has been added to the total list" + currentLine)
                    self.textList.append(currentLine)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
            print("Recording stopped.")
            self.save_text_to_file("my_recorded_text.txt")      