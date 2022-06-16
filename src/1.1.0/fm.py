# This example demonstrates the FORCED MODE
# First with BSEC disabled
# Then with BSEC enabled

from bme68x import BME68X
from time import sleep

def read_conf(path: str):
    with open(path, 'rb') as conf_file:
        conf = [int.from_bytes(bytes([b]), 'little') for b in conf_file.read()]
        conf = conf[4:]
    return conf

def main():
	print('TESTING FORCED MODE WITHOUT BSEC')
	# bme = BME68X(cst.BME68X_I2C_ADDR_HIGH)
	sensor = BME68X(0x77, 0)
	print(f'INIT BME68X {sensor.init_bme68x()}')
	print(" year mon day h min sec  Tmp degC            Prs Pa         Hum %rH           GsR Ohm   Status")
	sleep(3)
	data = sensor.get_data()
	sleep(3)
	print(data)
	sleep(3)
	
	print()
	print('TESTING FORCED MODE WITH BSEC')
	default_conf = read_conf('/home/pi/BME688CheeseMeatDetector-main/bme68x-extension/BSEC_2.0.6.1_Generic_Release_04302021/config/generic_33v_3s_4d/bsec.config')
	print(f'SET BSEC CONF DEFAULT SELECTIVITY {sensor.set_bsec_conf(default_conf)}')
	BSEC_SAMPLE_RATE_HIGH_PERFORMANCE = 0.055556
	BSEC_SAMPLE_RATE_LP = 0.33333
	print(f'SUBSCRIBE STANDARD OUTPUTS {sensor.set_sample_rate(BSEC_SAMPLE_RATE_LP)}')
	print(f'SET HEATER PROFILE {sensor.set_heatr_conf(1, [320, 100, 100, 100, 200, 200, 200, 320, 320, 320], [150, 150, 150, 150, 150, 150, 150, 150, 150, 150], 2)}')
	#	bme = BME68X(cst.BME68X_I2C_ADDR_HIGH, bsec.BSEC_ENABLE)
	print(f'INIT BME68X {sensor.init_bme68x()}')
	sleep(3)
	print(sensor.get_bsec_state())
	sleep(3)
	print(sensor.get_bsec_data())
	sleep(3)

if __name__ == '__main__':
    main()

