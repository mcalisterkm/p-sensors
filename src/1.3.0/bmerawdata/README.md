Bmerawdata - this is a mashup of Pi3G information and my own notes.
-------------------------------------------------------------------

!!!!NOTE: bmerwdata.py is not recording data in a format compatible with BME AI Studio. (SEPT 2023) !!!

This tool allows you to record and save data with your [BME688 Breakout Board](https://buyzero.de/products/luftqualitatssensor-bosch-bme688-breakout-board?_pos=2&_sid=985505100&_ss=r), so that it can be imported by [Boschs AI Studio](https://www.bosch-sensortec.com/software-tools/software/bme688-software/).
To use the smell detection feature of the BME688 you need to train an algorithm in AI Studio.
The algorithm requires lots of training and testing data, which you can record using this tool.
**[Read this guide](https://picockpit.com/raspberry-pi/teach-bme688-how-to-smell/)** for detailed instructions.

How to use the script

- Make sure your sensor is connected and working properly (check out the parallel_mode.py example in the examples folder to confirm)
- Download the bmerawdata folder
- Open a new project in AI Studio (at least version 1.7.1 since we need to export configurations for BSEC 2.2.0.0)
- (Optional) If you want to use your own configuration
  - Press Configure BME Board and save the Configuration file
  - It is advisable to use Heater Profile Exploration Mode and the RDC-1-0-Continuous Duty Cycle 
  - Copy the newly created **.bmeconfig** file into the bmerawdata folder
  - Edit the bmerawdata.py and in line 176 change the value of ai_conf to the name of your config file "your_name.bmeconfig".
- Execute the bmerawdata.py script to start recording data
- Press **Ctrl+C** to terminate the script
- The captured data will be saved as a **.bmerawdata** file that starts with the timestamp of creation
- Import that **.bmerawdata** file into AI Studio and label your specimen (You can record multiple specimens in one session, but you have to manually label them in AI Studio)

You may need to alter the raspbian zsh defaults to allow core dumps and increase heap memory. If you are seeing SIGSEGV errors then it is likely a memory issue, and to debug it is necessary to allow cores to be written. 

```
> ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 2906
max locked memory       (kbytes, -l) 65536
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 2906
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```
By default, core size is '0' (zero size core file) and "ulimit -c unlimitied" will allow an unlimitied sized core to be written. For heap "ulimit -s 32768" will make it 32MB. Your milage will vary, as bmerawdata.py builds all results in an internal memory array and when Ctrl-C (SIGINT, Kill -2 <pid>) is pressed it converts the data to JSON and writes it to file - the longer you record the more heap memory you will need.  The commands 'ps -ely' and  'prlimit --pid=<pid>' (pid is the process id) are helpful.


There are two variants of the original bmerawdata.py:
- bmerawdata-v1-4.py : This version tries to trap sensor null data errors and removes some redundant code. It retains the Ctrl-C to exit and save. Edit line 143 and change the value of ai_conf to the name of your config file "your_name.bmeconfig" 
- bmerawdata_sched.py   : This version runs for a specified time and then writes out the data and exits.
  Edit line 155 and change the value of ai_conf to the name of your config file "your_name.bmeconfig".
  Edit line 87 and change the number of seconds from the default 3600 (1 hour) It is intended to run as a background task which will ignore client timeout (SIGTERM) like this.  
```
$ nohup python3  bmerawdata_sched.py &
```

