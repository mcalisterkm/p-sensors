# p-sensors
## Example code using the Bosch BME688/PI3G Python wrapper and Adafruit PMSA003I PM25 Air Quality Sensor.

The BME688 is a multi-function I2C sensor for temp, pressure, humidity and gas sensing. The PI3G library provides a wrapper on the BOSCH binary.  My directories for the BME688/PI3G follow the PI3G releases - 1.1, 1.3, etc. I suggest using the latest 1.3 code. If you are starting out with the BME688 have a look at my burn-in code and saving/loading the sensor configuration. 

The PM25 sensor from Adafruit comes with I2C interface, in a very small format. The sensor runs at a low 100 MHz and my code uses I2C bus 3 keeping this device separate from the high speed I2C running on the standard bus. 

There are notes in each folder of what I was trying to do with these sensors. Both sensors have library dependencies which are explained in the notes, and I use PI Zero 2 boards with Raspbian Buster. The BOSCH BSEC library is 32bit so expect to hit barriers if you are runing a 64 bit OS.  



