#!/usr/bin/python3
#
# This version works with an SPI connected OLED SH1106 screen 128 x 128
# It uses the luma and pillow library and expects fonts to be in a fonts subdirectory.
# This code will not run without running the burn_in.py code and getting a saved state file from the 24 hour burn-in.
# Edit the state_file_name to reference your saved state file.
#
from bme68x import BME68X
import bme68xConstants as cst
import bsecConstants as bsec
from time import sleep, time
from pathlib import Path
from PIL import ImageFont
from luma.core.render import canvas
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010

temp_prof = [320, 100, 100, 100, 200, 200, 200, 320, 320, 320]
dur_prof =[5, 2, 10, 30, 5, 5, 5, 5, 5, 5]

# Amend this to your state file name
state_file_name = "state_data1644485092616.txt"

def get_screen1():
    # serial = i2c(port=1, address=0x3C)
    serial = spi(port=0, device=1, cs_high=True, gpio_DC=9) 
    # disp_device1 = ssd1306(serial, width=128, height=64, rotate=0)
    disp_device1 = sh1106(serial, width=128, height=128, rotate=2)
    return disp_device1

def disp_template_1(avg_temp, avg_humidity, avg_pressure, aiq, co2, gas, disp_device1):
    font_path = str(Path(__file__).resolve().parent.joinpath('fonts', 'C&C Red Alert [INET].ttf'))
    font2 = ImageFont.truetype(font_path, 18)
    with canvas(disp_device1) as draw:
        draw.rectangle(disp_device1.bounding_box, outline="white", fill="black")
        draw.text((5, 2), avg_temp , font=font2, fill="white")
        draw.text((5, 20), avg_humidity , font=font2, fill="white")
        draw.text((5, 40), avg_pressure , font=font2, fill="white")
        draw.text((5, 60), aiq , font=font2, fill="white")
        draw.text((5, 80), co2 , font=font2, fill="white")
        draw.text((5, 100), gas , font=font2, fill="white")


def readstate(state_file_name):
    state_path = str(Path(__file__).resolve().parent.joinpath('conf', state_file_name))
    state_file = open(state_path, 'r')
    # strip the brackets [.....]
    state_str =  state_file.read()[1:-1]
    # split on delimiter ,
    state_list = state_str.split(",")
    state_int = [int(x) for x in state_list]
    return(state_int)

def get_data(sensor):
    data = {}
    try:
        data = sensor.get_bsec_data()
    except Exception as e:
        print(e)
        return None
    if data == None or data == {}:
        sleep(0.1)
        return None
    else:
        sleep(3)
        return data
def main():
    while True:
        # print(bme.get_bsec_data())
        # sleep(1)
        data = bme.get_bsec_data()
        print(data)
        if data == None or data == {}:
            sleep(1)
        else:
            temp = "Temperature: " + "{: ^4.1f}".format(data['temperature']) + " \u00B0"+ "C"
            hum = "Humidity: " +  "{: ^4.1f}".format(data['humidity']) + "%"
            pres = "Pressure: " + "{: ^4.1f}".format((data['raw_pressure'] / 100))  + " hPa" # sensor reports in pascals so /100 for hpa
            iaq =  "IAQ: " +  "{: ^4.1f}".format(data['iaq'])
            co2 = "CO2: " + "{: ^4.1f}".format(data['co2_equivalent'])  + "ppm"
            gas = "Raw Gas: " + "{: ^4.1f}".format(data['raw_gas'])
            disp_template_1(temp, hum, pres, iaq, co2 , gas, disp_device1)


print('SETTING UP BME688')
bme = BME68X(cst.BME68X_I2C_ADDR_HIGH, 0)
bme.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)
print(bme.get_variant())
print(bme.set_heatr_conf(cst.BME68X_ENABLE, temp_prof, dur_prof, cst.BME68X_SEQUENTIAL_MODE))
sleep(0.5)
state_int = readstate(state_file_name)
print(bme.set_bsec_state(state_int))
# Offset calibrated in the BSEC Library.
print(bme.set_temp_offset(2))
print("BME688 Config set....")

if __name__ == '__main__':
    try:
        disp_device1 = get_screen1()
        main()
    except KeyboardInterrupt:
        pass
