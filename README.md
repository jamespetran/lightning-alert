# Lightning Alert Program

## About

This program will print an alert if there is a lightning strike near a specified location. Lightning strike data is located in `./data/lightning.json`, with tracked location data in `./data/assets.json`.

If a lightning strike is a heartbeat strike (flashType == 9), it will not display an alert. 

Each location will receive only one alert. If there are subsequent strikes, disregard them, because the location already received their alert.

For lightning strikes the following rules apply:
- flashType=(0='cloud to ground', 1='cloud to cloud', 9='heartbeat')
- strikeTime=the number of milliseconds since January 1, 1970, 00:00:00 GMT

# Instructions to run the program

Clone the code from this repository into your IDE, grabbing data files and the filepaths. This program was created and tested with Python 3.9.10 64-bit. You will need python3 installed to be able to be guaranteed to run this code correctly.

When you're ready to run the code, enter the command `python3 solution.py` in your terminal to run the app.

## required libraries:
- [pyquadkey2](https://github.com/muety/pyquadkey2) (install with pip)

# Questions to answer:

> What is the [time complexity](https://en.wikipedia.org/wiki/Time_complexity) for determining if a strike has occurred for a particular asset?

answer #1 here

> If we put this code into production, but found it too slow, or it needed to scale to many more users or more frequent strikes, what are the first things you would think of to speed it up?

answer #2 here
