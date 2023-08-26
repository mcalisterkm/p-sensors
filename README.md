# p-sensors
## Example Python code examples for the Bosch BME688/PI3G library and Adafruit PMSA003I PM25 Air Quality Sensor.

The BME688 is a multi-function I2C sensor for temp, pressure, humidity and gas sensing. This project contains python code to burn in the BME688 sensor and save/load the state of the BME688 sensor, and examples of outputting the BME688 data to an OLED display. Saving and loading the burned in sensor configuration helps it to get up to speed quicked from a cold start. 

The PM25 particulate matter sensor from Adafruit comes with I2C interface, in a very small format. The sensor runs at a low 100 MHz and my code uses I2C bus 3 keeping this device separate from the high speed I2C running on the standard bus. 

There are notes in each folder of what I was trying to do with these sensors. Both sensors have library dependencies which are explained in the notes, and I use PI Zero 2 boards with Raspbian Buster. I run raspbian os on various flavours of respberry pi, largely 32bit raspbian as that is what the Bosch Sensortec library supported, however Pi4 and 64bit raspbian is becoming more common and BOSCH have recently released a 64bit BSEC 2 library.   



