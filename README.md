# PdfCast

PdfCast is a utility that lets you convert a PDF to a podcast so you can listen to it instead of reading it. 

## Intallation:

You need to install the following libraries using `pip`.

* `pip install pdfminer`
* `pip install gTTS`
* `pip install selenium`

You also need to install a compatible version of the Chrome web driver and place it in the WebDrivers folder. You can find the latest releases here:

https://sites.google.com/a/chromium.org/chromedriver/downloads

You also need to enter your `Anchor` username and password into the  `login.py` file for selenium to work effectively. 

Please note that this projects was coded with Anchor in mind and will not work with other solutions. I acknowledge that this will not fit many peoples work flow and would consider developing a host agnostic folk if I see enough interest. 

Lastly, you need to supply your'e own pdf to get started.

I will be providing info on how to use the tool once I complete the functionality. For now, I intend on building a command line tool but if I see enough interest, I would consider adding a GUI.