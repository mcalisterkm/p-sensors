# This example demonstrates the FORCED MODE
# First with BSEC disabled
# Then with BSEC enabled

from bme68x import BME68X
import bme68xConstants as cst
import bsecConstants as bsec
from time import sleep

def read_conf(path: str):
    with open(path, 'rb) as conf_file:
        conf = [int.from_bytes(bytes([b]), 'little') for b in conf_file.read()]
        conf = conf[4:]
    return conf

default_config = read_conf("/home/pi/BME688CheeseMeatDetector-main/bme68x-extension/BSEC_2.0.6.1_Generic_Release_04302021/config/generic_33v_3s_4d/'2021_04_29_02_51_bsec_h2s_nonh2s_2_0_6_1 .config'")

print('TESTING FORCED MODE WITHOUT BSEC')
bme = BME68X(cst.BME68X_I2C_ADDR_HIGH, bsec.BSEC_DISABLE)
print(bme.get_data())
sleep(3)
print()
print('TESTING FORCED MODE WIT BSEC')
bme = BME68X(cst.BME68X_I2C_ADDR_HIGH, bsec.BSEC_ENABLE)
print(bme.get_bsec_data())
sleep(3)
