#!/usr/bin/python3

# Script to perform RS-232 communication between a Raspberry PI and a ultrasonic anemometer (yoUNG, MODEL 81000)
# Check the current values in the amenometer before staring reading any measure. The parameters froim factory are:
# Serial output 
#  - RS232 at 38400 Baud
#  - ASCII Text Serial String
# Wind Speed - 3D (m/s)
# Direction (Deg)
# Elevation (Deg)
# Speed of Sound (m/s)
# Sonic tempertature (Centigrades)

# To list available serial ports, you can use the command:  python3  -m serial.tools.list_ports (if using python 2.7, use python or python2 instead of python3) 


import serial
import datetime
import sys





def create_fileName():
    #get current date
    dt= datetime.datetime.today()
    fileName= 'dataFromAnemometer_'+str(dt.year)+'_'+str(dt.month)+'_'+str(dt.day)+'_'+str(dt.hour)+'_'+str(dt.minute)+'_'+str(dt.second)+'.log'
    return fileName


def rs232_connection(PORT, BAUDS, BYTESIZE, PARITY, STOPBITS, XONXOFF):
    print(' - Initalizing serial')
    rs232= serial.Serial(PORT, BAUDS, bytesize= BYTESIZE, parity= PARITY, stopbits= STOPBITS, xonxoff=XONXOFF )
    print(' - Opening serial port')
    # Check if the serial port is already Open
    if (rs232.is_open== False):
        rs232.open()
    else:
        print(' - Connection stablished')

    #Empty the buffer 
    rs232.flushInput()  
    return rs232


def read_data(rs232, msgSz):
    # in each iteration, read : speed (m/s), azimuth (deg),  elevation (deg),  speed-of-sound (m/s),  sonic-temperature (°C).
    # as data is in ASCII, we need to take into account the empty spaces sent in the message.
    msg= rs232.read(size=msgSz)
    msgConverted= msg.decode('cp1252')
    # print(str(readCounter)+ ' --> ' + msgConverted)
    return msgConverted


def save_data(fileName, msgLine):
    # write data from serial port into file
    with open(fileName, 'a') as outputFile:
        outputFile.write(msgLine)
        outputFile.write('\n')
        outputFile.flush()


def close_serial_conn(rs232):
    print('closintg RS232 conn.')
    rs232.close()   



# --- MAIN ---
if __name__=='__main__':   
    # ----- SERIAL RS232 parameters. -----
    # If values changed in the Anemometer, we need to change this values
    PORT= '/dev/ttyUSB0'
    BAUDS= 38400
    BYTESIZE= serial.EIGHTBITS
    STOPBITS= serial.STOPBITS_ONE
    PARITY= serial.PARITY_NONE
    XONXOFF= True
    msgSz= 30       #Size in BYTES of 1 full msg from anemometer. msg send as ASCII (1 Byte per char (empty spaces included)
    # ----- -----

    # Build the name of the file to save current lecture data
    fileName= create_fileName()

    # Establish a rs232 connection
    rs232Conn= rs232_connection(PORT, BAUDS, BYTESIZE, PARITY, STOPBITS, XONXOFF)

    while True:
        msg= read_data(rs232Conn, msgSz)
        save_data(fileName, msg)

