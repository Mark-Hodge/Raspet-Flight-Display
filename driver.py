from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot
from limitsdialog import Ui_Dialog as Form, Ui_Dialog
from dataTransformer import *
from pccFileHandler import *
from dataHandler import DataHandler
from dataValidator import *
from mainInterface import *

DataHandler = DataHandler()

def openPCCTelemetryFile(self):
    try:
        pccTelemetryFile = openFile(self, DataHandler)

    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)

def Driver_openOutputLogFile(self):
    try:
        FileHandler_OpenOutputLogFile(self, DataHandler)

    except Exception as ex:
        print("Could not open output log file (check file type and try again).", ex)

def flagIsSet(self):
    DataHandler.flagState = True

def flagIsNotSet(self):
    DataHandler.flagState = False

def startTracking(self):
    """
    Under Construction
    Further implementation needed later on
    """
    try:
        if (DataHandler.lockStartTime == False):
            DataHandler.timeStartClicked = datetime.datetime.now()
            DataHandler.startTime = time.time()
            self.label_infoBar_startTime.setText(DataHandler.timeStartClicked.strftime("Start Time: %H:%M:%S"))

            DataHandler.lockStartTime = True

    except Exception as ex:
        print("REVISE THIS ERROR MESSAGE: ", ex)

    # Initiate telemetry tracking and call methods
    try:
        self.label_infoBar_status.setText("Status: Tracking")

        retrievePCCLog(DataHandler)
        PopulateDictionary(DataHandler)
        UpdateHUD(self, DataHandler)
        writeToLogFile(DataHandler)

        # Get elapsed time and PCC time
        DataHandler.elapsedTime = (time.time() - DataHandler.startTime)
        PCCTime = DataHandler.getRawTelemetryData()
        PCCTime = PCCTime["<Clock>[ms]"]

        # Update GUI labels to elapsed time and PCC time
        self.label_infoBar_elapsedTime.setText(time.strftime("Elapsed Time: %H:%M:%S", time.gmtime(DataHandler.elapsedTime)))
        self.label_infoBar_PCCTime.setText("PCC Time: " + str(PCCTime))

        return 1

    except Exception as ex:
        print("Caught exception here, ", ex)
        return 1

def stopTracking(self):
    self.trackCondition = 0
    self.label_infoBar_status.setText("Status: Stopped")
