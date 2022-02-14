<H1> Burn-in</H1>

The BME688 needs to be run initially for 24 hours as a burn-in process. During the burn-in process you need to show the sensor clean air and bad air, in order for it to improve the accuracy rating, which is on a scale of 0 to 3. Zero indicates stabilisation after power-on (unreliable), one indicates low accuracy, two indicates medium accuracy, and three indicates the best sensor performance. The various physical sensors have their own accuracy results and all do not progress in sync. 

To provide bad air during burn in I have used a paper towel soaked in hand sanitiser (~60% ethyl alcohol) placed close to the sensor (or in a plastic container placed over the sensor) for ~30 min for two or three times in the 24 hours. So if I run the burn-in overnight, I give it the hand sanitiser first for 30 min and then again a couple of times in the morning.  

The burn-in program sets the sensor in Low Power mode, which is a 3 sec cycle rate, and runs it for 24 hours and also checks the IAQ Quality for a value 3 (best accuracy). If these conditions are met then it writes out the sensor configuration and the sensor state. The files are written to a sub-directory called "conf", created if it does not exist, and each file generated includes a time stamp in the file name to avoid overwriting. 

I2C is used in all the BME688 boards I have seen and there are two I2C addresses (BME68X_I2C_ADDR_LOW - 0x76,
BME68X_I2C_ADDR_HIGH - 0x77) defined in the PI3G code. You will need to make sure the I2C value is correct (in the burn-in.py code) for your sensor. The command line `$ i2cdetect -y 1` will show what is present on the I2C bus. 

Headless running requires steps to work around time out and dis-connect, and the following command line runs python in a new process and ignores the HUP signal when your ssh session gets an idle time out: 
```
$ nohup python3 burn_in.py &. 
```
Output goes to nohup.out and you can check on progress by tailing the file:
```
$ tail nohup.out
```

Two files are written conf_data<time-stamp>.txt and state_data<time-stamp>.txt
The PI3G code uses a default config which is good, but the sensor can take a long time to stabilise. Loading the state file saved during burn-in reduces this to ~5min for accuracy 2 and < 10 min for accuracy 3.

Both the config and state api calls from PI3G require an array of Int to be passed in, and that means processing the .txt files before passing in the data.  In the BOSCH C API code they are binary files. 

In read_conf.py the function `readState(state_file_name)` reads the state file and returns an array of Int values that is then passed in to `bme.set_bsec_state(state_int)` to set the sensor state to the burn-in values.  The code then loops round gets and prints the sensor data to the terminal.

Change to following values in read_conf.py
 `state_file_name = "state_data1644485092616.txt"` # change to match your state file name in ./conf
`bme = BME68X(cnst.BME68X_I2C_ADDR_LOW, 0)`  # Change to the I2C value for your BME688 sensor







