from ctypes import *
import platform


if platform.system() == 'Darwin':
    def setChanVolt(chan, volt):
        return "Using Mac OS, no S826 board available"

    def detectBoard():
        return "Using Mac OS, no S826 board available"
else:
    s826dll = cdll.LoadLibrary("./s826py_rev4.dll")
    id = s826dll.detectBoard()
    s826dll.SetVoltOut.argtypes = [c_int, c_int, c_float]


    def setChanVolt(chan, volt):
        s826dll.SetVoltOut(0, int(chan), float(volt))


    def detectBoard():
        return s826dll.detectBoard()



