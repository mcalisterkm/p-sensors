#!/bin/sh
# init script for pm25 sensor
# Based on Michael Lanyon's Blog: 2015: Raspberry Pi Init Script

### BEGIN INIT INFO
# Provides:          pm-sensor-start
# Required-Start:    $remote_fs $syslog $network
# Required-Stop:     $remote_fs $syslog $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: init script for the pm sensor box
# Description:       particulate sensor startup
### END INIT INFO
# set -x

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
NAME=pm25
DAEMON=/home/pi/pm25.py
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
