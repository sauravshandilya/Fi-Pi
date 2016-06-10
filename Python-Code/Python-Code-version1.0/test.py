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

pi.forward_mm(200)
time.sleep(2)
pi.back_mm(300)

time.sleep(2)

	pi.servo_1(0)
	pi.servo_2(0)
	time.sleep(0.5)
	
	pi.servo_1(120)
	pi.servo_2(120)
	
	time.sleep(0.5)

	
	pi.servo_1_free()
	pi.servo_2_free()
'''
pi.led_bargraph_off(0)
time.sleep(1)
pi.led_bargraph_on(pi.barLED6)
time.sleep(1)

pi.serial_close()
