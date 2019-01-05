
__author__="ilker Parmaksiz"

import sys,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from include.functions import Functions

class Scope(Functions):

    def __init__(self):
        super( Scope, self ).__init__()
        qApp.installEventFilter(self)

        #Initially What we need
        self.AtStart()



if __name__ == "__main__":

    App = QApplication( sys.argv )
    window = Scope()
    pixmap=QPixmap("images/splash2.jpg")
    splash = QSplashScreen( pixmap, Qt.WindowStaysOnTopHint )
    splash.setMask( pixmap.mask() )

    splashFont=QFont()
    splashFont.setFamily("Ubuntu" );
    splashFont.setBold( True );
    splashFont.setPointSize(16)
    splash.setFont(splashFont)



    # adding progress bar
    progressBar = QProgressBar( splash )
    progressBar.setAlignment(Qt.AlignCenter)
    progressBar.setGeometry(0,0,splash.width()/2,24)
    progressBar.setFormat("Please Wait Loading...")
    progressBar.move((splash.width()-progressBar.width())/2,(splash.height()-progressBar.height())/2)
    progressBar.setMinimum(0)
    progressBar.setMaximum(19)
    # adding message

    splash.showMessage( 'Welcome to Scope Control ', Qt.AlignHCenter | Qt.AlignTop, Qt.white )



    splash.show()

    for i in range( 0, 20 ):
        progressBar.setValue( i )
        # Simulate something that takes time
        App.processEvents()
        time.sleep( 0.15 )



    window.show()
    splash.finish( window )
    window.isConnection()
    sys.exit( App.exec_() )
