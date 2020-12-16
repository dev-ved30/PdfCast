
from pdfminer.high_level import extract_text
from tkinter import Tk, filedialog
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login import EMAIL, PASSWORD, PROJECT_PATH
import os
import time
import sys

PATH = "WebDrivers/chromedriver"

START = 0
END = 0
SPLITTER = ""


def inputPdf():
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
    SPLITTER = str(input("Enter the splitter: "))
    START = int(input("Enter the start page: "))
    END = int(input("Enter the end page: "))
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
        recording = gTTS(text = text, lang = language, slow = False) 
        recording.save("results/" + FILE + "/" + FILE + "_" + str(i) + ".mp3") 
        print("Done with Chapter " + str(i))
        i = i + 1

def UploadPodcast(lenght):
    """
    This is a function that uploads the audio files to your Anchor Podcast. Once you add your
    project path and credentials to the login.py file, it will log you in and upload all the audio files.

    Args:
        lenght ([int]): [Number of audio files generated]
    """

    driver = webdriver.Chrome(PATH)

    # Opening the website
    driver.get("https://anchor.fm/dashboard/episode/new")

    print("Current email: " + EMAIL)
    change = input("Do you want to log in with this account? (y/n)")

    if change == "n":
        print("You can change your account details in login.py")
        driver.quit()
        sys.exit()

    # Entering Email
    email = driver.find_element_by_id("email")
    email.send_keys(EMAIL)

    # Entering Password
    password = driver.find_element_by_id("password")
    password.send_keys(PASSWORD)

    # Pressing Enter
    password.send_keys(Keys.RETURN)

    i = 1

    for element in range(lenght):

        # Waiting for new code to be read by selenium
        time.sleep(5)

        # Clicking the button to open file dialog
        xPath = "/html/body/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/input"
        driver.find_element_by_xpath(xPath).send_keys(PROJECT_PATH + FILE + "/" + FILE + "_" + str(i) + ".mp3")
        
        # Waiting for file to upload
        time.sleep(30)

        # Click on the save episode button
        driver.find_element_by_class_name("styles__saveButton___lWrNZ").click()

        # Waiting for new code to be read by selenium
        time.sleep(5)    

        # Filling up the podcast details
        driver.find_element_by_class_name("styles__modeToggleText___26-xx").click()
        driver.find_element_by_id("title").send_keys(FILE)
        driver.find_element_by_class_name("styles__textarea___2-sXZ").send_keys("Episode " + str(i))

        # Pressing publish
        driver.find_element_by_class_name("styles__saveButtonWrapper___TrQYl").click()

        #Returning to publish page
        driver.get("https://anchor.fm/dashboard/episode/new")
        i = i + 1

        time.sleep(3)
    driver.quit()

path = inputPdf()
text_arr = PdfToText(path)
TextToSpeech(text_arr)
UploadPodcast(len(text_arr))