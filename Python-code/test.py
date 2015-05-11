import fipi as pi 
import time

pi.serial_open()	

'''
fipi.forward()
time.sleep(1)
fipi.stop()
time.sleep(0.5)
fipi.back()
time.sleep(1)
fipi.stop()
time.sleep(0.5)
time.sleep(0.5)
'''
pi.forward_mm(200)
time.sleep(2)
pi.back_mm(300)
time.sleep(2)


pi.serial_close()
