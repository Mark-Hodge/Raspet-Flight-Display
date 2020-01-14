
from limitsdialog import Ui_Dialog as Form, Ui_Dialog
from pccFileHandler import openFile
from mainInterface import *


def openLimitsDialog(self):
    import sys
    Dialog = QtWidgets.QDialog()
    ui = Form()
    ui.setupUi(Dialog)
    Dialog.exec()
    # sys.exit(app.exec_())

def openPCCTelemetryFile(self):
    try:
        pccTelemetryFile = openFile(self)

    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)

def startTracking(self):
    """
    Under Construction
    Further implementation needed later on
    """
    pushButton_toolBar_start = self.pushButton_toolBar_start


def stopTracking(self, stopValue = 0):

    print(str(stopValue))
    pushButton_toolBar_stop = self.pushButton_toolBar_stop.isChecked()
    print("pushButton_toolBar_stop --> ", str(pushButton_toolBar_stop))