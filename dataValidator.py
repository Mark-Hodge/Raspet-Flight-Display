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

        # Set position and rate values to dictionary to be written to output log.
        dataHandler.finalDataToLog["Clock[ms]"] = dict["<Clock>[ms]"]

        dataHandler.finalDataToLog["Elevator Deflection[deg]"] = elevatorDeflection
        dataHandler.finalDataToLog["Aileron Deflection[deg]"] = aileronDeflection
        dataHandler.finalDataToLog["Rudder Deflection[deg]"] = rudderDeflection

        dataHandler.finalDataToLog["Pitch Rate[deg/s]"] = pitchRate
        dataHandler.finalDataToLog["Roll Rate[deg/s]"] = rollRate
        dataHandler.finalDataToLog["Yaw Rate[deg/s]"] = yawRate

    # FIXME: Re-write exception handling later, is for testing one update only
    except Exception as ex:
        print("\n --> ERROR 1 handled, ", ex, "\n")

# ====================================================================================================================== Check Pitch Conditions()
def CheckPitchDeflectionConditions(self, elevatorDeflection, pitchRate, dataHandler):

    warningCondition = 1.1 * ((2.0761 * elevatorDeflection) + 5.2714)
    alertCondition   = 1.2 * ((2.0761 * elevatorDeflection) + 5.2714)

    # Set warning and alert conditions to data to write to output log
    dataHandler.finalDataToLog["Pitch Rate Warning Condition[deg]"] = warningCondition
    dataHandler.finalDataToLog["Pitch Rate Alert Condition[deg]"] = warningCondition

    if (pitchRate <= warningCondition):

        self.label_pitchDeflectionValue.setText("{:.3f}".format(warningCondition))
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_pitchDeflection.setText("Warning")

        dataHandler.finalDataToLog["Pitch Deflection State"] = "Warning"

    elif (pitchRate <= alertCondition):

        self.label_pitchDeflectionValue.setText("{:.3f}".format(alertCondition))
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_pitchDeflection.setText("Alert")

        dataHandler.finalDataToLog["Pitch Deflection State"] = "Alert"

    else:
        labelValue = ("Normal")
        self.label_pitchDeflectionValue.setText(labelValue)
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_pitchDeflection.setText("Normal")


        dataHandler.finalDataToLog["Pitch Deflection State"] = "Normal"

# ====================================================================================================================== Check Roll Conditions()
def CheckRollDeflectionConditions(self, aileronDeflection, rollRate, dataHandler):

    warningCondition = 1.1 * ((2.8471 * aileronDeflection) + 1.5321)
    alertCondition   = 1.2 * ((2.8471 * aileronDeflection) + 1.5321)

    # Set warning and alert conditions to data to write to output log
    dataHandler.finalDataToLog["Roll Rate Warning Condition[deg]"] = warningCondition
    dataHandler.finalDataToLog["Roll Rate Alert Condition[deg]"] = warningCondition

    if (rollRate <= warningCondition):

        self.label_rollDeflectionValue.setText("{:.3f}".format(warningCondition))
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_rollDeflection.setText("Warning")

        dataHandler.finalDataToLog["Roll Deflection State"] = "Warning"

    elif (rollRate <= alertCondition):

        self.label_rollDeflectionValue.setText("{:.3f}".format(alertCondition))
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_rollDeflection.setText("Alert")

        dataHandler.finalDataToLog["Roll Deflection State"] = "Alert"

    else:
        labelValue = ("Normal")
        self.label_rollDeflectionValue.setText(labelValue)
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_rollDeflection.setText("Normal")

        dataHandler.finalDataToLog["Roll Deflection State"] = "Normal"

# ====================================================================================================================== Check Yaw Conditions()
def CheckYawDeflectionConditions(self, rudderDeflection, yawRate, dataHandler):

    warningCondition = 1.1 * ((0.2654 * rudderDeflection) + 0.8041)
    alertCondition   = 1.2 * ((0.2654 * rudderDeflection) + 0.8041)

    # Set warning and alert conditions to data to write to output log
    dataHandler.finalDataToLog["Yaw Rate Warning Condition[deg]"] = warningCondition
    dataHandler.finalDataToLog["Yaw Rate Alert Condition[deg]"] = warningCondition

    if (yawRate <= warningCondition):

        self.label_yawDeflectionValue.setText("{:.3f}".format(warningCondition))
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_yawDeflection.setText("Warning")

        dataHandler.finalDataToLog["Yaw Deflection State"] = "Warning"

    elif (yawRate <= alertCondition):

        self.label_yawDeflectionValue.setText("{:.3f}".format(alertCondition))
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_yawDeflection.setText("Alert")

        dataHandler.finalDataToLog["Yaw Deflection State"] = "Alert"

    else:
        labelValue = ("Normal")
        self.label_yawDeflectionValue.setText(labelValue)
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_yawDeflection.setText("Normal")

        dataHandler.finalDataToLog["Yaw Deflection State"] = "Normal"

    # Check if user opened a log file. If so, write to log.
    # if (self.logCreated == 1):
    #     print("To Log --> ", self.paramsToLog)
    #     self.WriteToLog()

    # self.elapsedTime = (time.time() - self.startTime)
    # self.label_infoBar_elapsedtime.setText(time.strftime("Elapsed Time: %H:%M:%S", time.gmtime(self.elapsedTime)))
