# Micropython
Repository for Micropython breadboard projects on the Rpi Pico and the Esp32.

## RFID Music Player
Plays a tune on a WS2812 buzzer using a Raspberry Pi Pico. I saved the song pattern on an RFID tag so that each scan could play a portion of the song off of each tag.

## Raspberry Pi Pico Themometer and Humidity Sensor
This program reads from a DHT11 temprature/humidity sensor and a temprature sensor. It reads the temprature in F and also gives the relative humidity, and displays the results on a Lcd1602 screen every 2 seconds.

## uConfig
uConfig is a custom configuration parser I wrote in MicroPython that provides similar functionality to the configparser library in CPython. It reads a configuration file and stores the values in a dictionary, where each section in the file corresponds to a key in the dictionary and each key-value pair in the section corresponds to a key-value pair in the dictionary. The config reader program allows for flexible reading of any number of sections and key-value pairs in a configuration file, making it suitable for use in MicroPython projects.
