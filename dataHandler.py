
class DataHandler:

    def __init__(self):
        self.telemetryFile = ""
        self.manuallyDefinedLimits = {"elevatorPositionLimit": 0.0, "aileronPositionLimit": 0.0, "rudderPositionLimit": 0.0,
                                     "pitchRateLimit": 0.0, "rollRateLimit": 0.0, "yawRateLimit": 0.0}

    @classmethod
    def setManuallyDefinedLimts(cls, data):
        cls.manuallyDefinedLimits = data
        print(data, cls.manuallyDefinedLimits)

    # @classmethod
    # def setTelemetryFile(cls):

