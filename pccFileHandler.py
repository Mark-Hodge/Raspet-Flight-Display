
# import os   # TODO: remove later if not needed
from dataTransformer import PopulateDictionary
from PyQt5.QtWidgets import QFileDialog
# from dataHandler import DataHandler   # TODO: remove later if not needed


# ====================================================================================================================== Open File()
def openFile(self, dataHandlerInstance):

    # Call file navigator on mouse click and display path on screen
    try:
        PCCTelemetryFile = QFileDialog.getOpenFileName()

    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)

    # Open file and move cursor to EOF
    try:
        fh = open(PCCTelemetryFile[0], 'r')
        # fh.seek(0, os.SEEK_END)   TODO: Uncomment for production version. Ignored for testing purposes while not working with live telemetry
        print("File Successfully Opened and cursor moved to EOF")       # TODO: DEBUGGING PURPOSES ONLY (delete print statement later)
        self.label_toolBar_PCCFile.setText("PCC Telemetry File: " + str(PCCTelemetryFile[0]))

        # Store file path in DataHandler encase restart or failure, file path can be retrieved and re-opened.
        dataHandlerInstance.setTelemetryFile(fh)
        dataHandlerInstance.resetRawTelemetryData()


    # Hand errors in opening or navigating to EOF
    except Exception as ex:
        print("Could not open file: ERROR --> ", ex)


# ====================================================================================================================== Retrive PCC Log()
def retrievePCCLog(self, dataHandlerInstance):
    fh = dataHandlerInstance.getTelemetryFile()        # Initialize local file header encase corrupted (allows restart with correct file header)

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
        PopulateDictionary(self, dataHandlerInstance, dataSegment, )