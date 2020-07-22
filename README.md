# AnemometerDataCollector
Python3 script to read the measures from a Young ultrasonic anemometer and collect it in a Raspberry PI. 

Communication done via RS232. 

Anemometer Factory Default Serial Output:
  - RS232 at 38400 Baud
  - ASCII Text Serial String
      Wind Speed - 3D (m/s)
      Direction (Deg)
      Elevation (Deg)
      Speed of Sound (m/s)
      Sonic Temperature (°C)
      
Current parameters in the Anemometer (07/22/2020)
    BAUDS=    38400
    BYTESIZE= 8 bits
    STOPBITS= 1 bit
    PARITY=   None
    XONXOFF=  True
    msgSz=    30   (# of Bytes to read)
