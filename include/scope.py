__author__="ilker Parmaksiz"
from ds1054z import DS1054Z as rg
import csv
import sys
#from itertools import zip_longest
from itertools import zip_longest
from sys import stdout
from time import sleep
from decimal import *
#ip=raw_input("ip address of scope")
ip="169.254.1.5"
nwaveform=int(input("Number of Waveforms  ->  "))

scope=rg(ip)
#print(scope.idn)
# to start scope
# scope.write(":RUN")
def Set_ip(ip):
	scope=rg(ip)

def Save_Waveform(Ch,trig,slope,couple,n):
     # CHANneln
     #print n
        if(scope.query(":TRIGger:EDGe:SOURce?")!=Ch):
                        scope.write(":TRIGger:EDGe:SOURce" + " " + Ch)
                        print( scope.query(":TRIGger:EDGe:SOURce?") + " is choosen")
        else:
                        print( scope.query(":TRIGger:EDGe:SOURce?") + " is choosen")
     # AC, DC

        if(scope.query(":TRIGger:COUPling?")!=couple):
                        scope.write(":TRIGger:COUPling" + " " + couple)
                        print( scope.query(":TRIGger:COUPling?") + " is choosen")
        else:
                        print( scope.query(":TRIGger:EDGe:COUPling?") + " is choosen")


     # POSitive: rising edge,NEGative: falling edge, RFALl: rising/falling edge
        if(scope.query(":TRIGger:EDGe:SLOPe?")!=Ch):
                        scope.write(":TRIGger:EDGe:SLOpe" + " " + slope)
                        print( scope.query(":TRIGger:EDGe:SLOPe?") + " is choosen")
        else:
                        print( scope.query(":TRIGger:EDGe:SLOPe?") + " is choosen")

	#  0.16 == 160mv/div
     #if(scope.query(":TRIGger:EDGe:LEVel?")!=trig):
		#	scope.write(":TRIGger:EDGe:LEVel" + " " + trig)
		#	print( scope.query(":TRIGger:EDGe:LEVel?") + " is choosen")
     #else:
        print( scope.query(":TRIGger:EDGe:LEVel?") + " is choosen")
        trig=scope.query(":TRIGger:EDGe:LEVel?")
        count=0;
        while (count<n):
			#while (scope.query(":TRIGger:STATus?")=="WAIT"):
					#sleep(1)
					#wait= "-> Waiting to capture waveforms....."
					#stdout.write("\r%s" % wait)
					#stdout.flush()

                        while(scope.query(":TRIGger:STATus?")=="TD" and count<n): # returns  TD, WAIT, RUN, AUTO, or STOP
                                        data=[]
                                        filename="/home/ilker/scope/data/sipm2/72.5/" + Ch.lower() + "_Sipm2_72.5V_" + trig + "_" + str(count) + ".csv"
                                        data.append(scope.get_waveform_samples(Ch,"NORMal"))
                                        data.insert(0, scope.waveform_time_values_decimal)
                                        def csv_open(filename):
                                                return open(filename,"w")
                                        with csv_open(filename) as csv_file:
                                                        delimiter = ','
                                                        csv_writer = csv.writer(csv_file)
                                                        csv_writer.writerow(["TIME","Voltage"])
                                                        for vals in zip_longest(*data):
                                                                    vals = [vals[0]] + ['{:.2e}'.format(val) for val in vals[1:]]
                                                                    csv_writer.writerow(vals)

                                        tx="-> " + str(count) + " files are saved for " + Ch.lower()
                                        stdout.write("\r%s" % tx)
                                        stdout.flush()
                                        count+=1

        stdout.write("\n DONE!! \n")

#Saving waveforms to a file
#Save_Waveform("CHANnel1","-2.0","NEGative","DC",nwaveform)
#Save_Waveform("CHANnel2","-2.0","POSitive","DC",nwaveform)
Save_Waveform("CHANnel4","2.68","NEGative","AC",nwaveform)



