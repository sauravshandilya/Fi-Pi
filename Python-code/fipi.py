import serial
import time 
import glob			# Glob module finds all the pathnames matching a specified pattern. It is used for detecting serial port in linux 
import sys			# This module provides access to some variables used or maintained by the interpreter. It is used to exit from program when exception occur

########### Variable declaration
global device_id 
global device_type 
global function_type 
global param_count
global port
global port_detect

def serial_port_connection(port_detect):
	global port 
	
	print len(port_detect),"Ports detected" # print number of ports detected
	
	#------------- print all detectec ports - STARTS ---------#
	if (len(port_detect) != 0):				
		print "Port(s) detected is/are:"	
		
		for i in range (0,len(port_detect)):
			print port_detect[i]
	#------------- print all detectec ports - END ---------#
	
	#------------- connect to PORT if only one port is detected - STARTS ---------#
		if (len(port_detect) == 1):
			port = serial.Serial(port_detect[0],baudrate=9600)
			print "connected to: ", port_detect[0]
	#------------- connect to PORT if only one port is detected - END ---------#	
	
	#------------- Ask for user i/p if more then one port is detected - STARTS ---------#
		else:
			for i in range(0,len(port_detect)):
				print "Enter",i,"to connect to:",port_detect[i]
			
			y = int(raw_input("Enter your choice of connection: "))
			
			while y >= len(port_detect):
				print "Invalid choice"
				for i in range(0,len(port_detect)):
					print "Enter",i,"to connect to:",port_detect[i]
				y = int(raw_input("Enter your choice of connection: "))
	#------------- Ask for user i/p if more then one port is detected - END ---------#			
			
			port = serial.Serial(port_detect[y],baudrate=9600)
			print "connected to: ", port_detect[y]
	return
		
def serial_open():	
	port_detect = glob.glob("/dev/ttyUSB*") # stores all /dev/ttyUSB* into a list port_detect
	
	try:
		serial_port_connection(port_detect)
				
		if port.isOpen() == True:
			print "Port is open"
		else:
			serial_port_connection()
				
	except:
		print "No USB port detected....check connection"
		sys.exit(0)		# stop program execution when exception occur

def forward ():
	 print "In forward"
	 data = []
	 device_id = 2				#DC Motors has device id = 2
	 device_type = 1			#DC Motors is o/p device. hence device type = 0	
	 function_type = 0			#Function_type = 0 for forward motion 
	 param_count = 0			#No parameter is sent through forward function hence param_count = 0
	 data.append(chr(device_id))
	 data.append(chr(device_type))
	 data.append(chr(function_type))
	 data.append(chr(param_count))
	 data.append("\n")
	 data.append("\r") 
	 
	 for i in range(0,len(data)):
		 port.write(str(data[i]))
		 print str(data[i])
	 #port.write(str(device_id))
	 #print "device_id =", device_id
	 #port.write(str(device_type))
	 #port.write(str(function_type))
	 #port.write(str(param_count))
	 #port.write("\n")
	 #port.write("\r")
	 print "packet sent is" , str(data)
	 return

def back ():
	 print "In forward"
	 data = []
	 device_id = 2				#DC Motors has device id = 2
	 device_type = 1			#DC Motors is o/p device. hence device type = 0	
	 function_type = 1			#Function_type = 0 for forward motion 
	 param_count = 0			#No parameter is sent through forward function hence param_count = 0
	 data.append(chr(device_id))
	 data.append(chr(device_type))
	 data.append(chr(function_type))
	 data.append(chr(param_count))
	 data.append("\n")
	 data.append("\r") 
	 
	 for i in range(0,len(data)):
		 port.write(str(data[i]))
		 print str(data[i])
	 #port.write(str(device_id))
	 #print "device_id =", device_id
	 #port.write(str(device_type))
	 #port.write(str(function_type))
	 #port.write(str(param_count))
	 #port.write("\n")
	 #port.write("\r")
	 print "packet sent is" , str(data)
	 return
	 
def stop ():
	 print "in Stop"
	 device_id = 2
	 device_type = 1
	 function_type = 4
	 param_count = 0
	 port.write(chr(device_id))
	 port.write(chr(device_type))
	 port.write(chr(function_type))
	 print "function_type =",function_type
	 port.write(chr(param_count))
	 port.write("\n")
	 port.write("\r")
	 return

def buzzer_on():
	 device_id = 1
	 device_type = 1
	 function_type = 0
	 param_count = 0
	 port.write(chr(device_id))
	 port.write(chr(device_type))
	 port.write(chr(function_type))
	 port.write(chr(param_count))
	 port.write("\n")
	 port.write("\r")
	 return
	
def buzzer_off():
	 device_id = 1
	 device_type = 1
	 function_type = 1
	 param_count = 0
	
	 port.write(chr(device_id))
	 port.write(chr(device_type))
	 port.write(chr(function_type))
	 port.write(chr(param_count))
	 port.write("\n")
	 port.write("\r")
	 return

def velocity(left_motor,right_motor):
	data = []
	device_id = 2
	device_type = 1
	function_type = 9
	param_count = 2
	param_1 = left_motor
	param_2 = right_motor
	data.append(chr(device_id))
	data.append(chr(device_type))
	data.append(chr(function_type))
	data.append(chr(param_count))
	data.append(chr(param_1)) 
	data.append(chr(param_2))
	data.append("\n")
	data.append("\r") 
	 
	for i in range(0,len(data)):
		port.write(str(data[i]))
		print str(data[i])
	print "packet sent is ", str(data)
	return

def forward_mm(distanceinmm):
	data = []
	device_id = 3
	device_type = 1
	function_type = 0
	param_count = 1
	param_1 = distanceinmm
	data.append(chr(device_id))
	data.append(chr(device_type))
	data.append(chr(function_type))
	data.append(chr(param_count))
	data.append(chr(param_1)) 
	data.append("\n")
	data.append("\r") 
	 
	for i in range(0,len(data)):
		port.write(str(data[i]))
		print str(data[i])
	print "packet sent is ", str(data)
	return

def back_mm(distanceinmm):
	data = []
	device_id = 3
	device_type = 1
	function_type = 1
	param_count = 1
	param_1 = distanceinmm
	data.append(chr(device_id))
	data.append(chr(device_type))
	data.append(chr(function_type))
	data.append(chr(param_count))
	data.append(chr(param_1)) 
	data.append("\n")
	data.append("\r") 
	 
	for i in range(0,len(data)):
		port.write(str(data[i]))
		print str(data[i])
	print "packet sent is ", str(data)
	return	
	
def adc_conversion(channel_no):
	data = []
	device_id = channel_no
	device_type = 0			# sensors are input so device_type is 0
	function_type = 0
	param_count = 0
	data.append(chr(device_id))
	data.append(chr(device_type))
	data.append(chr(function_type))
	data.append(chr(param_count))
	data.append("\n")
	data.append("\r") 
	
	for i in range(0,len(data)):
		port.write(str(data[i]))
		#print str(data[i])
	print "packet sent is ", str(data)
	
	ret = port.read()
	print "channel no:",channel_no, "returned: ", '%s' %str(ord(ret))
	
	return		
	
