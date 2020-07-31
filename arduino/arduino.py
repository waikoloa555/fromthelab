#python run temperature logger

import serial

date = input("Enter the date (00/00/0000): ")
start = input("Enter the time (00:00:00): ")


#print start
arduino = serial.Serial('COM3', 9600, timeout=.1)
#if True:
time = input("How often would you like to record the temperature (s)?")
rate = int(time)*1000
ardRate = str(rate)
arduino.write(ardRate)
ardTEMP = open("thermoLOG.txt","a")#opens .txt file and records data
#ardTEMP.write("Start time: ")
ardTEMP.write('Date,')
ardTEMP.write(date)
ardTEMP.write('\n')
ardTEMP.write('Time (s),')
ardTEMP.write(str(time))
ardTEMP.write('\n')
ardTEMP.write(start)
ardTEMP.write(', ')

ready = False #initialize

try:
        while True:
                data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
                if data == 'Internal Temp, C, F': #don't record until beginning of new data
                        ready = True
                if data == 'Internal Temp1, Internal Temp2, C1, C2, F1, F2,':
                        ready = True
                if ready:
                        if data:
                                print(data)
                                ardTEMP.write(data)
                                ardTEMP.write('\n')

		


except KeyboardInterrupt: #type ctrl-C to end
	print('\nDone.')
	ardTEMP.close()



#use temperature_recorder arduino code
