from pdfminer.high_level import extract_text
from tkinter import Tk, filedialog
from gtts import gTTS
import os
import time

def input():
    """
    This function asks the user to input a file through the standard OS
    filewindow. It only accepts PDF's.

    Returns:
        path: The path to the PDF.
    """

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    root.lift()
    root.filename = filedialog.askopenfilename(
        initialdir = "/$HOME/",
        title = "Select file",
        filetypes=(("PDF files", "*.pdf"), ("PDF files", "*.pdf"))
    )

    if root.filename:
        print(root.filename)
        return root.filename

def PdfToText(path):
    text = extract_text(path)
    print(text)
    # Language in which you want to convert 
    language = 'en'
    
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=text, lang=language, slow=False) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("Coders.mp3") 
    

##def TextToSpeech(text):

print(time.time())
path = input();
PdfToText(path)
print(time.time())