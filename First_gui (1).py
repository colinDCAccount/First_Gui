'''
First PyQt5 (PySide5) app

Created by Phil J Sept 25

Note - no apparent distro for PySide 6 via pip - so cant install to use with Thonny, yet.

This will also run with Win11, assuming the PyQt5 lib files are installed with Thonny

resource - raspberrytips.com/pyqt-on-raspberry-pi

*****
      To begin run this script as is - after running the code, add comments to these
      uncommented lines (not the from or import), describing what happens
      
      Upload the completed code with comments to your github, provide the url in the DC Connect assignment box
*****
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys



app = QApplication([])
win = QMainWindow()

#Now Uncomment this 2nd section and test - state what each line does with comments
win.setWindowTitle("A windows thing") ##adds a title to the top header
win.resize(500, 500) ## resizes the box
win.move(400,200) ##says where to place the window


#Now uncomment this 3rd section and test - state what each line does with comments in these lines
label = QLabel("Some text", win) ###adds a line to add some text
label.move(50, 100) ### moves the prompt of where to add text

#Now uncomment the 4th section and test - state what each line does with comments in these lines
def clickMethod():
    print("Button clicked") #prints (button clicked) after clicking mouse in the shell
# 
button = QPushButton("Click here", win) #### adds a click here box in top left of the window
button.move(20,40) #### moves the click here box lower
button.clicked.connect(clickMethod) ####


win.show()

sys.exit(app.exec_())

