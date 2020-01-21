import cls as cls

class DataHandler:

    def __init__(self):
        self.telemetryFile = ""
        self.manuallyDefinedLimits = {"elevatorPositionLimit": 0.0, "aileronPositionLimit": 0.0, "rudderPositionLimit": 0.0,
                                     "pitchRateLimit": 0.0, "rollRateLimit": 0.0, "yawRateLimit": 0.0}
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


    @classmethod
    def setManuallyDefinedLimts(cls, data):
        cls.manuallyDefinedLimits = data
        print(data, cls.manuallyDefinedLimits)

    @classmethod
    def setTelemetryFile(cls, telemetryFile):
        cls.telemetryFile = telemetryFile
        print(cls.telemetryFile) # TODO: Delete after debugging

    @classmethod
    def getTelemetryFile(cls):
        return cls.telemetryFile

    @classmethod
    def resetRawTelemetryData(cls):
        cls.rawTelemetryData = {'<Clock>[ms]': [],'<Year>': [],'<Month>': [],'<Day>': [],'<Hours>': [],'<Minutes>': [],'<Seconds>': [],'<Lat>[rad]': [],'<Lon>[rad]': [],
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

    @classmethod
    def setRawTelemetryData(cls, newTelemetryDictionary):
        print("OLD: ", cls.rawTelemetryData)
        cls.rawTelemetryData = newTelemetryDictionary
        print("NEW: ", cls.rawTelemetryData)

    @classmethod
    def getRawTelemetryData(cls):
        return cls.rawTelemetryData

