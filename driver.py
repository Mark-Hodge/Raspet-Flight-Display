from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot
from limitsdialog import Ui_Dialog as Form, Ui_Dialog
from dataTransformer import *
from pccFileHandler import *
from dataHandler import DataHandler
from dataValidator import *
from mainInterface import *

# Initialize a new DataHandler() class instance for storing/updating
# important information used to maintain successful execution.
DataHandler = DataHandler()

def openPCCTelemetryFile(self):
    # Attempt to open user provided .tel file
    try:
        pccTelemetryFile = openFile(self, DataHandler)

    # Catch any I/O or File Not Found errors
    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)

def Driver_openOutputLogFile(self):
    # Attempt to open or create the user specified file for RFD to log output
    try:
        FileHandler_OpenOutputLogFile(self, DataHandler)

    # Catch any I/O or File Not Found errors
    except Exception as ex:
        print("Could not open output log file (check file type and try again).", ex)

def flagIsSet(self):
    # Set flag to 1 (true) to mark as important in the output log
    DataHandler.flagState = True

def flagIsNotSet(self):
    # Set flag to 0 (false) to mark as not important in the output log
    DataHandler.flagState = False

# Attempt to start tracking data from PCC and processing data to provide output
def startTracking(self):
    # Attempt to get time RFD starts tracking and begin counting elapsed time
    try:
        if (DataHandler.lockStartTime == False):
            DataHandler.timeStartClicked = datetime.datetime.now()  # Get datetime for displaying start time to screen
            DataHandler.startTime = time.time()                     # Get time for counting elapsed time
            self.label_infoBar_startTime.setText(DataHandler.timeStartClicked.strftime("Start Time: %H:%M:%S"))

            DataHandler.lockStartTime = True

    except Exception as ex:
        print("Could not request time() and/or datetime(): ", ex)

    # Initiate telemetry tracking and call methods which process incoming data
    try:
        self.label_infoBar_status.setText("Status: Tracking")

        retrievePCCLog(DataHandler)         # Method in pccFileHandler.py which reads data in and validates segments
        PopulateDictionary(DataHandler)     # Method in dataTransformer.py which checks segment integrity and stores segment in a key/value dictionary for later use
        UpdateHUD(self, DataHandler)        # Method in dataValidator.py which updates the GUI with recently read-in values
        writeToLogFile(DataHandler)         # Method in pccfileHandler.py which writes data, and alarm states to log

        # Get elapsed time and PCC time
        DataHandler.elapsedTime = (time.time() - DataHandler.startTime)
        PCCTime = DataHandler.getRawTelemetryData()
        PCCTime = PCCTime["<Clock>[ms]"]

        # Update GUI labels to elapsed time and PCC time
        self.label_infoBar_elapsedTime.setText(time.strftime("Elapsed Time: %H:%M:%S", time.gmtime(DataHandler.elapsedTime)))
        self.label_infoBar_PCCTime.setText("PCC Time: " + str(PCCTime))

        return 1

    except Exception as ex:
        print("Error occurred while initializing tracking ", ex)
        return 1

# Stop tracking data from PCC when user pauses application
def stopTracking(self):
    self.trackCondition = 0
    self.label_infoBar_status.setText("Status: Stopped")
