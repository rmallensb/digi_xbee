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
 - Add following line to `/etc/rc.local` to have script run on bootup
 ```
 sudo python3 /home/pi/xbee_read.py &
 ```