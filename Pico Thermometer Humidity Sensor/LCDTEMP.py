#TEMP TO DISPLAY
from machine import Pin, I2C
import utime as time
from dht import DHT11
from lcd1602 import LCD
import math

#Temp Sensor
pin = Pin(16, Pin.OUT, Pin.PULL_UP)
sensor = DHT11(pin)

#LCD
lcd = LCD()

# Thermister setup
thermistor = machine.ADC(28)  
def therm():
    temperature_value = thermistor.read_u16()
    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    Fah = Cel * 1.8 + 32
    return Fah

while True:
    sensor.measure()
    temp = sensor.temperature
    # (0°C × 9/5) + 32 = 32°F
    temp_f = (int(temp)*(9/5)) +32
    t = therm()
    print("Temp: {}°F, Humidity: {}".format(temp_f, sensor.humidity))
    lcd.message("Temp: {}°F,\nHumidity: {}".format(t, sensor.humidity))
    time.sleep(2)
    #lcd.clear()
    