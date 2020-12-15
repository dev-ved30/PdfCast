from pdfminer.high_level import extract_text
from tkinter import Tk, filedialog
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

PATH = "WebDrivers/chromedriver"

PODCAST_NAME = ""
EMAIL = ""
PASSWORD = ""

START = 26
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
    if not os.path.exists("resutls/" + FILE):
        os.mkdir("results/" + FILE)
    for text in text_arr:
        print(text)
        recording = gTTS(text = text, lang = language, slow = False) 
        recording.save("results/" + FILE + "/" + FILE + "_" + str(i) + ".mp3") 
        print("Done with Chapter " + str(i))
        i = i + 1

def UploadPodcast():


    driver = webdriver.Chrome(PATH)

    # Opening the website
    driver.get("https://anchor.fm/dashboard/episode/new")

    a = driver.page_source
    # Entering Email
    email = driver.find_element_by_id("email")
    email.send_keys(EMAIL)

    # Entering Password
    password = driver.find_element_by_id("password")
    password.send_keys(PASSWORD)

    # Pressing Enter
    password.send_keys(Keys.RETURN)

    # Waiting for new code to be read by selenium
    time.sleep(5)

    # Clicking the button to open file dialog
    # uploader = driver.find_element_by_class_name("styles__uploadAudioIcon___1BcDm").click()
    driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/input").send_keys("/Users/ved/Documents/Projects/PdfCast/results/Coders/Coders_1.mp3")
    #keys = uploader.send_keys()

    #uploader.send_keys(Keys.RETURN)

    
    time.sleep(100)
    driver.quit()



#path = input()
#text_arr = PdfToText(path)
#TextToSpeech(text_arr)
UploadPodcast()