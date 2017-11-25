# PiStand
![alt text](https://github.com/benja239/PiStand/blob/master/PiStand%20Time.jpg)
Raspberry Pi 3 with 2 8x8 dot matrices

This project is using a Raspberry Pi 3, 2 8x8 dot matrices (via 2 MAX7219 LED Display drivers) and python 3.My aim is to use this display for a number of different functions. Currently getting to grips with using python with the MAX7219's to create a digital clock with scrolling text.

+This project largely uses JonA1961's MAX7219array code (found here: https://github.com/JonA1961/MAX7219array) for interfacing with the dot matrix. From his code, I use various methods to write values to the display registers and also the fonts for the 8x8 dot matrix. In his code however, the fonts are stored to be used where the displays are vertical. I wanted them to be horizontal so have recreated the fonts in another orientation.

---
### Future Aims
* Alarm clock
* Use Calendar API from Google Calendar to then display the next event in my calendar with a title, location (University
room) and time, as well as displaying the current time in between.
* Google assistant API implementation and integration with the display.
