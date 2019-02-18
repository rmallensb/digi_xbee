from digi.xbee.devices import XBeeDevice
from hexdump import hexdump

xbee_port = "/dev/ttyUSB0"
baud_rate = 9600
logfile   = "/home/pi/logfile.log"

device    = XBeeDevice(xbee_port, baud_rate)


def log(msg, rssi):

    lf = open(logfile, "a")

    lf.write("{}, {}\n".format(msg.data.decode(), rssi.decode()))
    lf.close()

def main():
    device.open()

    while True:
        try:
            # Returns an object
            # .remote_device
            # .data
            # .is_broadcast
            # .timestamp
            xbee_msg = device.read_data()
            if (xbee_msg):
                remote_device = xbee_msg.remote_device
                data          = xbee_msg.data

                # Returns rssi info in -dBm
                rssi = device.get_parameter("DB")
                
                log(xbee_msg, rssi)
                
                '''
                # DEBUG
                print("Received: {}\nFrom: {}".format(data, remote_device))
                hexdump(data)
                print("RSSI: {}".format(rssi))
                hexdump(rssi)
                print("\n")
                '''

        except KeyboardInterrupt:
            break

    device.close()


if __name__ == "__main__":
    main()
