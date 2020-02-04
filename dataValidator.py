import time, datetime, math

# ====================================================================================================================== Update HUD()
def UpdateHUD(self, dataHandler):

    #TODO: This is bad programming, test to find if this is possible then correctly write this code
    #   Only need to store the necessary values in the data handler instance after checking against
    #   complete set and integrity

    # TODO: NOTE  P,    Q,    R
    #           Roll, Pitch, Yaw
    #   Control Authority Equations, Correction -> PitchRate: 1.1(2.0761x + 7.3747)

    dict = dataHandler.getRawTelemetryData()

    try:
        # ----------------------------------------------------------- Elevator pos.
        elevatorDeflection= float(dict["<Surface6>"])
        elevatorDeflection= math.degrees(elevatorDeflection)
        self.label_elevatorPositionValue.setText("{:.3f}".format(elevatorDeflection))

        # ----------------------------------------------------------- Pitch rate.
        pitchRate = float(dict["<Q>[rad/s]"])
        pitchRate = math.degrees(pitchRate)
        self.label_pitchRateValue.setText("{:.3f}".format(pitchRate))

        # ----------------------------------------------------------- Left aileron pos.
        aileronDeflection = float(dict["<Surface0>"])
        aileronDeflection= math.degrees(aileronDeflection)
        self.label_aileronPositionValue.setText("{:.3f}".format(aileronDeflection))

        # ----------------------------------------------------------- Roll rate.
        rollRate = float(dict["<P>[rad/s]"])
        rollRate = math.degrees(rollRate)
        self.label_rollRateValue.setText("{:.3f}".format(rollRate))

        # ----------------------------------------------------------- Rudder pos.
        rudderDeflection = float(dict["<Surface3>"])
        rudderDeflection= math.degrees(rudderDeflection)
        self.label_rudderPositionValue.setText("{:.3f}".format(rudderDeflection))

        # ----------------------------------------------------------- Yaw rate.
        yawRate = float(dict["<R>[rad/s]"])
        yawRate = math.degrees(yawRate)
        self.label_yawRateValue.setText("{:.3f}".format(yawRate))

        # Check current values against limits and update display
        CheckPitchDeflectionConditions(self, elevatorDeflection, pitchRate)
        CheckRollDeflectionConditions(self, aileronDeflection, rollRate)
        CheckYawDeflectionConditions(self, rudderDeflection, yawRate)

    # FIXME: Re-write exception handling later, is for testing one update only
    except Exception as ex:
        print("\n --> ERROR 1 handled, ", ex, "\n")

# ====================================================================================================================== Check Pitch Conditions()
def CheckPitchDeflectionConditions(self, elevatorDeflection, pitchRate):

    # --------------------------------------------------------------------------------------------- Warning condition.
    warningCondition = 1.1 * ((2.0761 * elevatorDeflection) + 7.3747)
    alertCondition   = 1.2 * ((2.0761 * elevatorDeflection) + 7.3747)

    if (pitchRate <= warningCondition):

        self.label_pitchDeflectionValue.setText("{:.3f}".format(warningCondition))
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_pitchDeflection.setText("Warning")

    elif (pitchRate <= alertCondition):

        self.label_pitchDeflectionValue.setText("{:.3f}".format(alertCondition))
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_pitchDeflection.setText("Alert")

    else:
        labelValue = ("Normal")
        self.label_pitchDeflectionValue.setText(labelValue)
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_pitchDeflection.setText("Normal")

# ====================================================================================================================== Check Roll Conditions()
def CheckRollDeflectionConditions(self, aileronDeflection, rollRate):

    # --------------------------------------------------------------------------------------------- Warning condition.
    warningCondition = 1.1 * ((2.8471 * aileronDeflection) + 1.5321)
    alertCondition = 1.2 * ((2.8471 * aileronDeflection) + 1.5321)

    if (rollRate <= warningCondition):

        self.label_rollDeflectionValue.setText("{:.3f}".format(warningCondition))
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_rollDeflection.setText("Warning")

    elif (rollRate <= alertCondition):

        self.label_rollDeflectionValue.setText("{:.3f}".format(alertCondition))
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_rollDeflection.setText("Alert")

    else:
        labelValue = ("Normal")
        self.label_rollDeflectionValue.setText(labelValue)
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_rollDeflection.setText("Normal")

# ====================================================================================================================== Check Yaw Conditions()
def CheckYawDeflectionConditions(self, rudderDeflection, yawRate):

    # --------------------------------------------------------------------------------------------- Warning condition.
    warningCondition = 1.1 * ((0.2654 * rudderDeflection) + 0.8041)
    alertCondition = 1.2 * ((0.2654 * rudderDeflection) + 0.8041)

    if (yawRate <= warningCondition):

        self.label_yawDeflectionValue.setText("{:.3f}".format(warningCondition))
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_yawDeflection.setText("Warning")

    elif (yawRate <= alertCondition):

        self.label_yawDeflectionValue.setText("{:.3f}".format(alertCondition))
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_yawDeflection.setText("Alert")

    else:
        labelValue = ("Normal")
        self.label_yawDeflectionValue.setText(labelValue)
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_yawDeflection.setText("Normal")

    # self.paramsToLog = [self.telemetry_data["<Clock>[ms]"], self.Surface6, self.pitch_y, self.Surface0, self.roll_y, self.Surface3, self.yaw_y]

    # Check if user opened a log file. If so, write to log.
    # if (self.logCreated == 1):
    #     print("To Log --> ", self.paramsToLog)
    #     self.WriteToLog()

    # self.elapsedTime = (time.time() - self.startTime)
    # self.label_infoBar_elapsedtime.setText(time.strftime("Elapsed Time: %H:%M:%S", time.gmtime(self.elapsedTime)))
