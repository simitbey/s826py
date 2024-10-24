# s826py -> Controlling the Sensoray 826 PCIE Expansion Board with Python

The s826py allows robust control of voltage for channels that the Sensoray 826 PCIE Expansion Board use.

# Usage
1. Place all the files in the working directory

2. Import s826 controller using this code:
   ```py
   from s826 import setChanVolt, detectBoard
   ```
You have succesfully imported the methods setChanVolt and detectBoard.
Here's an example code for the usage:
```py
setChanVolt(chan=4, volt=5)
```

You have succesfully set the voltage for channel 4 to 5 volts.
   
