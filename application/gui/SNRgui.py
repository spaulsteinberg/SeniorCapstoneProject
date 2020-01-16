#PyQt5 modules
from PyQt5 import uic
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class SNR(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SNR, self).__init__(*args, **kwargs)

        uic.loadUi("./gui/Visuals/SNR.ui", self) # Load the .ui file
        self.setWindowTitle('Search-N-Rescue Jetson Nano Project')   
        self.setMaximumSize(1150,1000) 

        self.initUI()

    def initUI(self):

        self.queryLayout = self.findChild(QGridLayout, 'queryLayout')
        self.imageLayout = self.findChild(QGridLayout, 'imageLayout')
        self.videoLayout = self.findChild(QGridLayout, 'videoLayout')

        placeholder1 = QLabel("List of available images will go here.")
        placeholder2 = QLabel("View of selected image to search\nfor will be displayed here.")
        placeholder3 = QLabel("Live video footage will be displayed here.")

        self.queryLayout.addWidget(placeholder1)
        self.imageLayout.addWidget(placeholder2)
        self.videoLayout.addWidget(placeholder3)


        self.show()

    def mainWindowExitHandler(self):
        self.close()



if __name__=="__main__":
    print("Main application file.")