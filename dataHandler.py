import csv

class DataHandler:

    def __init__(self):

        # Keeps track of the start, end, and elapsed time
        self.lockStartTime = False
        self.timeStartClicked = 0
        self.startTime = 0
        self.elapsedTime = 0

        # Holds the file descriptor of the PCC telemetry file that data is being retrieved from.
        self.telemetryFile = ""

        # Holds the file descriptor of the output log file that RFD is writing to.
        self.outputLogFile = ""

        # Dictionary that holds the keys and values of limits the user manually defines (not always used).
        # self.manuallyDefinedLimits = {"elevatorPositionLimit": 0.0, "aileronPositionLimit": 0.0, "rudderPositionLimit": 0.0,
        #                              "pitchRateLimit": 0.0, "rollRateLimit": 0.0, "yawRateLimit": 0.0}

        # Dictionary holds the keys and values of the entire data set from PCC (200 values per iteration).
        self.rawTelemetryData = {'<Clock>[ms]': [],'<Year>': [],'<Month>': [],'<Day>': [],'<Hours>': [],'<Minutes>': [],'<Seconds>': [],'<Lat>[rad]': [],'<Lon>[rad]': [],
    '<Height>[m]': [],'<VNorth>[m/s]': [],'<VEast>[m/s]': [],'<VDown>[m/s]': [],'<GroundSpeed>[m/s]': [],'<Direction>[rad]': [],'<Status>': [],
    '<NumSats>': [],'<VisibleSats>': [],'<PDOP>': [],'<InputV>[V]': [],'<InputC>[A]': [],'<ServoV>[V]': [],'<ServoC>[A]': [],
    '<FirstStageFail>': [],'<FiveDFail>': [],'<FiveAFail>': [],'<CPUFail>': [],'<GPSFail>': [],'<BoxTemp>[C]': [],'<Alt>[m]': [],'<TAS>[m/s]': [],'<OAT>[C]': [],
    '<Static>[Pa]': [],'<Dynamic>[Pa]': [],'<P>[rad/s]': [],'<Q>[rad/s]': [],'<R>[rad/s]': [],'<Xaccel>[m/s/s]': [],'<Yaccel>[m/s/s]': [],
    '<Zaccel>[m/s/s]': [],'<Roll>[rad]': [],'<Pitch>[rad]': [],'<Yaw>[rad]': [],'<MagHdg>[rad]': [],'<AGL>[m]': [],'<LeftRPM>': [],
    '<RightRPM>': [],'<Fuel>[kg]': [],'<FuelFlow>[g/hr]': [],'<WindSouth>[m/s]': [],'<WindWest>[m/s]': [],'<UplinkRatio>[%%]': [],
    '<DownlinkRatio>[%%]': [],'<RSSI>[dBm]': [],'<Surface0>': [],'<Surface1>': [],'<Surface2>': [],'<Surface3>': [],'<Surface4>': [],
    '<Surface5>': [],'<Surface6>': [],'<Surface7>': [],'<Surface8>': [],'<Surface9>': [],'<Surface10>': [],'<Surface11>': [],'<Surface12>': [],
    '<Surface13>': [],'<Surface14>': [],'<Surface15>': [],'<P_Bias>[rad/s]': [],'<Q_Bias>[rad/s]': [],'<R_Bias>[rad/s]': [],
    '<AX_Bias>[m/s/s]': [],'<AY_Bias>[m/s/s]': [],'<AZ_Bias>[m/s/s]': [],'<MagX>[mGauss]': [],'<MagY>[mGauss]': [],'<MagZ>[mGauss]': [],
    '<AP_Global>': [],'<MA_Mode>': [],'<AP_Mode>': [],'<WeightOnWheel>': [],'<TrackerStatus>': [],'<TrackerTarget>': [],'<Orbit>': [],
    '<LoopStatus0>': [],'<LoopTarget0>': [],'<LoopStatus1>': [],'<LoopTarget1>': [],'<LoopStatus2>': [],'<LoopTarget2>': [],'<LoopStatus3>': [],
    '<LoopTarget3>': [],'<LoopStatus4>': [],'<LoopTarget4>': [],'<LoopStatus5>': [],'<LoopTarget5>': [],'<LoopStatus6>': [],'<LoopTarget6>': [],
    '<LoopStatus7>': [],'<LoopTarget7>': [],'<AltCtrl>': [],'<Track_X>[m]': [],'<Track_Y>[m]': [],'<Track_Z>[m]': [],'<Track_VX>[m/s]': [],
    '<Track_VY>[m/s]': [],'<Track_VZ>[m/s]': [],'<ExtADC0>': [],'<ExtADC1>': [],'<ExtADC2>': [],'<ExtADC3>': [],'<NavMode>': [],'<PosGood>': [],
    '<VelGood>': [],'<BaroGood>': [],'<TASGood>': [],'<AGLGood>': [],'<MagGood>': [],'<YawGood>': [],'<AttGood>': [],'<GyroGood>': [],
    '<AccelGood>': [],'<MagBiasGood>': [],'<WindGood>': [],'<GPSWeek>': [],'<GPSITOW>': [],'<MBTime>[ms]': [],'<MBSolnType>': [],
    '<MBETA>[s]': [],'<MBHead>[rad]': [],'<MBNorth>[m]': [],'<MBEast>[m]': [],'<MBDown>[m]': [],'<MBCross>[m]': [],'<MBBelow>[m]': [],
    '<MBLat>[rad]': [],'<MBLon>[rad]': [],'<MBAlt>[m]': [],'<GSLat>[rad]': [],'<GSLon>[rad]': [],'<GSHeight>[m]': [],'<GSVNorth>[m/s]': [],
    '<GSVEast>[m/s]': [],'<GSVDown>[m/s]': [],'<GSGroundSpeed>[m/s]': [],'<GSDirection>[rad]': [],'<GSStatus>': [],'<GS_RSSI>': [],
    '<Deadman>': [],'<EngKill>': [],'<Drop>': [],'<Lights>': [],'<Parachute>': [],'<Brakes>': [],'<GPSTimeout>': [],'<CommTimeout>': [],
    '<Boundary>': [],'<FlightTimer>': [],'<FlightTerm>': [],'<AeroTerm>': [],'<UserAction0>': [],'<UserAction1>': [],'<UserAction2>': [],
    '<UserAction3>': [],'<UserAction4>': [],'<UserAction5>': [],'<UserAction6>': [],'<UserAction7>': [],'<CHT_A>': [],'<CHT_B>': [],
    '<EGT_A>': [],'<EGT_B>': [],'<IAT>': [],'<Volts>': [],'<MAP>': [],'<InjectTime>': [],'<InjectAngle>': [],'<TPS>': [],'<FuelPress>': [],
    '<AFR>': [],'<AFRcomp>': [],'<EngineTime>[hrs]': [],'<ECU_ERR_0>': [],'<ECU_ERR_1>': [],'<ECU_MODE>': [],'<PilotPrcnt>[%]': [],
    '<PilotRate>[Hz]': [],'<GSPilotPrcnt>[%]': [],'<GSPilotRate>[Hz]': [],'<AlignHdg>[rad]': [],'<AlignHdgSigma>[rad]': [],'<AlignSolnType>': [],
    '<ResidualPosNorth>[m]': [],'<ResidualPosEast>[m]': [],'<ResidualPosDown>[m]': [],'<ResidualVelNorth>[m/s]': [],'<ResidualVelEast>[m/s]': [],
    '<ResidualVelDown>[m/s]': []
    }

        # Data segment is a temporary array that holds the entire data set from PCC until the set is verified to be complete and not corrupt.
        self.rawDataSegment = []

        # Holds the final set of desired data after all integrity checks, calculations, and updates to the GUI have been made.
        self.finalDataToLog = {"Flag": None, "Clock[ms]": None, "Elevator Deflection[deg]": None, "Pitch Rate[deg/s]": None, "Aileron Deflection[deg]": None,
                               "Roll Rate[deg/s]": None, "Rudder Deflection[deg]": None, "Yaw Rate[deg/s]": None, "Pitch Rate Warning Condition[deg]": None, "Pitch Rate Alert Condition[deg]": None,
                               "Roll Rate Warning Condition[deg]": None, "Roll Rate Alert Condition[deg]": None, "Yaw Rate Warning Condition[deg]": None, "Yaw Rate Alert Condition[deg]": None,
                               "Pitch Deflection State": None, "Roll Deflection State": None, "Yaw Deflection State": None}

        # Holds the fieldnames for the .csv output log file
        self.fieldnames = ["Flag", "Clock[ms]", "Elevator Deflection[deg]", "Pitch Rate[deg/s]", "Aileron Deflection[deg]",
                               "Roll Rate[deg/s]", "Rudder Deflection[deg]", "Yaw Rate[deg/s]", "Pitch Rate Warning Condition[deg]", "Pitch Rate Alert Condition[deg]",
                               "Roll Rate Warning Condition[deg]", "Roll Rate Alert Condition[deg]", "Yaw Rate Warning Condition[deg]", "Yaw Rate Alert Condition[deg]",
                               "Pitch Deflection State", "Roll Deflection State", "Yaw Deflection State"]

        # Holds the dictionary writer containing the file descriptor and fieldnames for output log file
        self.writer = ""

        # Boolean value tracks the state of the flag button
        self.flagState = False

    # @classmethod
    # def setManuallyDefinedLimits(self, data):
    #     self.manuallyDefinedLimits = data
    #     print(data, self.manuallyDefinedLimits)

    # Updates the csv writer instance used for writing output to the log file and writes the header row
    def setWriter(self):
        self.writer = csv.DictWriter(self.outputLogFile, fieldnames=self.fieldnames)
        self.writer.writeheader()

    # Returns the csv writer
    def getWriter(self):
        return self.writer

    # Returns the state that the output log flag is currently set to
    def getFlagState(self):
        return self.flagState

    # Store the argument in the rawDataSegment object of the DataHandler instance
    def setDataSegment(self, dataSegment):
        self.rawDataSegment = dataSegment

    # Return the rawDataSegment
    def getDataSegment(self):
        return self.rawDataSegment

    # Store the argument in the telemetryFile object of the DataHandler instance
    def setTelemetryFile(self, telemetryFile):
        self.telemetryFile = telemetryFile
        print(self.telemetryFile) # TODO: Delete after debugging

    # Return the telemetryFile
    def getTelemetryFile(self):
        return self.telemetryFile

    # Store the argument in the outputLogFile object of the DataHandler instance
    def setOutputLogFile(self, outputLogFile):
        self.outputLogFile = outputLogFile
        print(self.outputLogFile) # TODO: Debugging purposes only

    # Return the outPutLogFile
    def getOutputLogFile(self):
        return self.outputLogFile

    # Clear then reset the dictionary with key and empty values
    def resetRawTelemetryData(self):
        self.rawTelemetryData = {'<Clock>[ms]': [],'<Year>': [],'<Month>': [],'<Day>': [],'<Hours>': [],'<Minutes>': [],'<Seconds>': [],'<Lat>[rad]': [],'<Lon>[rad]': [],
    '<Height>[m]': [],'<VNorth>[m/s]': [],'<VEast>[m/s]': [],'<VDown>[m/s]': [],'<GroundSpeed>[m/s]': [],'<Direction>[rad]': [],'<Status>': [],
    '<NumSats>': [],'<VisibleSats>': [],'<PDOP>': [],'<InputV>[V]': [],'<InputC>[A]': [],'<ServoV>[V]': [],'<ServoC>[A]': [],
    '<FirstStageFail>': [],'<FiveDFail>': [],'<FiveAFail>': [],'<CPUFail>': [],'<GPSFail>': [],'<BoxTemp>[C]': [],'<Alt>[m]': [],'<TAS>[m/s]': [],'<OAT>[C]': [],
    '<Static>[Pa]': [],'<Dynamic>[Pa]': [],'<P>[rad/s]': [],'<Q>[rad/s]': [],'<R>[rad/s]': [],'<Xaccel>[m/s/s]': [],'<Yaccel>[m/s/s]': [],
    '<Zaccel>[m/s/s]': [],'<Roll>[rad]': [],'<Pitch>[rad]': [],'<Yaw>[rad]': [],'<MagHdg>[rad]': [],'<AGL>[m]': [],'<LeftRPM>': [],
    '<RightRPM>': [],'<Fuel>[kg]': [],'<FuelFlow>[g/hr]': [],'<WindSouth>[m/s]': [],'<WindWest>[m/s]': [],'<UplinkRatio>[%%]': [],
    '<DownlinkRatio>[%%]': [],'<RSSI>[dBm]': [],'<Surface0>': [],'<Surface1>': [],'<Surface2>': [],'<Surface3>': [],'<Surface4>': [],
    '<Surface5>': [],'<Surface6>': [],'<Surface7>': [],'<Surface8>': [],'<Surface9>': [],'<Surface10>': [],'<Surface11>': [],'<Surface12>': [],
    '<Surface13>': [],'<Surface14>': [],'<Surface15>': [],'<P_Bias>[rad/s]': [],'<Q_Bias>[rad/s]': [],'<R_Bias>[rad/s]': [],
    '<AX_Bias>[m/s/s]': [],'<AY_Bias>[m/s/s]': [],'<AZ_Bias>[m/s/s]': [],'<MagX>[mGauss]': [],'<MagY>[mGauss]': [],'<MagZ>[mGauss]': [],
    '<AP_Global>': [],'<MA_Mode>': [],'<AP_Mode>': [],'<WeightOnWheel>': [],'<TrackerStatus>': [],'<TrackerTarget>': [],'<Orbit>': [],
    '<LoopStatus0>': [],'<LoopTarget0>': [],'<LoopStatus1>': [],'<LoopTarget1>': [],'<LoopStatus2>': [],'<LoopTarget2>': [],'<LoopStatus3>': [],
    '<LoopTarget3>': [],'<LoopStatus4>': [],'<LoopTarget4>': [],'<LoopStatus5>': [],'<LoopTarget5>': [],'<LoopStatus6>': [],'<LoopTarget6>': [],
    '<LoopStatus7>': [],'<LoopTarget7>': [],'<AltCtrl>': [],'<Track_X>[m]': [],'<Track_Y>[m]': [],'<Track_Z>[m]': [],'<Track_VX>[m/s]': [],
    '<Track_VY>[m/s]': [],'<Track_VZ>[m/s]': [],'<ExtADC0>': [],'<ExtADC1>': [],'<ExtADC2>': [],'<ExtADC3>': [],'<NavMode>': [],'<PosGood>': [],
    '<VelGood>': [],'<BaroGood>': [],'<TASGood>': [],'<AGLGood>': [],'<MagGood>': [],'<YawGood>': [],'<AttGood>': [],'<GyroGood>': [],
    '<AccelGood>': [],'<MagBiasGood>': [],'<WindGood>': [],'<GPSWeek>': [],'<GPSITOW>': [],'<MBTime>[ms]': [],'<MBSolnType>': [],
    '<MBETA>[s]': [],'<MBHead>[rad]': [],'<MBNorth>[m]': [],'<MBEast>[m]': [],'<MBDown>[m]': [],'<MBCross>[m]': [],'<MBBelow>[m]': [],
    '<MBLat>[rad]': [],'<MBLon>[rad]': [],'<MBAlt>[m]': [],'<GSLat>[rad]': [],'<GSLon>[rad]': [],'<GSHeight>[m]': [],'<GSVNorth>[m/s]': [],
    '<GSVEast>[m/s]': [],'<GSVDown>[m/s]': [],'<GSGroundSpeed>[m/s]': [],'<GSDirection>[rad]': [],'<GSStatus>': [],'<GS_RSSI>': [],
    '<Deadman>': [],'<EngKill>': [],'<Drop>': [],'<Lights>': [],'<Parachute>': [],'<Brakes>': [],'<GPSTimeout>': [],'<CommTimeout>': [],
    '<Boundary>': [],'<FlightTimer>': [],'<FlightTerm>': [],'<AeroTerm>': [],'<UserAction0>': [],'<UserAction1>': [],'<UserAction2>': [],
    '<UserAction3>': [],'<UserAction4>': [],'<UserAction5>': [],'<UserAction6>': [],'<UserAction7>': [],'<CHT_A>': [],'<CHT_B>': [],
    '<EGT_A>': [],'<EGT_B>': [],'<IAT>': [],'<Volts>': [],'<MAP>': [],'<InjectTime>': [],'<InjectAngle>': [],'<TPS>': [],'<FuelPress>': [],
    '<AFR>': [],'<AFRcomp>': [],'<EngineTime>[hrs]': [],'<ECU_ERR_0>': [],'<ECU_ERR_1>': [],'<ECU_MODE>': [],'<PilotPrcnt>[%]': [],
    '<PilotRate>[Hz]': [],'<GSPilotPrcnt>[%]': [],'<GSPilotRate>[Hz]': [],'<AlignHdg>[rad]': [],'<AlignHdgSigma>[rad]': [],'<AlignSolnType>': [],
    '<ResidualPosNorth>[m]': [],'<ResidualPosEast>[m]': [],'<ResidualPosDown>[m]': [],'<ResidualVelNorth>[m/s]': [],'<ResidualVelEast>[m/s]': [],
    '<ResidualVelDown>[m/s]': []
    }

    # Store the argument in the rawTelemetryDictionary object of the DataHandler instance
    def setRawTelemetryData(self, newTelemetryDictionary):
        # print("OLD: ", self.rawTelemetryData) #TODO: Debugging purposes only, delete later
        self.rawTelemetryData = newTelemetryDictionary
        # print("NEW: ", self.rawTelemetryData) #TODO: Debugging purposes only, delete later

    # Return the rawTelemetryData object
    def getRawTelemetryData(self):
        return self.rawTelemetryData

