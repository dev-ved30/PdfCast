# PdfCast

Ever been in a situation where you need to read a paper for school but can't cus you're attention span is too low? Yeah same.

So I made a bot do it for me. This tool will let you convert any PDF into a Podcast which you can listen to on your podcast player of choice [Pocket Cast FTW]

The way it work is:

* You give it a PDF 
* It gets converted to text
* The text gets converted to audio files using `gtts`
* The audio is uploaded to your podcast so you can listen to it.

## Intallation:

Assuming you have `Python` set up, you need to install the following libraries.

In your terminal, run:

* `pip install pdfminer`
* `pip install gTTS`
* `pip install selenium`

You also need to install a compatible version of the Chrome web driver and place it in the WebDrivers folder. You can find the latest releases here:

https://sites.google.com/a/chromium.org/chromedriver/downloads

## Set Up

You will need to add your `Anchor` username and password to the `login.py` file for selenium to work as intended. You will also need to add the absolute path of your project file to `login.py`.

Within Anchor, you will need to create a Podcast which will let `Selenium` create new episodes automatically. 

## Running

At this point, you should be able to use the utility. Please note that this is meant to be a command line tool.

You can run `main.py` from your terminal. The utility will walk you through all the steps and by the end of it, you should have your podcats up on Anchor.

You need to select the start and end page numbers, the first word of every chapter (Splitter) etc

Note: This projects was coded with Anchor in mind and will not work with other solutions. 

## Bugs

Please report any bugs in the `Issues` tab. I will try to solve them in a timely manner.

## Future

I created this project beacuse I didn't want to read a book for school. As it follows, the current implementation can be broken very easily. It's also uncomfortably reliant on `Anchor` for a large chunk of its functionality.

While this has worked for me, I acknowledge that it will not fit the work flow for many people. If there's enough interest, I would consider developing a host agnostic fork or recode the project entirely. Based on the feedback, I could also work on building a user interface to make the utility a little easier to use. 

As it stands, I will try to fix bugs and solve any major issues. 

If you're interested in working on the project, you can start off with a fork and get in touch to discuss the specifics. I'm always up for nerdy stuff!


