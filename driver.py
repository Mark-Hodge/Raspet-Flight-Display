

from pccFileHandler import *
from mainInterface import *
from limitsdialog import Ui_Dialog as Form


class Driver:

    def __init__(self):
        self.fh = ""
        self.stopStatus = 0
        self.RawPCCData = {}
        self.UsablePCCData = {}
        self.pccFileHandler = ""

def openPCCTelemetryFile(self):
    try:
        pccTelemetryFile = OpenFile(self)

    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)


def openLimitsDialog(self):
    Dialog = QtWidgets.QDialog()
    ui = Form()
    ui.setupUi(Dialog)
    Dialog.exec()
    # sys.exit(app.exec_())

def startTracking(self):

    pushButton_toolBar_start = self.pushButton_toolBar_start
    #
    # Under Construction #
    #

def stopTracking(self, stopValue = 0):

    print(str(stopValue))
    pushButton_toolBar_stop = self.pushButton_toolBar_stop.isChecked()
    print("pushButton_toolBar_stop --> ", str(pushButton_toolBar_stop))

# if __name__ == "__main__":
#     PCCFileHandler = PCCFileHandler()
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())