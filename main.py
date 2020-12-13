from pdfminer.high_level import extract_text
from tkinter import Tk, filedialog
from gtts import gTTS
import os

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
    """
    This function takes the path to a PDF from the START to END page numbers, 
    converts it to a String, splits it along the splitter, and returns the list
    of Strings.

    Args:
        path (String): [The path to the PDF file]

    Returns:
        [List]: [A list of Strings made up of the PDF text split across the SPLITTER]
    """
    text = extract_text(path, page_numbers = range(START, END))
    arr = text.split(SPLITTER)
    return arr

def TextToSpeech(text_arr):
    """
    Thie function takes an array of Strings and converts each String to an MP3 clip. It
    also saves them locally.

    Args:
        text_arr ([List]): [A list of Strings that need to converted to MP3 clips.]
    """
    language = 'en'
    i = 1
    if not os.path.exists("results"):
        os.mkdir("results")
    for text in text_arr:
        recording = gTTS(text=text, lang=language, slow=False) 
        recording.save("results/" + FILE + "_" + str(i) + ".mp3") 
        print("Done with Chapter " + str(i))
        i = i + 1

def UploadToRSS():
    print("Test")

path = input()
text_arr = PdfToText(path)
TextToSpeech(text_arr)
