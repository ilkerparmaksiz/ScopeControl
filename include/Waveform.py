from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from include.chart import  *

class waveformViewer(QMainWindow,Ui_WaveFormView):
    def __init__(self,parent=None):
        super(waveformViewer,self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupW( self )
        self.AtFirst()


    def AtFirst(self):
        self.count=0;
        self.setWindowTitle("WaveForm Viewer")
        self.browserB.clicked.connect( self.CollectFilePath )
        self.action_Open.triggered.connect( self.CollectFilePath )
        self.action_Exit.triggered.connect( self.hide )
        self.comboBox.currentIndexChanged.connect(self.FileReader)
        self.statusbar.showMessage("Welcome To WaveFormViewer Please Choose Directory",10000)

    def Plot(self,Series,title):
        self.chart = QChart()
        self.chart.addSeries( Series )
        self.chart.setTitle( title )
        self.chart.createDefaultAxes()
        axisX = QValueAxis()
        axisX.setTitleText("Time (s)")
        axisX.setLabelFormat( "%s" );
        #axisX.setTickCount( Series.count())
        self.chart.addAxis( axisX, Qt.AlignBottom)
        Series.attachAxis(axisX)

        axisY = QValueAxis()
        axisY.setTitleText( "Voltage (V)" )
        axisY.setLabelFormat( "%s" );
        #axisY.setTickCount( Series.count() )
        self.chart.addAxis( axisY, Qt.AlignLeft )
        Series.attachAxis( axisY )


        self.chartview.setChart(self.chart)
        self.chartview.setRenderHint( QPainter.Antialiasing )

    def FileReaderandBrowser(self):
        FileDialog=QFileDialog()
        #FilePath=FileDialog.getOpenFileName(self,"Choose file","home/ilker/scope")
        FilePath=FileDialog.getOpenFileName(self,"Open","/home/ilker/scope",("Documents (*.csv *.txt)"))
        Series = QLineSeries()
        File=QFile(FilePath[0])
        if( not File.open(QIODevice.ReadOnly)):
            QMessageBox.information(0,"error",File.errorString())

        In=QTextStream(File)
        count=0
        while (not In.atEnd()):
            line=In.readLine()
            Values=line.split(",")
            if(count==0):
                pass
            else:
                Series.append(float(Values[0]),float(Values[1]))
            count=1
        self.Plot(Series)
        File.close()

    def FileReader(self):
        Series=QLineSeries()
        path=self.FilePath + "/" + self.comboBox.currentText()
        if(self.comboBox.currentText()==""):
            pass
        elif(self.FilePath==""):
            self.CollectFilePath()
        else:
            title=self.comboBox.currentText()
            File=QFile(path)
            if(not File.open(QIODevice.ReadOnly)):
                QMessageBox.information(self,"error",File.errorString())
            In=QTextStream(File)
            count=0
            while(not In.atEnd()):
                line=In.readLine()
                Values=line.split(",")
                if(count==0):
                    pass
                else:
                    Series.append(float(Values[0]),float(Values[1]))
                count=1
            self.Plot(Series,title)
            self.statusbar.showMessage("Now Plotting --> " + path,10000)

            File.close()
    def QuestionMessage(self,title,message):
        Message = QMessageBox()
        response = Message.question( self, title, message, Message.Yes | Message.No )
        if (response == Message.Yes):
                return True
        else:
            return False
    def CollectFilePath(self):
        FileDialog=QFileDialog()
        self.FilePath=FileDialog.getExistingDirectory(self,"FilePaths","/home",FileDialog.ShowDirsOnly | FileDialog.DontResolveSymlinks )
        QDirObject = QDir(self.FilePath)
        List=["*.csv","*.txt"]
        FileNames=QDirObject.entryList(List,QDir.Files)
        self.comboBox.clear()

        if(FileNames):
            self.comboBox.addItems(FileNames)
        else:
            self.count+=1
            if(self.count<3):
                self.CollectFilePath()
            else:
                pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = waveformViewer()
    window.setWindowModality(Qt.WindowModal)


    window.show()


    sys.exit(app.exec_())