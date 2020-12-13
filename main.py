from pdfminer.high_level import extract_text
from tkinter import Tk, filedialog
from gtts import gTTS
import os
import time

START = 6
END = 31
SPLITTER = "< Chapter"


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
        tempArr1 = root.filename.split("/")
        tempArr2 = tempArr1[len(tempArr1) - 1].split(".")
        global FILE
        FILE = tempArr2[0]
        return root.filename

def PdfToText(path):
    text = extract_text(path, page_numbers = range(START, END))
    arr = text.split(SPLITTER)
    print(len(arr))
    return arr

def TextToSpeech(text_arr):
    language = 'en'
    i = 1
    os.mkdir("results")
    for text in text_arr:
        recording = gTTS(text=text, lang=language, slow=False) 
        recording.save("results/" + FILE + "_" + str(i) + ".mp3") 
        i = i + 1

path = input()
text_arr = PdfToText(path)
TextToSpeech(text_arr)
