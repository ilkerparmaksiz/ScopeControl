#This is a Waveform Saver for Ds1054z

it uses following [the API package](https://ds1054z.readthedocs.org/en/stable/api/index.html) and PyQt5. Therefore, You need to install this packages before you can run this program.
there is also github repository for  [previous package](https://raw.githubusercontent.com/pklaus/ds1054z)

#Following devices may also work but have not tested

* DS1054Z
* DS1074Z
* DS1104Z
* DS1074Z-S
* DS1104Z-S
* MSO1074Z
* MSO1104Z
* MSO1074Z-S
* MSO1104Z-S

#Features
*Save Waveforms in Csv files on trigger 
*Display waveforms

#Installation
install following packages 
	pip3 install ds1054z
	pip3 install pyqt5 
	pip3 install PyQtChart

Run following in the folder
	python start.py
