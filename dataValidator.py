import copy
import time, datetime, math


# ====================================================================================================================== Update HUD()
def UpdateHUD(self, dataHandler):

    #TODO: This is bad programming, test to find if this is possible then correctly write this code
    #   Only need to store the necessary values in the data handler instance after checking against
    #   complete set and integrity

    dict = dataHandler.getRawTelemetryData()

    try:

        # ----------------------------------------------------------- Elevator pos.
        surface6 = float(dict["<Surface6>"])
        surface6 = math.degrees(surface6)
        self.label_elevatorPositionValue.setText("{:.3f}".format(surface6))

        # ----------------------------------------------------------- Pitch rate.
        pitchRate = float(dict["<P>[rad/s]"])
        pitchRate = math.degrees(pitchRate)
        self.label_pitchRateValue.setText("{:.3f}".format(pitchRate))

        # ----------------------------------------------------------- Left aileron pos.
        surface0 = float(dict["<Surface0>"])
        surface0 = math.degrees(surface0)
        self.label_aileronPositionValue.setText("{:.3f}".format(surface0))

        # ----------------------------------------------------------- Roll rate
        rollRate = float(dict["<Q>[rad/s]"])
        rollRate = math.degrees(rollRate)
        self.label_rollRateValue.setText("{:.3f}".format(rollRate))

        # ----------------------------------------------------------- Rudder pos.
        surface3 = float(dict["<Surface3>"])
        surface3 = math.degrees(surface3)
        self.label_rudderPositionValue.setText("{:.3f}".format(surface3))

        # ----------------------------------------------------------- Yaw rate.
        yawRate = float(dict["<R>[rad/s]"])
        yawRate = math.degrees(yawRate)
        self.label_yawRateValue.setText("{:.3f}".format(yawRate))


    # FIXME: Re-write exception handling later, is for testing one update only.
    except Exception as ex:
        print("ERROR 1 handled, ", ex)


    # Check current values against user-defined limits and update display
    # self.CheckLimits_ElevatorPitch()
    # self.paramsToLog = [self.telemetry_data["<Clock>[ms]"], self.Surface6, self.pitch_y, self.Surface0, self.roll_y, self.Surface3, self.yaw_y]

    # Check if user opened a log file. If so, write to log.
    # if (self.logCreated == 1):
    #     print("To Log --> ", self.paramsToLog)
    #     self.WriteToLog()

    # self.elapsedTime = (time.time() - self.startTime)
    # self.label_infoBar_elapsedtime.setText(time.strftime("Elapsed Time: %H:%M:%S", time.gmtime(self.elapsedTime)))
