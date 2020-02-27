import time, datetime, math

# ====================================================================================================================== Update HUD()
from PyQt5.QtWidgets import QApplication


def UpdateHUD(self, dataHandler):

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
        CheckPitchDeflectionConditions(self, elevatorDeflection, pitchRate, dataHandler)
        CheckRollDeflectionConditions(self, aileronDeflection, rollRate, dataHandler)
        CheckYawDeflectionConditions(self, rudderDeflection, yawRate, dataHandler)

        QApplication.processEvents()

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

    # Take the absolute value of rate and of surface deflection
    absoluteRate = abs(pitchRate)
    absoluteDeflection = abs(elevatorDeflection)

    # Calculate the upper bound of the warning and alert conditions. Take the absolute value
    warningCondition = abs(1.1 * ((2.0761 * absoluteDeflection) + 5.2714))
    alertCondition = abs(1.2 * ((2.0761 * absoluteDeflection) + 5.2714))

    # TODO: Debugging purposes, remove from production release
    print("\nPitch Rate\t\tElevator Deflection\t\tWarning Condition\t\tAlert Condition")
    print(str(absoluteRate) + "\t" + str(absoluteDeflection) + "\t" + str(warningCondition) + "\t" + str(alertCondition) + "\n")
    #   END TODO ^

    # Set warning and alert conditions to data to write to output log
    dataHandler.finalDataToLog["Pitch Rate Warning Condition[deg]"] = warningCondition
    dataHandler.finalDataToLog["Pitch Rate Alert Condition[deg]"] = alertCondition

    # Set the text of the label to the current absolute value of the warning/alert condition
    labelValue = ("Warning: " + "{:.9f}".format(warningCondition) + "\nAlert: " + "{:.9f}".format(
        alertCondition))

    # Evaluate absolute value of rate at or below the warning condition
    if (absoluteRate <= warningCondition):

        # Change and update the text and color of the labels/buttons
        self.label_pitchDeflectionValue.setText(labelValue)
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_pitchDeflection.setText("Warning")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Pitch Deflection State"] = "Warning"

    # Evaluate absolute value of rate between the alert condition and warning condition
    elif (absoluteRate <= alertCondition) and (absoluteRate > warningCondition):

        # Change and update the text and color of the labels/buttons
        self.label_pitchDeflectionValue.setText(labelValue)
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_pitchDeflection.setText("Alert")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Pitch Deflection State"] = "Alert"

    else:

        # Change and update the text and color of the labels/buttons
        self.label_pitchDeflectionValue.setText(labelValue)
        self.pushButton_pitchDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_pitchDeflection.setText("Normal")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Pitch Deflection State"] = "Normal"

# ====================================================================================================================== Check Roll Conditions()
def CheckRollDeflectionConditions(self, aileronDeflection, rollRate, dataHandler):

    # Take the absolute value of rate and of surface deflection
    absoluteRate = abs(rollRate)
    absoluteDeflection = abs(aileronDeflection)

    # Calculate the upper bound of the warning and alert conditions. Take the absolute value
    warningCondition = abs(1.1 * ((2.8471 * absoluteDeflection) + 1.5321))
    alertCondition = abs(1.2 * ((2.8471 * absoluteDeflection) + 1.5321))

    # TODO: Debugging purposes, remove from production release
    print("\nRoll Rate\t\tAileron Deflection\t\tWarning Condition\t\tAlert Condition")
    print(str(absoluteRate) + "\t" + str(absoluteDeflection) + "\t" + str(warningCondition) + "\t" + str(alertCondition) + "\n")
    #   END TODO ^

    # Set warning and alert conditions to data to write to output log
    dataHandler.finalDataToLog["Roll Rate Warning Condition[deg]"] = warningCondition
    dataHandler.finalDataToLog["Roll Rate Alert Condition[deg]"] = alertCondition

    # Set the text of the label to the current absolute value of the warning/alert condition
    labelValue = ("Warning: " + "{:.9f}".format(warningCondition) + "\nAlert: " + "{:.9f}".format(
        alertCondition))

    # Evaluate absolute value of rate at or below the warning condition
    if (absoluteRate <= warningCondition):

        # Change and update the text and color of the labels/buttons
        self.label_rollDeflectionValue.setText(labelValue)
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_rollDeflection.setText("Warning")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Roll Deflection State"] = "Warning"

    # Evaluate absolute value of rate between the alert condition and warning condition
    elif (absoluteRate <= alertCondition) and (absoluteRate > warningCondition):

        # Change and update the text and color of the labels/buttons
        self.label_rollDeflectionValue.setText(labelValue)
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_rollDeflection.setText("Alert")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Roll Deflection State"] = "Alert"

    else:

        # Change and update the text and color of the labels/buttons
        self.label_rollDeflectionValue.setText(labelValue)
        self.pushButton_rollDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_rollDeflection.setText("Normal")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Roll Deflection State"] = "Normal"

# ====================================================================================================================== Check Yaw Conditions()
def CheckYawDeflectionConditions(self, rudderDeflection, yawRate, dataHandler):

    # Take the absolute value of rate and of surface deflection
    absoluteRate = abs(yawRate)
    absoluteDeflection = abs(rudderDeflection)

    # Calculate the upper bound of the warning and alert conditions. Take the absolute value
    warningCondition = abs(1.1 * ((0.2654 * absoluteDeflection) + 0.8041))
    alertCondition = abs(1.2 * ((0.2654 * absoluteDeflection) + 0.8041))

    # TODO: Debugging purposes, remove from production release
    print("\nYaw Rate\t\tRudder Deflection\t\tWarning Condition\t\tAlert Condition")
    print(str(absoluteRate) + "\t" + str(absoluteDeflection) + "\t" + str(warningCondition) + "\t" + str(alertCondition) + "\n")
    #   END TODO ^

    # Set warning and alert conditions to data to write to output log
    dataHandler.finalDataToLog["Yaw Rate Warning Condition[deg]"] = warningCondition
    dataHandler.finalDataToLog["Yaw Rate Alert Condition[deg]"] = alertCondition

    # Set the text of the label to the current absolute value of the warning/alert condition
    labelValue = ("Warning: " + "{:.9f}".format(warningCondition) + "\nAlert: " + "{:.9f}".format(
        alertCondition))

    # Evaluate absolute value of rate at or below the warning condition
    if (absoluteRate <= warningCondition):

        # Change and update the text and color of the labels/buttons
        self.label_yawDeflectionValue.setText(labelValue)
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: red;}')
        self.pushButton_yawDeflection.setText("Warning")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Yaw Deflection State"] = "Warning"

    # Evaluate absolute value of rate between the alert condition and warning condition
    elif (absoluteRate <= alertCondition) and (absoluteRate > warningCondition):

        # Change and update the text and color of the labels/buttons
        self.label_yawDeflectionValue.setText(labelValue)
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: yellow;}')
        self.pushButton_yawDeflection.setText("Alert")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Yaw Deflection State"] = "Alert"

    else:

        # Change and update the text and color of the labels/buttons
        self.label_yawDeflectionValue.setText(labelValue)
        self.pushButton_yawDeflection.setStyleSheet('QPushButton {background-color: #e1e1e1;}')
        self.pushButton_yawDeflection.setText("Normal")

        # Save the state to the container that will be written to the output log file
        dataHandler.finalDataToLog["Yaw Deflection State"] = "Normal"
