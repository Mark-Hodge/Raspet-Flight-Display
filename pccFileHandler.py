
import os   # TODO: remove later if not needed
from dataTransformer import PopulateDictionary
from PyQt5.QtWidgets import QFileDialog
# from dataHandler import DataHandler   # TODO: remove later if not needed

# ====================================================================================================================== Open Output Log File()
def FileHandler_OpenOutputLogFile(self, dataHandlerInstance):

    # Call file navigator on mouse click and attempt to open/create file.
    try:
        outputLogFile = QFileDialog.getOpenFileName()

    except Exception as ex:
        print("Could not open output log file (check file type and try again).", ex)

    # Open or create file and move cursor to EOF.
    try:
        fh = open(outputLogFile[0], 'a', newline='')
        fh.seek(0, os.SEEK_END)

        # Set GUI label to file path
        self.label_infoBar_output.setText("Output Log: " + str(outputLogFile[0]))

        # Store file descriptor in DataHandler
        dataHandlerInstance.setOutputLogFile(fh)
        dataHandlerInstance.setWriter()

    except Exception as ex:
        print("Could not open/create file and/or move cursor to EOF: ERROR --> ", ex)

# ====================================================================================================================== Open PCC Telemetry File()
def openFile(self, dataHandlerInstance):

    # Call file navigator on mouse click and display path on screen
    try:
        PCCTelemetryFile = QFileDialog.getOpenFileName()

    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)

    # Open file and move cursor to EOF
    try:
        fh = open(PCCTelemetryFile[0], 'r')
        fh.seek(0, os.SEEK_END)   # TODO: Uncomment for production version. Ignored for testing purposes while not working with live telemetry

        # Set GUI label to file path
        self.label_toolBar_PCCFile.setText("PCC Telemetry File: " + str(PCCTelemetryFile[0]))

        # Store file descriptor in DataHandler
        dataHandlerInstance.setTelemetryFile(fh)
        dataHandlerInstance.resetRawTelemetryData()

        print("File Successfully Opened and cursor moved to EOF")  # TODO: DEBUGGING PURPOSES ONLY (delete print statement later)

    # Hand errors in opening or navigating to EOF
    except Exception as ex:
        print("Could not open/create file and/or move cursor to EOF: ERROR --> ", ex)

# ====================================================================================================================== Write To Log()
def writeToLogFile(dataHandlerInstance):

    if (dataHandlerInstance.getFlagState()):
        dataHandlerInstance.writer.writerow({"Flag": "1", "Clock[ms]": dataHandlerInstance.finalDataToLog["Clock[ms]"], "Elevator Deflection[deg]": dataHandlerInstance.finalDataToLog["Elevator Deflection[deg]"],
                                             "Pitch Rate[deg/s]": dataHandlerInstance.finalDataToLog["Pitch Rate[deg/s]"], "Aileron Deflection[deg]": dataHandlerInstance.finalDataToLog["Aileron Deflection[deg]"],
                                             "Roll Rate[deg/s]": dataHandlerInstance.finalDataToLog["Roll Rate[deg/s]"], "Rudder Deflection[deg]": dataHandlerInstance.finalDataToLog["Rudder Deflection[deg]"],
                                             "Yaw Rate[deg/s]": dataHandlerInstance.finalDataToLog["Yaw Rate[deg/s]"], "Pitch Rate Warning Condition[deg]": dataHandlerInstance.finalDataToLog["Pitch Rate Warning Condition[deg]"],
                                             "Pitch Rate Alert Condition[deg]": dataHandlerInstance.finalDataToLog["Pitch Rate Alert Condition[deg]"], "Roll Rate Warning Condition[deg]": dataHandlerInstance.finalDataToLog["Roll Rate Warning Condition[deg]"],
                                             "Roll Rate Alert Condition[deg]": dataHandlerInstance.finalDataToLog["Roll Rate Alert Condition[deg]"], "Yaw Rate Warning Condition[deg]": dataHandlerInstance.finalDataToLog["Yaw Rate Warning Condition[deg]"],
                                             "Yaw Rate Alert Condition[deg]": dataHandlerInstance.finalDataToLog["Yaw Rate Alert Condition[deg]"], "Pitch Deflection State": dataHandlerInstance.finalDataToLog["Pitch Deflection State"],
                                             "Roll Deflection State": dataHandlerInstance.finalDataToLog["Roll Deflection State"], "Yaw Deflection State": dataHandlerInstance.finalDataToLog["Yaw Deflection State"]})

    else:
        dataHandlerInstance.writer.writerow({"Flag": "0", "Clock[ms]": dataHandlerInstance.finalDataToLog["Clock[ms]"], "Elevator Deflection[deg]": dataHandlerInstance.finalDataToLog["Elevator Deflection[deg]"],
                                             "Pitch Rate[deg/s]": dataHandlerInstance.finalDataToLog["Pitch Rate[deg/s]"], "Aileron Deflection[deg]": dataHandlerInstance.finalDataToLog["Aileron Deflection[deg]"],
                                             "Roll Rate[deg/s]": dataHandlerInstance.finalDataToLog["Roll Rate[deg/s]"], "Rudder Deflection[deg]": dataHandlerInstance.finalDataToLog["Rudder Deflection[deg]"],
                                             "Yaw Rate[deg/s]": dataHandlerInstance.finalDataToLog["Yaw Rate[deg/s]"], "Pitch Rate Warning Condition[deg]": dataHandlerInstance.finalDataToLog["Pitch Rate Warning Condition[deg]"],
                                             "Pitch Rate Alert Condition[deg]": dataHandlerInstance.finalDataToLog["Pitch Rate Alert Condition[deg]"], "Roll Rate Warning Condition[deg]": dataHandlerInstance.finalDataToLog["Roll Rate Warning Condition[deg]"],
                                             "Roll Rate Alert Condition[deg]": dataHandlerInstance.finalDataToLog["Roll Rate Alert Condition[deg]"], "Yaw Rate Warning Condition[deg]": dataHandlerInstance.finalDataToLog["Yaw Rate Warning Condition[deg]"],
                                             "Yaw Rate Alert Condition[deg]": dataHandlerInstance.finalDataToLog["Yaw Rate Alert Condition[deg]"], "Pitch Deflection State": dataHandlerInstance.finalDataToLog["Pitch Deflection State"],
                                             "Roll Deflection State": dataHandlerInstance.finalDataToLog["Roll Deflection State"], "Yaw Deflection State": dataHandlerInstance.finalDataToLog["Yaw Deflection State"]})

# ====================================================================================================================== Retrive PCC Log()
def retrievePCCLog(dataHandler):
    fh = dataHandler.getTelemetryFile()        # Initialize local file header encase corrupted (allows restart with correct file header)

    # Iterate while incoming data
    while 1:

        # Initialize empty arrays to store values until pushed to dictionary
        tempArr = []
        dataSegment = []
        overFlow = []

        line = fh.readline()

        # If current line is not empty string, split and store in temporary array
        if not len(line.strip()) == 0:
            tempArr = line.split()

            # If temporary array contains less than a full data set, set complete
            # segment to false (PCC records 200 fields per 1 full set. Operating on incomplete
            # set will cause data corruptions and mis-calculations later on).
            if len(tempArr) < 200:
                completeSegment = 0

                while not completeSegment:

                    line = fh.readline()        # Read in a new line to complete the segment

                    # If new line is not empty string, split and move to condition
                    if not len(line.strip()) == 0:
                        line = line.split()

                        # Append each element in new line to temporary array
                        for each in line:
                            tempArr.append(each)

                        # If temporary array contains more than one complete set, set complete segment to true
                        # and splice the complete portion into dataSegment array. Move overflowed elements to overFlow array.
                        if len(tempArr) >= 200:
                            completeSegment = 1
                            dataSegment = tempArr[0:200]
                            overFlow = tempArr[201:]

            # If temporary array contains a full data set after first line read, splice one full set into dataSegment array
            # and move overflowed elements to overFlow array
            if len(tempArr) >= 200:
                dataSegment = tempArr[0:200]
                overFlow = tempArr[201:]

        else:
            continue

        # Pass complete data segment for use in populating dictionary
        dataHandler.setDataSegment(dataSegment)
        return 1
