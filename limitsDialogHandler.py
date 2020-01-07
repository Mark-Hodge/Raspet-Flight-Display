
# from limitsdialog import Ui_Dialog as Form
from driver import *

def limitsDialogHandler_getLimits(self):
    elevatorPositionLimit = self.doubleSpinBox_elevatorPosition.value()
    aileronPositionLimit = self.doubleSpinBox_aileronPosition.value()
    rudderPositionLimit = self.doubleSpinBox_rudderPosition.value()

    pitchRateLimit = self.doubleSpinBox_pitchRate.value()
    rollRateLimit = self.doubleSpinBox_rollRate.value()
    yawRateLimit = self.doubleSpinBox_yawRate.value()