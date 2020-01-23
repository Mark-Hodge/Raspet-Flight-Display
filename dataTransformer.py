# from dataHandler import DataHandler   #TODO: Remove if not needed
import copy
from dataValidator import *

def PopulateDictionary(self, dataHandlerInstance, dataSegment):
    position = 0        # Initialize for index tracking
    newTelemetryDictionary = copy.deepcopy(dataHandlerInstance.getRawTelemetryData())

    # Iterate through each key in dictionary
    for key in newTelemetryDictionary:

        # If position moved pass index length, break from loop
        if position >= len(dataSegment):
            break

        # If position is valid, copy corresponding dataSegment value to dictionary key and increment position
        else:
            newTelemetryDictionary[key] = dataSegment[position]
            position += 1

    # Pull values from populated dictionary for quality checking, Keys used are parameters needed for display
    # or special values which will be corrupted by minor character shifts in the dictionary
    try:        # TODO: Re-asses the values used for checking the integrity of the data... find better values
        integrity01 = newTelemetryDictionary['<AP_Global>']
        integrity02 = newTelemetryDictionary['<NavMode>']
        integrity03 = newTelemetryDictionary['<AlignSolnType>']
        integrity04 = newTelemetryDictionary['<Clock>[ms]']
        integrity05 = newTelemetryDictionary['<Surface3>']
        integrity06 = newTelemetryDictionary['<Surface6>']
        integrity07 = newTelemetryDictionary['<Surface0>']

        # If integrity values 1-3 are not alphabetical characters only, integrity check fails. If alphabetical
        # move to integrity values 4-6.
        check01 = integrity01.isalpha()
        # check02 = integrity02.isalpha()
        check02 = True
        check03 = integrity03.isalpha()

        if (not check01) or (not check02) or (not check03):
            raise ValueError("1, 2, 3 are not alpha")

        # if (integrity01.isalpha()) and (integrity02.isalpha()) and (integrity03.isalpha()):
        # If integrity values 4-6 are not numeric characters only, integrity check fails
        else:
            integrity04 = float(integrity04)
            integrity05 = float(integrity05)
            integrity06 = float(integrity06)
            integrity07 = float(integrity07)


    # Catch exception raised and print corrupted values and full set to console for analyzing. Dictionary is not passed to be used
    # in updating display. Values are ignored and program writes over dictionary with next loop.
    except Exception as ex2:
        print("Integrity Check Failed: truncating entry. --> ", newTelemetryDictionary['<Clock>[ms]'], newTelemetryDictionary['<AP_Global>'],
              newTelemetryDictionary['<NavMode>'], newTelemetryDictionary['<AlignSolnType>'], newTelemetryDictionary['<Surface3>'],
              newTelemetryDictionary['<Surface0>'], newTelemetryDictionary['<Surface6>'], '\n--> corrupt entry', newTelemetryDictionary)

    else:
        # If integrity check passes, push dictionary for values to be used in updating display
        print(newTelemetryDictionary)   #TODO: Debugging purposes only
        dataHandlerInstance.setRawTelemetryData(newTelemetryDictionary)
        print(dataHandlerInstance.getRawTelemetryData())    # TODO: Debugging purposes only

        UpdateHUD(self, dataHandlerInstance)