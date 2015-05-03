import glob
import serial

port_detect = glob.glob("/dev/ttyUSB*")

try:
	print len(port_detect),"Ports detected"
	for i in range(0,len(port_detect)):
		print "Ports are:",port_detect[i]
	#print len(port_detect),"Port detected. Ports are:",port_detect[0]
except:
	print "No USB port detected....please check connection and/or power supply"



