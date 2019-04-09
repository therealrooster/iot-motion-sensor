import pycom
from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
import time

# Motion Sensor
py = Pytrack()
acc = LIS2HH12()
motion_data = []
start_time = time.ticks_ms()
pycom.heartbeat(False)

# pycom.rgbled(0xFF0000)  # Red
print('Data collection beginning...')
for i in range(500):
    x, y, z = acc.acceleration()
    # print(x, y, z, time.time())
    motion_data.append((x, y, z, time.ticks_diff(start_time, time.ticks_ms())))

# pycom.rgbled(0x00FF00)  # Green
