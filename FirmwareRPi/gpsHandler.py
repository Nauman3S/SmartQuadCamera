import serial
import time
import string
import pynmea2

# Get GPS Data


def getData():
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline().decode('unicode_escape')
    lat=""
    lng=""

    if newdata[0:6] == "$GPRMC":# use cat /dev/ttyAMA0 to get the name
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
        print(gps)
    return [lat,lng]
   