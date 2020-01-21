
# from limitsdialog import Ui_Dialog as Form
from dataHandler import DataHandler
from driver import *

def getLimits(self):
    elevatorPositionLimit = self.doubleSpinBox_elevatorPosition.value()
    aileronPositionLimit = self.doubleSpinBox_aileronPosition.value()
    rudderPositionLimit = self.doubleSpinBox_rudderPosition.value()

    pitchRateLimit = self.doubleSpinBox_pitchRate.value()
    rollRateLimit = self.doubleSpinBox_rollRate.value()
    yawRateLimit = self.doubleSpinBox_yawRate.value()
    print(yawRateLimit) # TODO: Delete after debugging
    DataHandler.setManuallyDefinedLimts({"elevatorPositionLimit": elevatorPositionLimit, "aileronPositionLimit": aileronPositionLimit, "rudderPositionLimit": rudderPositionLimit,
                                     "pitchRateLimit": pitchRateLimit, "rollRateLimit": rollRateLimit, "yawRateLimit": yawRateLimit})
