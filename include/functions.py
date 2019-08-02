
__author__="ilker Parmaksiz"

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from con import Ui_Dialog
from guiscope2 import Ui_MainWindow

from ds1054z import DS1054Z as conn
import csv, time

from Waveform import *
from itertools import zip_longest

import sys
import configparser

class Functions(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Functions,self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi( self )
        self.config = configparser.ConfigParser()
        self.stop=False;


    def WritetheConfig(self,ip):
        self.config['Default'] = {"Ip": ip}
        with open( 'config/config.ini', '+w' ) as configfile:
            self.config.write( configfile )
        configfile.close()
        message=ip + " has been written to config and set as default ip address"
        self.WriteToStatusBar(message,1000)


    #Prints to textBrowser
    def Write(self,_str):
        str=self.textBrowser
        str.append(_str)




    def WriteToStatusBar(self,_str,timems):
        self.statusbar.showMessage( str(_str), int(timems) )

    #Print it to same line
    def WriteSame(self,_str):
        TextB = self.textBrowser
        Text_Cursor = TextB.textCursor()
        TextB.append( _str )
        TextB.moveCursor( Text_Cursor.End, Text_Cursor.MoveAnchor )
        TextB.moveCursor( Text_Cursor.StartOfLine, Text_Cursor.MoveAnchor)
        TextB.moveCursor( Text_Cursor.End, Text_Cursor.KeepAnchor )
        Text_Cursor.removeSelectedText()
        Text_Cursor.deletePreviousChar()



    def Clear(self):
        self.textBrowser.clear()

    def HideProgressbar(self):
        self.progressBar.hide()
        self.label_4.hide()
    def ShowProgressbar(self):
        self.progressBar.show()
        self.label_4.show()

    #Exits the program
    def Exit(self):
        QApplication.quit() #or -> sys.exit(1)

    def WaveFormViewer(self):

        self.ui=waveformViewer()
        self.ui.show()






    #Opens Connection Dialog
    def Connect(self):
        Dialog=QDialog()
        ui = Ui_Dialog()
        ui.setupUi( Dialog )
        ui.Ip.setText( str( self.getIp() ) )
        Dialog.show()
        Dialog.exec_()


        if(Dialog.result()==1):
            ip=str(ui.Ip.toPlainText())
            self.WritetheConfig(ip)
            self.isConnection()
        elif(Dialog.result()==0):
            self.WriteToStatusBar("Ip change is canceled!",1000)




    #Get the ip
    def getIp(self):
        Dialog=QDialog()
        get = Ui_Dialog()
        get.setupUi(Dialog)
        ip=str(get.Ip.toPlainText())
        self.config.read('config/config.ini')
        if('Default' in self.config):
            ip=self.config['Default']["Ip"]
        else:
            self.WritetheConfig(ip)

        #set the new Ip so you can see
        get.Ip.setText( str( ip ) )
        #ip address validation
        return ip


        #When SaveWaveform Button is pressed
    def StartCaptureWaveforms(self):

        n=self.textEdit.toPlainText()
        STOP=self.STOP
        TD=self.TD
        self.stop=False

        if(TD.isChecked() ):
            if (n.isalnum() and not n.isalpha()):
                if(self.textBrowser_2.toPlainText()):

                    n=int(n)
                    self.ShowProgressbar()
                    self.Estop.show()
                    self.pushButton.hide()

                    for i in self.ch:
                        if (i.isChecked() and not self.same.isChecked()):
                            self.Save_Waveform( self.ch[i], n)
                    

                else: #Checks if file path is provided
                    self.WriteToStatusBar("You Forgot to Choose File Path!!!",5000)
            else: # Checks if Number of waveForms Provided
                self.WriteToStatusBar( "--> Please Provide Number of WaveForms to Store !" ,5000)
        else: # when Save on Stop choosed
            self.ShowProgressbar()
            n= 1
            for i in self.ch:
                if(i.isChecked() and not self.same.isChecked()):
                    self.Save_Waveform(self.ch[i],n)




    def CaptureControl(self):
        if(self.TD.isChecked()):
            self.textEdit.setDisabled(False)
            self.HideProgressbar()

        elif(self.STOP.isChecked()):
            self.textEdit.setDisabled(True)


        if (self.progressBar.value() == 0 or self.progressBar.value() == 100):
            self.HideProgressbar()

    #Initially
    def AtStart(self):
        # Initially Disable Some Buttons
        self.POSitive.setDisabled( True )
        self.NEGative.setDisabled( True )
        self.AC.setDisabled( True )
        self.DC.setDisabled( True )
        self.doubleSpinBox.setDisabled( True )
        self.same.setDisabled( True )
        self.Estop.hide()

        #Create checkButtons
        self.CB_Sources=QButtonGroup()
        self.CB_Sources.setExclusive(True)
        self.CB_Sources.addButton(self.CHANnel1)
        self.CB_Sources.addButton(self.CHANnel2)
        self.CB_Sources.addButton(self.CHANnel3)
        self.CB_Sources.addButton(self.CHANnel4)
        self.CB_Sources.setExclusive( False )

        #Create RadioButton Groups
        self.RB_Couple=QButtonGroup()
        self.RB_Couple.addButton( self.AC )
        self.RB_Couple.addButton( self.DC )

        self.RB_Slope = QButtonGroup()
        self.RB_Slope.addButton( self.NEGative )
        self.RB_Slope.addButton( self.POSitive )

        self.RB_Capture=QButtonGroup()
        self.RB_Capture.addButton(self.STOP)
        self.RB_Capture.addButton(self.TD)

        self.RB_Mode=QButtonGroup()
        self.RB_Mode.addButton(self.NORMal)
        self.RB_Mode.addButton(self.MAXimum)
        self.RB_Mode.addButton(self.RAW)

        self.ch = {self.CHANnel1:self.CHANnel1.objectName(),
              self.CHANnel2: self.CHANnel2.objectName(),
              self.CHANnel3: self.CHANnel3.objectName(),
              self.CHANnel4: self.CHANnel4.objectName(),
              self.MATH: self.MATH.objectName()}

        # Functions

        self.CaptureControl()
        # Check initial Buttons
        self.TD.setChecked( True )
        self.NORMal.setChecked( True )

        # Connections
        #self.All.clicked.connect( self.Check )
        self.trigger.clicked.connect( self.TrigControl )
        self.pushButton_3.clicked.connect( self.FileBrowser )

        self.RB_Capture.checkedButton().toggled.connect(self.CaptureControl)
        self.RB_Mode.checkedButton().toggled.connect(self.CaptureControl)

        # Connect the checkbox
        for i in self.ch:
            if(self.ch[i]!=self.MATH.objectName()):
                i.toggled.connect( self.TurnOnChannels )

        self.Estop.pressed.connect(self.Stopnow)

        # Toolbar button actions
        self.actionExit.triggered.connect( self.Exit )
        self.actionConnection.triggered.connect( self.Connect )
        self.action_WaveForm_Viewer.triggered.connect( self.WaveFormViewer )

        # Start Saving when button is clicked
        self.pushButton.clicked.connect( self.StartCaptureWaveforms )
        self.RB_Mode.checkedButton().toggled.connect(self.MathButtonControl)

        # Hide the ProgressBar
        self.progressBar.hide()
        self.label_4.hide()

        # Initially set progressbar 0%
        self.progressBar.setMinimum(0)


        # Show Some Messages
        self.Write( " ---> Output Screen" )
        self.statusbar.showMessage( " Welcome To Waveform Catcher", 10000 )

        # Color of Status Bar
        self.statusbar.setStyleSheet( "color:red;font-weight:bold" )
        self.WriteToStatusBar( "Hello, Welcome To Rigol Scope WaveForm Saver !", 10000 )

        #self.isConnection()

    #Checks for "All" is checked or not
    def Check(self):
        if (self.All.isChecked()):
            self.CHANnel1.setChecked( True )
            self.CHANnel2.setChecked( True )
            self.CHANnel3.setChecked( True )
            self.CHANnel4.setChecked( True )

            self.same.setDisabled(False)

        elif (not self.All.isChecked()):
            self.CHANnel1.setChecked( True )
            self.CHANnel2.setChecked( False )
            self.CHANnel3.setChecked( False )
            self.CHANnel4.setChecked( False )
            self.same.setDisabled( True )
            self.same.setChecked( False )


    def MathButtonControl(self):

        if(self.RB_Mode.checkedButton().text().lower()=="normal"):
            self.MATH.setDisabled(False)

        else:
            self.MATH.setChecked(False)
            self.MATH.setDisabled(True)


            #Connection Check
    def isConnection(self):
        ip=self.getIp()


        try:
            self.scope=conn(ip)
            Name=self.scope.idn.split(",")
            Name=Name[1]
            if(Name):
                self.statusbar.showMessage("Success! " + Name + " is Connected", 10000)


        except OSError as e:
            Warn=QMessageBox.warning(self,"Connection Problem! " + str(e), "  Please Check the Cable and Scope to see if it is frozen. Do You want to try again?",QMessageBox.Yes |QMessageBox.No)
            if(Warn==QMessageBox.Yes):
                self.isConnection()
            else:
                Ques=self.QuestionMessage("Before you go!","Would you like to change your ip adress?")
                if(Ques):
                    self.Connect()




    def FileExistResponse(self, path):
        File=QFileInfo(path)
        if(File.exists() and File.isFile()):
            return self.QuestionMessage("This File is Exists!","Would you like to OverWrite?")
        else:
            return True
    def QuestionMessage(self,title,question):
        Message = QMessageBox()
        response = Message.question( self,title,question, Message.Yes | Message.No )
        if (response == Message.Yes):
            return True
        elif(response==Message.No):
            return False

    def FileExist(self,path):
        File=QFileInfo(path)
        if(File.exists() and File.isFile()):
            return True
        else:
            return False



    def Querries(self,chr,str):

        if (chr == "source"):
            response = self.scope.query( ":TRIGger:EDGe:SOURce?")
        elif (chr == "coupling"):
            response = self.scope.query( ":TRIGger:COUPling?" )
        elif (chr == "slope"):
            response = self.scope.query( ":TRIGger:EDGe:SLOPe?" )
        elif (chr == "triglevel"):
            response = self.scope.query( ":TRIGger:EDGe:LEVel?" )
        elif (chr == "trigstatus"):
            response = self.scope.query( ":TRIGger:STATus?" )
        elif (chr == "isChON"):
            response = self.scope.query( ":CHANnel" + str + ":DISPlay?" )

        return response

    def Apply(self,chr,str):

        if(chr=="source"):
            response=self.scope.write( ":TRIGger:EDGe:SOURce " + str )
        elif(chr=="coupling"):
            response=self.scope.write( ":TRIGger:COUPling " + str)
        elif (chr == "slope"):
            response = self.scope.write(":TRIGger:EDGe:SLOPe " + str )
        elif (chr == "triglevel"):
            response = self.scope.write( ":TRIGger:EDGe:LEVel " + str )
        elif (chr == "trigmode"):
            response = self.scope.write( ":TRIGger:MODE " + str )
        elif (chr == "ChON"):
            response = self.scope.write( ":CHANnel" + str + ":DISPlay ON")
        elif (chr == "ChOFF"):
            response = self.scope.write( ":CHANnel" + str + ":DISPlay OFF" )
        return response

    # Activates Trigger
    def TrigControl(self):
        if (self.trigger.isChecked()):
            self.POSitive.setChecked( True )
            self.AC.setChecked( True )

            # Enable Functions
            self.POSitive.setDisabled( False )
            self.NEGative.setDisabled( False )
            self.AC.setDisabled( False )
            self.DC.setDisabled( False )
            self.doubleSpinBox.setDisabled( False )
        else:
            #Uncheck the buttons
            self.RB_Couple.setExclusive(False)
            self.RB_Couple.checkedButton().setChecked(False)
            self.RB_Couple.setExclusive( True )

            self.RB_Slope.setExclusive( False )
            self.RB_Slope.checkedButton().setChecked( False )
            self.RB_Slope.setExclusive( True )

            # Disable Functions
            self.POSitive.setDisabled( True )
            self.NEGative.setDisabled( True )
            self.AC.setDisabled( True )
            self.DC.setDisabled( True )
            self.doubleSpinBox.setDisabled( True )

    #file Browser
    def FileBrowser(self):
        FileName=QFileDialog()
        FilePath=FileName.getExistingDirectory(self,"Choose Folder","/home",QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.textBrowser_2.setText(str(FilePath))

    def csv_open(self,FilePath):
        return open( FilePath, "w" )

    def TriggerSourceSelect(self,Ch):
        Name = str( self.Querries("source","") )
        Name = Name[-1:]
        Name = "CHANnel" + Name

        if (Ch != Name and Ch != "MATH"):
            self.Apply("source",Ch)
            self.Write( "Trigger source  now is  " + Ch )

    def Stopnow(self):
        self.pushButton.show()
        self.Estop.hide()
        self.Write("You have stopped the process!")
        self.stop=True


    def TriggerControlSet(self,Ch):
        slope = self.RB_Slope.checkedButton().objectName()
        couple = self.RB_Couple.checkedButton().objectName()
        trig = str( float( self.doubleSpinBox.value() ) / 1000 )  # converting it to Volts

        if (self.Querries("source","") != Ch):
            self.Apply( "source", Ch )
            self.Write( self.Querries("source","") + " is choosen" )

        else:
            self.Write( self.Querries("source","") + " is choosen" )
        # AC, DC

        if (self.Querries("coupling","") != couple):
            self.Apply( "coupling", couple )
            self.Write( self.Querries("coupling","") + " is choosen" )
        else:
            self.Write( self.Querries("coupling","") + " is choosen" )

        # POSitive: rising edge,NEGative: falling edge, RFALl: rising/falling edge
        if (self.Querries("slope","") != Ch):
            self.Apply( "slope", Ch )
            self.Write( self.Querries("slope","") + " is choosen" )
        else:
            self.Write( self.Querries("slope","") + " is choosen" )

        #  0.16 == 160mv/div
        if (self.Querries("triglevel","") != trig):
            self.Apply( "triglevel", trig )
            self.Write( self.Querries("triglevel","") + " is choosen" )
        else:
            self.Write( self.Querries("triglevel","") + " is choosen" )

    def TurnOnChannels(self):
        count = 1
        for i in (self.ch):
            if (not self.ch[i] == self.MATH.objectName()):
                if (i.isChecked()):
                    response = self.Querries( "isChON", str(count) )

                    if (response == "0"):
                        self.Apply( "ChON", str( count ) )
                        self.Write( str( i.text() ) + " is ON" )
                elif (not i.isChecked()):
                    response = self.Querries( "isChON", str(count) )

                    if (response == "1"):
                        self.Apply( "ChOFF", str(count) )
                        self.Write( str( i.text() ) + " is OFF" )
                count += 1
        if (count == 4):
            self.textBrowser.clear()

    #WaveForm Capturer
    def Save_Waveform(self,Ch,n):

        count = 1;
        done=True
        FirstResponse = 0
        self.progressBar.setMinimum(-1)
        self.progressBar.setMaximum(n-1)



        mode=self.RB_Mode.checkedButton().objectName()
        FileDir = self.textBrowser_2.toPlainText()
        FileName = "_" + Ch.lower() + "_" + str( count ) + ".csv"
        FilePath = str( FileDir ) + "/" + str( FileName )

        #Trigger control button is checked
        if(self.trigger.isChecked()):
            self.TriggerControlSet(Ch)

        #self.TriggerSourceSelect(Ch)


        if(FirstResponse==0):
            response = self.FileExistResponse( FilePath )
            if(response):
                pass
            else:
                count += 1

                if (self.STOP.isChecked()):
                    n += 1
                while (count<=n):
                    FileName = "_" + Ch.lower() + "_" + str( count ) + ".csv"
                    FilePath = str( FileDir ) + "/" + str( FileName )

                    if(self.FileExist(FilePath)):
                        count+=1
                        if (self.STOP.isChecked()):
                            n += 1
                    else:
                        break


        while (count <= n):
           
            

            while (self.Querries("trigstatus","")== str(self.RB_Capture.checkedButton().objectName()) and count <= n):  # returns  TD, WAIT, RUN, AUTO, or STOP
                data = []
                FileName="_" + Ch.lower() + "_" + str(count ) + ".csv"
                FilePath =  str(FileDir) + "/" +  str(FileName)
                if(Ch=="MATH"):
                    data.append(self.scope._get_waveform_bytes_screen(Ch,"NORMal"))
                else:
                    data.append( self.scope.get_waveform_samples( Ch, mode ) )
                data.insert( 0, self.scope.waveform_time_values_decimal )

                with self.csv_open( FilePath ) as csv_file:
                    delimiter = ','
                    csv_writer = csv.writer( csv_file )
                    csv_writer.writerow( ["TIME", "Voltage"] )

                    for vals in zip_longest( *data ):
                        vals = [vals[0]] + ['{:.2e}'.format( val ) for val in vals[1:]]
                        csv_writer.writerow( vals )
                
                if(self.stop):
                  count=n-1
                  done=False
                
                if (done):
                  tx = "------> " + str( count ) + " files are saved for " + Ch.lower()
                else:
                  tx="Stopped!"
                 
                self.statusbar.showMessage(tx,10000)

                self.progressBar.setValue(count)
                


                qApp.processEvents();
                count += 1

        self.WriteSame( "DONE!! \n" )
       
