#!/bin/sh
#
# init script for bme688 sensor
# Based on Michael Lanyon's Blog: 2015: Raspberry Pi Init Script
#

### BEGIN INIT INFO
# Provides:          bme-sensor-start
# Required-Start:    $remote_fs $syslog $network
# Required-Stop:     $remote_fs $syslog $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: init script for the Bosch bme688 sensor
# Description:       BME688 sensor startup
### END INIT INFO

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
NAME=bme
DAEMON=/home/pi/sensor_app_1-3-0.py
DAEMONARGS=""
PIDFILE=/var/run/$NAME.pid
LOGFILE=/var/log/$NAME.log

. /lib/lsb/init-functions

test -f $DAEMON || exit 0

case "$1" in
    start)
        start-stop-daemon --start --background \
            --pidfile $PIDFILE --make-pidfile --startas /bin/bash \
            -- -c "exec stdbuf -oL -eL /usr/bin/python3 $DAEMON $DAEMONARGS > $LOGFILE 2>&1"
        log_end_msg $?
        ;;
    stop)
        start-stop-daemon --stop --pidfile $PIDFILE
        log_end_msg $?
        rm -f $PIDFILE
        ;;
    restart)
        $0 stop
        $0 start
        ;;
    status)
        start-stop-daemon --status --pidfile $PIDFILE
        log_end_msg $?
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 2
        ;;
esac

exit 0

To make the Raspberry Pi use your init script at the right time,
one more step is required: running the command
# sudo update-rc.d <myservice.sh> defaults.