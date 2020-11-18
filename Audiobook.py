import pyttsx3
import PyPDF2

pdfbook = open('12.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfbook)
pages = pdfReader.numPages
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

speaker.say("This program is build by Beeplab")
speaker.setProperty('voice', voices[1].id)

#speaker.setProperty('voice', voices[0].id)

for idx in range(21, pages):
    page = pdfReader.getPage(idx)
    text = page.extractText()
    print(text)
    speaker.say(text)
    speaker.runAndWait()
