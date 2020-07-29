#This is a Waveform Saver for Ds1054z

it uses following [the API package](https://ds1054z.readthedocs.org/en/stable/api/index.html) and PyQt5. Therefore, You need to install this packages before you can run this program.
there is also github repository for  [previous package](https://raw.githubusercontent.com/pklaus/ds1054z)

# Following devices may also work but have not tested

* DS1054Z
* DS1074Z
* DS1104Z
* DS1074Z-S
* DS1104Z-S
* MSO1074Z
* MSO1104Z
* MSO1074Z-S
* MSO1104Z-S

## Features
* Save Waveforms in Csv files on trigger 
* Display waveforms
## Enviroment Variables
   Open and change env.sh according to destination of the program and then type following
   sudo gedit ~/.bashrc 
   in the end of the this file
   source "PathoftheProgram"/env.sh
   source ~/.bashrc
   this way you can call the program anywhere by typing "ScopeControl" to terminal

## Installation for Ubuntu
install following packages 
	pip3 install ds1054z
	pip3 install pyqt5 
	pip3 install PyQtChart

Run following in the folder (python version 3.6 and up is strongly suggested)
	source start.sh  
	Note: you can adjust your python version to call in start.sh
	
## Installation for Rasberry Pi 
#Special thanks to @carlosperate for working this out. this issue addressed here :https://github.com/mu-editor/mu/issues/441

Install Following packages 
	pip3 install ds1054z
	sudo apt-get install python3-pyqt5 qtdeclarative5-dev qt5-default pyqt5-dev pyqt5-dev-tools pyqt5.qsci-dev qt5-qmake
# SIP 4.19:
 wget https://netcologne.dl.sourceforge.net/project/pyqt/sip/sip-4.19/sip-4.19.tar.gz
 tar zxvf sip-4.19.tar.gz
 cd sip-4.19
 python3 configure.py
 make -j 3
 sudo make install
 
# QtCharts:
Check the version for pyqt5 by this 
	apt-cache policy python3-pyqt5
You will get following:
	Installed: 5.14.1+dfsg-3build1
  	Candidate: 5.14.1+dfsg-3build1
Use the version above to clone git anywhere you want by changing -b "version" like below and follow the code	
	git clone git://code.qt.io/qt/qtcharts.git -b 5.14
 	cd qtcharts
	mkdir build
	cd build
 	qmake -r ..
 	make
 	sudo make install
# PyQtChart:
Download the program first by following:
	wget https://files.pythonhosted.org/packages/1c/a7/b075cd95d5481306e27643f80372d72f540e65812ed432a8e44f836a21c4/PyQtChart-5.15.0.tar.gz
Extract it to a folder:
	tar zxvf PyQtChart-5.15.0.tar.gz
	cd PyQtChart-5.15.0
Configure it and make sure versions match above
	python3.7 configure.py --qtchart-version=5.14 --verbose
	make
	sudo make install
# Run
type bellow anywhere in the terminal 
	ScopeControl 
## ScopeControl
<img src=“https://github.com/ilkerparmaksiz/ScopeControl/tree/master/images/Scope.png” raw="true" alt="ScopeControl" align="center"/>
	
