from dataTransformer import PopulateDictionary
from limitsdialog import Ui_Dialog as Form, Ui_Dialog
from pccFileHandler import retrievePCCLog, openFile
from dataHandler import DataHandler
from dataValidator import *
from mainInterface import *

DataHandler = DataHandler()

def openLimitsDialog(self):
    import sys
    Dialog = QtWidgets.QDialog()
    ui = Form()
    ui.setupUi(Dialog)
    Dialog.exec()
    # sys.exit(app.exec_())

def openPCCTelemetryFile(self):
    try:
        pccTelemetryFile = openFile(self, DataHandler)

    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)

def startTracking(self):
    """
    Under Construction
    Further implementation needed later on
    """
    # pushButton_toolBar_start = self.pushButton_toolBar_start
    """
    # TODO: re-write this section, this is for testing one iteration of the programs function calls.
    # Will need to implement continuous iteration, exception handling, and interface updating.
    # As well as validation for each new set of telemetry data and checking against limit conditions
    """
    test = retrievePCCLog(DataHandler)

    test2 = PopulateDictionary(DataHandler)

    test3 = UpdateHUD(self, DataHandler)



def stopTracking(self, stopValue = 0):

    print(str(stopValue))
    pushButton_toolBar_stop = self.pushButton_toolBar_stop.isChecked()
    print("pushButton_toolBar_stop --> ", str(pushButton_toolBar_stop))