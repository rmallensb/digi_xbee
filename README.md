# digi_xbee
 - Passively listens and logs received messages and corresponding RSSI

## Requirements
 - python3
 ```
 apt-get install python3
 ```
 - hexdump
 ```
 pip3 install hexdump
 ```
 - digi-xbee
 ```
 pip3 install digi-xbee
 ```

## Setup
 - Alter xbee COM port in `xbee_read.py` to correct path
 - Alter baud_rate in `xbee_read.py` to correct value
 - Alter logfile in `xbee_read.py` to desired logfile path

## To Run on Bootup
 - If done with sudo, adding the following line to your `/etc/rc.local` will work
 ```
 bash /home/pi/xbee_scan.sh
 ```
 - If done without sudo, add the following cronjob
 ```
 @reboot bash /home/pi/xbee_scan.sh
 ```
