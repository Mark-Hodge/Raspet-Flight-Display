"""
Copyright (c) 2019 Mark Hodge
Version 1.0.0
Last Update: August 23, 2019 12:27:00 CST
"""

import os
import csv
import math
import time
import datetime
from tkinter import *
from tkinter import filedialog


class Interface:

    def __init__(self, master):

        self.telemetry_data = {
    '<Clock>[ms]': [],'<Year>': [],'<Month>': [],'<Day>': [],'<Hours>': [],'<Minutes>': [],'<Seconds>': [],'<Lat>[rad]': [],'<Lon>[rad]': [],
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


        # Set styling for text on screen.
        font = 'Times New Roman'
        fontSize = 12
        backGround = '#321000'
        foreGround = '#000fff000'


        # Contains toolbar and holds X axis at top of window.
        toolFrame = Frame(master)
        toolFrame.pack(side='top', fill=BOTH)

        statusFrame = Frame(master)
        statusFrame.pack(side='bottom', fill=X)


        # Contains entire window below toolframe and holds other frames.
        self.mainframe = Frame(master)
        self.mainframe.pack(side='top', fill=BOTH, expand=TRUE)


        # Contains Column 0
        leftFrame = Frame(master)
        leftFrame.place(in_=self.mainframe, anchor='w', relx=0.05, rely=0.3)


        # Contains Column 1
        centerFrame = Frame(master)
        centerFrame.place(in_=self.mainframe, anchor='center', relx=0.5, rely=0.3)


        # Contains column 2
        rightFrame = Frame(master)
        rightFrame.place(in_=self.mainframe, anchor='e', relx=0.95, rely=0.3)


        # Drop down menu
        menu = Menu(master)
        master.config(menu=menu)
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Open...", command=self.OpenFile)
        subMenu.add_command(label="New Log File", command=self.CreateLogFile)
        subMenu.add_command(label="Define Limits", command=self.DefineLimits)
        subMenu.add_separator()
        subMenu.add_command(label="Quit", command=master.destroy)


        # Toolbar placed across the top of screen
        self.toolBarHeader = StringVar()
        self.toolBarHeader.set("File: N/A")
        toolbar = Frame(toolFrame, bd=1, relief=SUNKEN)
        tBarLabel = Label(toolFrame, textvariable=self.toolBarHeader, fg="Black", pady=5, relief=SUNKEN, anchor=W)
        tBarLabel.pack(side='top', fill=X)

        # Flag data in logfile button.
        self.flagButton = Button(toolFrame, padx=15, pady=0, text="Flag", bg="Light Gray", font=(font, 11), command=self.UpdateFlag)
        self.flagButton.place(in_=tBarLabel, anchor='w', relx=0.81, rely=0.5)

        # Start button placed in tool bar at right edge of screen. Locked until file opened and starts file processing on click.
        self.startButton = Button(toolFrame, text="Start", padx=15, pady=0, bg="Light Gray", fg="Green", font=(font, 11),
                                  state=DISABLED, relief=SUNKEN, command=self.StartProgram)
        self.startButton.place(in_=tBarLabel, anchor='w', relx=0.89, rely=0.5)

        # Quit button placed in tool bar at right edge of screen
        self.quitButton = Button(toolFrame, text="quit", padx=15, pady=0, bg="Light Gray", fg="Red", font=(font, 11), command=master.destroy)
        self.quitButton.place(in_=tBarLabel, anchor='w', relx=0.95, rely=0.5)

        toolbar.pack(side='top')


        # Status bar
        self.runStatusValue = StringVar()
        self.runStatusValue.set("Status: Not Running")
        statusBar = Label(statusFrame, textvariable=self.runStatusValue, bd=1, relief=SUNKEN, anchor=W)
        statusBar.pack(side='bottom', fill=X)

        self.limitsStatusValue = StringVar()
        self.limitsStatusValue.set("Limits: N/A")
        self.limitsStatus = Label(statusFrame, textvariable=self.limitsStatusValue, fg="Black", padx=15, pady=0)
        self.limitsStatus.place(in_=statusBar, anchor='w', relx=0.100, rely=0.5)

        self.logStatusValue = StringVar()
        self.logStatusValue.set("Log: Not Logging")
        self.logStatus = Label(statusFrame, textvariable=self.logStatusValue, fg="Black", padx=15, pady=0)
        self.logStatus.place(in_=statusBar, anchor='w', relx=0.175, rely=0.5)

        self.startTimeValue = StringVar()
        self.startTimeValue.set("Start Time: 00:00:00")
        self.startTimeLabel = Label(statusFrame, textvariable=self.startTimeValue, fg="Black", padx=15, pady=0)
        self.startTimeLabel.place(in_=statusBar, anchor='w', relx=0.785, rely=0.5)

        self.elapsedTimeValue = StringVar()
        self.elapsedTimeValue.set("Elapsed Time: 00:00:00")
        self.elapsedTimeLabel = Label(statusFrame, textvariable=self.elapsedTimeValue, fg="Black", padx=15, pady=0)
        self.elapsedTimeLabel.place(in_=statusBar, anchor='w', relx=0.885, rely=0.5)



        # Initialize parameter values
        # --------------------------------- Elevator position
        self.elevator_value = StringVar()
        self.elevator_value.set("null")
        self.elevator_state = StringVar()
        self.elevator_state.set("Off")

        # --------------------------------- Rudder position
        self.rudder_value = StringVar()
        self.rudder_value.set("null")
        self.rudder_state = StringVar()
        self.rudder_state.set("Off")

        # --------------------------------- Aileron position
        self.aileron_value = StringVar()
        self.aileron_value.set("null")
        self.aileron_state = StringVar()
        self.aileron_state.set("Off")

        # --------------------------------- Pitch rate
        self.pitch_value = StringVar()
        self.pitch_value.set("null")
        self.pitch_state = StringVar()
        self.pitch_state.set("Off")

        # --------------------------------- Roll rate
        self.roll_value = StringVar()
        self.roll_value.set("null")
        self.roll_state = StringVar()
        self.roll_state.set("Off")

        # --------------------------------- Yaw rate
        self.yaw_value = StringVar()
        self.yaw_value.set("null")
        self.yaw_state = StringVar()
        self.yaw_state.set("Off")

        self.flagValue = 0

        # Sets all alarms to neutral on startup
        alarmColor = "Light Gray"


        # Add empty space between first and second row of parameters for.
        aesthetic_space0 = Label(leftFrame).grid(row=3, column=0, padx=0, pady=25)
        aesthetic_space1 = Label(centerFrame).grid(row=3, column=0, padx=0, pady=25)
        aesthetic_space2 = Label(rightFrame).grid(row=3, column=0, padx=0, pady=25)


        # Position paremeters on screen
        # ------------------------------------------------------------------------------------------------------------------ Elevator position
        self.elevator_alarm = Button(leftFrame, padx=25, pady=0, textvariable=self.elevator_state, bg=alarmColor)
        self.elevator_alarm.grid(row=0, column=0)

        elevator_header = Label(leftFrame, padx=25, pady=5, text="Elevator Pos. (deg)", fg="Black", font=(font, fontSize))
        elevator_header.grid(row=1, column=0)

        elevator_label = Label(leftFrame, padx=5, pady=5, textvariable=self.elevator_value, fg="Black", font=(font, fontSize))
        elevator_label.grid(row=2, column=0)

        # ------------------------------------------------------------------------------------------------------------------ Aileron position
        self.aileron_alarm = Button(centerFrame, padx=25, pady=0, textvariable=self.aileron_state, bg=alarmColor)
        self.aileron_alarm.grid(row=0, column=0)

        aileron_header = Label(centerFrame, padx=25, pady=5, text="Aileron Pos. (deg)", fg="Black", font=(font, fontSize))
        aileron_header.grid(row=1, column=0)

        aileron_label = Label(centerFrame, padx=5, pady=5, textvariable=self.aileron_value, fg="Black", font=(font, fontSize))
        aileron_label.grid(row=2, column=0)

        # ------------------------------------------------------------------------------------------------------------------ Rudder position
        self.rudder_alarm = Button(rightFrame, padx=25, pady=0, textvariable=self.rudder_state, bg=alarmColor)
        self.rudder_alarm.grid(row=0, column=0)

        rudder_header = Label(rightFrame, padx=25, pady=5, text="Rudder Pos. (deg)", fg="Black", font=(font, fontSize))
        rudder_header.grid(row=1, column=0)

        rudder_label = Label(rightFrame, padx=5, pady=5, textvariable=self.rudder_value, fg="Black", font=(font, fontSize))
        rudder_label.grid(row=2, column=0)

        # ------------------------------------------------------------------------------------------------------------------ Pitch rate
        self.pitch_alarm = Button(leftFrame, padx=25, pady=0, textvariable=self.pitch_state, bg=alarmColor)
        self.pitch_alarm.grid(row=4, column=0)

        pitch_header = Label(leftFrame, padx=25, pady=5, text="Pitch Rate (deg/s)", fg="Black", font=(font, fontSize))
        pitch_header.grid(row=5, column=0)

        pitch_label = Label(leftFrame, padx=5, pady=5, textvariable=self.pitch_value, fg="Black", font=(font, fontSize))
        pitch_label.grid(row=6, column=0)

        # ------------------------------------------------------------------------------------------------------------------ Roll rate
        self.roll_alarm = Button(centerFrame, padx=25, pady=0, textvariable=self.roll_state, bg=alarmColor)
        self.roll_alarm.grid(row=4, column=0)

        roll_header = Label(centerFrame, padx=25, pady=5, text="Roll Rate (deg/s)", fg="Black", font=(font, fontSize))
        roll_header.grid(row=5, column=0)

        roll_label = Label(centerFrame, padx=5, pady=5, textvariable=self.roll_value, fg="Black", font=(font, fontSize))
        roll_label.grid(row=6, column=0)

        # ------------------------------------------------------------------------------------------------------------------ yaw rate
        self.yaw_alarm = Button(rightFrame, padx=25, pady=0, textvariable=self.yaw_state, bg=alarmColor)
        self.yaw_alarm.grid(row=4, column=0)

        yaw_header = Label(rightFrame, padx=25, pady=5, text="Yaw Rate (deg/s)", fg="Black", font=(font, fontSize))
        yaw_header.grid(row=5, column=0)

        yaw_label = Label(rightFrame, padx=5, pady=5, textvariable=self.yaw_value, fg="Black", font=(font, fontSize))
        yaw_label.grid(row=6, column=0)


    # ====================================================================================================================== Open File()
    def OpenFile(self):
        # Call file navigator on mouse click and display path on screen
        filename = filedialog.askopenfilename()
        self.toolBarHeader.set("File: %s" % filename)

        # Open file and move cursur to EOF
        try:
            self.fh = open(filename, 'r')
            self.fh.seek(0, os.SEEK_END)

        # Hand errors in opening or navigating to EOF
        except Exception as ex:
            print("Could not open file: ERROR --> ", ex)

        # self.mainframe.update()
        self.startButton.configure(state=NORMAL, relief=RAISED)     # Un-lock start button if success


    # ====================================================================================================================== Create Log File()
    def CreateLogFile(self):
        # Call file navigator on mouse click and display path on screen
        log_filename = filedialog.askopenfilename()

        # Open file and move cursor to EOF
        try:
            self.log_fh = open(log_filename, 'a', newline='')
            self.log_fh.seek(0, os.SEEK_END)
            self.logStatusValue.set("Log: %s" % log_filename)
            self.logCreated = 1

            fieldnames = ["<FLAG>", "<Clock>[ms]", "<Elevator Position>[deg]", "State0", "<Pitch Rate>[deg/s]", "State1",
                          "<Aileron Position>[deg]", "State2", "<Roll Rate>[deg/s]", "State3", "<Rudder Position>[deg]", "State4",
                          "<Yaw Rate>[deg/s]", "State5"]
            self.writer = csv.DictWriter(self.log_fh, fieldnames=fieldnames)
            self.writer.writeheader()

        # Handle errors in opening or navigating to EOF
        except Exception as ex:
            print("Could not open file: ERROR --> ", ex)
            self.logCreated = 0


    # ====================================================================================================================== Update Flag()
    def UpdateFlag(self):
        print(self.flagValue)

        if self.flagValue == 0:
            self.flagValue = 1
            self.flagButton.configure(bg="Lime Green")
        else:
            self.flagValue = 0
            self.flagButton.configure(bg="Light Gray")


    # ====================================================================================================================== Write To Log()
    def WriteToLog(self):
        elePos_state = str(self.elevator_state.get())
        pitRat_state = str(self.pitch_state.get())
        ailPos_state = str(self.aileron_state.get())
        rolRat_state = str(self.roll_state.get())
        rudPos_state = str(self.rudder_state.get())
        yawRat_state = str(self.yaw_state.get())

        if (self.flagValue == 0):
            self.writer.writerow({"<FLAG>": "0", "<Clock>[ms]": self.paramsToLog[0], "<Elevator Position>[deg]": self.paramsToLog[1],
                    "State0": elePos_state, "<Pitch Rate>[deg/s]": self.paramsToLog[2], "State1": pitRat_state,
                    "<Aileron Position>[deg]": self.paramsToLog[3], "State2": ailPos_state,
                    "<Roll Rate>[deg/s]": self.paramsToLog[4], "State3": rolRat_state,"<Rudder Position>[deg]": self.paramsToLog[5],
                    "State4": rudPos_state, "<Yaw Rate>[deg/s]": self.paramsToLog[6], "State5": yawRat_state})

        if (self.flagValue == 1):
            self.writer.writerow({"<FLAG>": "1", "<Clock>[ms]": self.paramsToLog[0], "<Elevator Position>[deg]": self.paramsToLog[1],
                    "State0": elePos_state, "<Pitch Rate>[deg/s]": self.paramsToLog[2], "State1": pitRat_state,
                    "<Aileron Position>[deg]": self.paramsToLog[3], "State2": ailPos_state,
                    "<Roll Rate>[deg/s]": self.paramsToLog[4], "State3": rolRat_state,"<Rudder Position>[deg]": self.paramsToLog[5],
                    "State4": rudPos_state, "<Yaw Rate>[deg/s]": self.paramsToLog[6], "State5": yawRat_state})


    # ====================================================================================================================== Define Limits()
    def DefineLimits(self):
        self.popup = Tk()
        self.popup.wm_title("Limits")
        label = Label(self.popup, text="No limits set by default on startup!")
        label.grid(row=0, column=0, columnspan=3, sticky=W, padx=5, pady=5)
        label2 = Label(self.popup, text="Enter positive values only, system will account for +/-")
        label2.grid(row=1, column=0, columnspan=3, sticky=W, padx=5, pady=5)


        # --------------------------------------------------------------------------------------------------- Position Limits
        elevatorLimit_label = Label(self.popup, text="Elevator Position: ")
        elevatorLimit_label.grid(row=2, column=0, padx=5, pady=5)
        self.elevatorLimit_entry = Entry(self.popup)
        self.elevatorLimit_entry.grid(row=2, column=1, padx=5, pady=5)

        aileronLimit_label = Label(self.popup, text="Aileron Position: ")
        aileronLimit_label.grid(row=3, column=0, padx=5, pady=5)
        self.aileronLimit_entry = Entry(self.popup)
        self.aileronLimit_entry.grid(row=3, column=1, padx=5, pady=5)

        rudderLimit_label = Label(self.popup, text="Rudder Position: ")
        rudderLimit_label.grid(row=4, column=0, padx=5, pady=5)
        self.rudderLimit_entry = Entry(self.popup)
        self.rudderLimit_entry.grid(row=4, column=1, padx=5, pady=5)


        # --------------------------------------------------------------------------------------------------- Rate Limits
        pitchRateLimit_label = Label(self.popup, text="Pitch Rate: ")
        pitchRateLimit_label.grid(row=2, column=3, padx=5, pady=5)
        self.pitchRateLimit_entry = Entry(self.popup)
        self.pitchRateLimit_entry.grid(row=2, column=4, padx=5, pady=5)

        rollRateLimit_label = Label(self.popup, text="Roll Rate: ")
        rollRateLimit_label.grid(row=3, column=3, padx=5, pady=5)
        self.rollRateLimit_entry = Entry(self.popup)
        self.rollRateLimit_entry.grid(row=3, column=4, padx=5, pady=5)

        yawRateLimit_label = Label(self.popup, text="Yaw Rate: ")
        yawRateLimit_label.grid(row=4, column=3, padx=5, pady=5)
        self.yawRateLimit_entry = Entry(self.popup)
        self.yawRateLimit_entry.grid(row=4, column=4, padx=5, pady=5)

        P1 = Button(self.popup, text="Exit", command=self.popup.destroy, fg="Red")
        P1.grid(row=5, column=4, ipadx=7, padx=5, pady=5, sticky=W)
        P2 = Button(self.popup, text="Set Limits", command=self.MultiFunc_SetAndClose)
        P2.grid(row=5, column=4, ipadx=7, padx=5, pady=5, sticky=E)

        self.popup.mainloop()


    # ====================================================================================================================== MultiFunc Set And Close ()
    def MultiFunc_SetAndClose(self):
        self.SetLimits()
        self.popup.destroy()


    # ====================================================================================================================== Set Limits()
    def SetLimits(self):

        self.elevatorPos_limit = self.elevatorLimit_entry.get()
        self.aileronPos_limit  = self.aileronLimit_entry.get()
        self.rudderPos_limit   = self.rudderLimit_entry.get()

        self.pitchRate_limit = self.pitchRateLimit_entry.get()
        self.rollRate_limit  = self.rollRateLimit_entry.get()
        self.yawRate_limit   = self.yawRateLimit_entry.get()


        # Update limit status indicator
        self.limitsStatusValue.set("Limits: Set")
        # self.CheckLimits_ElevatorPitch()


    # ====================================================================================================================== Check Limits()
    def CheckLimits_ElevatorPitch(self):
        self.elevatorPos = float(self.Surface6)     # Raw elevator position
        self.pitchPos = round(self.pitch_y, 3)      # Pitch rate
        self.aileronPos = float(self.Surface0)
        self.rollPos = round(self.roll_y, 3)
        self.rudderPos = float(self.Surface3)       # Raw rudder position
        self.yawPos = round(self.yaw_y, 3)          # Yaw rate

        # --------------------------------------------------------------------------------------------------- Elevator position Limits
        self.elevatorPos_limit_upper = float(self.elevatorPos_limit)
        self.elevatorPos_limit_lower = (0 - self.elevatorPos_limit_upper)

        # Calculate alert value at 90% of of limit
        self.elevatorPos_alert_upper = (float(self.elevatorPos_limit) * 0.90)
        self.elevatorPos_alert_lower = (0 - self.elevatorPos_alert_upper)

        # Round alert to 3 decimals
        self.elevatorPos_alert_upper = (round(self.elevatorPos_alert_upper, 3))
        self.elevatorPos_alert_lower = (round(self.elevatorPos_alert_lower, 3))

        # --------------------------------------------------------------------------------------------------- Elevator pitch rate limits
        self.pitchRate_limit_upper = float(self.pitchRate_limit)
        self.pitchRate_limit_lower = (0 - self.pitchRate_limit_upper)

        # Calculate alert value at 90% of of limit
        self.pitchRate_alert_upper = (float(self.pitchRate_limit) * 0.90)
        self.pitchRate_alert_lower = (0 - self.pitchRate_alert_upper)

        # Round alert to 3 decimals
        self.pitchRate_alert_upper = (round(self.pitchRate_alert_upper, 3))
        self.pitchRate_alert_lower = (round(self.pitchRate_alert_lower, 3))

        # --------------------------------------------------------------------------------------------------- Aileron pos. limit
        self.aileronPos_limit_upper = float(self.aileronPos_limit)
        self.aileronPos_limit_lower = (0 - self.aileronPos_limit_upper)

        # Calculate alert value at 90% of of limit
        self.aileronPos_alert_upper = (float(self.aileronPos_limit) * 0.90)
        self.aileronPos_alert_lower = (0 - self.aileronPos_alert_upper)

        # Round alert to 3 decimals
        self.aileronPos_alert_upper = (round(self.aileronPos_alert_upper, 3))
        self.aileronPos_alert_lower = (round(self.aileronPos_alert_lower, 3))

        # --------------------------------------------------------------------------------------------------- Aileron roll rate limits
        self.rollRate_limit_upper = float(self.rollRate_limit)
        self.rollRate_limit_lower = (0 - self.rollRate_limit_upper)

        # Calculate alert value at 90% of of limit
        self.rollRate_alert_upper = (float(self.rollRate_limit) * 0.90)
        self.rollRate_alert_lower = (0 - self.rollRate_alert_upper)

        # Round alert to 3 decimals
        self.rollRate_alert_upper = (round(self.rollRate_alert_upper, 3))
        self.rollRate_alert_lower = (round(self.rollRate_alert_lower, 3))

        # --------------------------------------------------------------------------------------------------- Rudder position limits
        self.rudderPos_limit_upper = float(self.rudderPos_limit)
        self.rudderPos_limit_lower = (0 - self.rudderPos_limit_upper)

        # Calculate alert value at 90% of of limit
        self.rudderPos_alert_upper = (float(self.rudderPos_limit) * 0.90)
        self.rudderPos_alert_lower = (0 - self.rudderPos_alert_upper)

        # Round alert to 3 decimals
        self.rudderPos_alert_upper = (round(self.rudderPos_alert_upper, 3))
        self.rudderPos_alert_lower = (round(self.rudderPos_alert_lower, 3))

        # --------------------------------------------------------------------------------------------------- Rudder yaw rate limits
        self.yawRate_limit_upper = float(self.yawRate_limit)
        self.yawRate_limit_lower = (0 - self.yawRate_limit_upper)

        # Calculate alert value at 90% of of limit
        self.yawRate_alert_upper = (float(self.yawRate_limit) * 0.90)
        self.yawRate_alert_lower = (0 - self.yawRate_alert_upper)

        # Round alert to 3 decimals
        self.yawRate_alert_upper = (round(self.yawRate_alert_upper, 3))
        self.yawRate_alert_lower = (round(self.yawRate_alert_lower, 3))

        # --------------------------------------------------------------------------------------------------- Update elevator pos. alarm
        if ((self.elevatorPos) <= (self.elevatorPos_alert_lower)) or ((self.elevatorPos) >= (self.elevatorPos_alert_upper)):
            self.elevator_alarm.configure(bg="Yellow")
            self.elevator_state.set("ALERT")

        if ((self.elevatorPos) <= (self.elevatorPos_limit_lower)) or ((self.elevatorPos) >= (self.elevatorPos_limit_upper)):
            self.elevator_alarm.configure(bg="Red")
            self.elevator_state.set("WARN")

        if ((self.elevatorPos) > (self.elevatorPos_alert_lower)) and ((self.elevatorPos) < (self.elevatorPos_alert_upper)):
            self.elevator_alarm.configure(bg="Lime Green")
            self.elevator_state.set("Okay")

        # --------------------------------------------------------------------------------------------------- Update pitch rate alarm
        if ((self.pitchPos) <= (self.pitchRate_alert_lower)) or ((self.pitchPos) >= (self.pitchRate_alert_upper)):
            self.pitch_alarm.configure(bg="Yellow")
            self.pitch_state.set("ALERT")

        if ((self.pitchPos) <= (self.pitchRate_limit_lower)) or ((self.pitchPos) >= (self.pitchRate_limit_upper)):
            self.pitch_alarm.configure(bg="Red")
            self.pitch_state.set("WARN")

        if ((self.pitchPos) > (self.pitchRate_alert_lower)) and ((self.pitchPos) < (self.pitchRate_alert_upper)):
            self.pitch_alarm.configure(bg="Lime Green")
            self.pitch_state.set("Okay")

        # --------------------------------------------------------------------------------------------------- Update Aileron pos. alarm
        if ((self.aileronPos) <= (self.aileronPos_alert_lower)) or ((self.aileronPos) >= (self.aileronPos_alert_upper)):
            self.aileron_alarm.configure(bg="Yellow")
            self.aileron_state.set("ALERT")

        if ((self.aileronPos) <= (self.aileronPos_limit_lower)) or ((self.aileronPos) >= (self.aileronPos_limit_upper)):
            self.aileron_alarm.configure(bg="Red")
            self.aileron_state.set("WARN")

        if ((self.aileronPos) > (self.aileronPos_alert_lower)) and ((self.aileronPos) < (self.aileronPos_alert_upper)):
            self.aileron_alarm.configure(bg="Lime Green")
            self.aileron_state.set("Okay")

        # --------------------------------------------------------------------------------------------------- Update Aileron roll rate alarm
        if ((self.rollPos) <= (self.rollRate_alert_lower)) or ((self.rollPos) >= (self.rollRate_alert_upper)):
            self.roll_alarm.configure(bg="Yellow")
            self.roll_state.set("ALERT")

        if ((self.rollPos) <= (self.rollRate_limit_lower)) or ((self.rollPos) >= (self.rollRate_limit_upper)):
            self.roll_alarm.configure(bg="Red")
            self.roll_state.set("WARN")

        if ((self.rollPos) > (self.rollRate_alert_lower)) and ((self.rollPos) < (self.rollRate_alert_upper)):
            self.roll_alarm.configure(bg="Lime Green")
            self.roll_state.set("Okay")

        # --------------------------------------------------------------------------------------------------- Update Rudder pos. alarm
        if ((self.rudderPos) <= (self.rudderPos_alert_lower)) or ((self.rudderPos) >= (self.rudderPos_alert_upper)):
            self.rudder_alarm.configure(bg="Yellow")
            self.rudder_state.set("ALERT")

        if ((self.rudderPos) <= (self.rudderPos_limit_lower)) or ((self.rudderPos) >= (self.rudderPos_limit_upper)):
            self.rudder_alarm.configure(bg="Red")
            self.rudder_state.set("WARN")

        if ((self.rudderPos) > (self.rudderPos_alert_lower)) and ((self.rudderPos) < (self.rudderPos_alert_upper)):
            self.rudder_alarm.configure(bg="Lime Green")
            self.rudder_state.set("Okay")

        # --------------------------------------------------------------------------------------------------- Update yaw rate alarm
        if ((self.yawPos) <= (self.yawRate_alert_lower)) or ((self.yawPos) >= (self.yawRate_alert_upper)):
            self.yaw_alarm.configure(bg="Yellow")
            self.yaw_state.set("ALERT")

        if ((self.yawPos) <= (self.yawRate_limit_lower)) or ((self.yawPos) >= (self.yawRate_limit_upper)):
            self.yaw_alarm.configure(bg="Red")
            self.yaw_state.set("WARN")

        if ((self.yawPos) > (self.yawRate_alert_lower)) and ((self.yawPos) < (self.yawRate_alert_upper)):
            self.yaw_alarm.configure(bg="Lime Green")
            self.yaw_state.set("Okay")


    # ====================================================================================================================== Update HUD()
    def UpdateHUD(self, dict):
        # ----------------------------------------------------------- Elevator pos.
        self.Surface6 = float(dict["<Surface6>"])
        self.Surface6 = math.degrees(self.Surface6)
        self.elevator_value.set("{:.3f}".format(self.Surface6))

        # ----------------------------------------------------------- Pitch rate.
        pitch_x = self.Surface6
        self.pitch_y = ((1.4777 * pitch_x) + 7.3747)
        self.pitch_value.set("{:.3f}".format(self.pitch_y))

        # ----------------------------------------------------------- Left aileron pos.
        self.Surface0 = float(dict["<Surface0>"])
        self.Surface0 = math.degrees(self.Surface0)
        self.aileron_value.set("{:.3f}".format(self.Surface0))

        # ----------------------------------------------------------- Roll rate
        roll_x = self.Surface0
        self.roll_y = ((2.0108 * roll_x) - 2.1642)
        self.roll_value.set("{:.3f}".format(self.roll_y))

        # ----------------------------------------------------------- Rudder pos.
        self.Surface3 = float(dict["<Surface3>"])
        self.Surface3 = math.degrees(self.Surface3)
        self.rudder_value.set("{:.3f}".format(self.Surface3))
        self.rudder_state.set("Okay")

        # ----------------------------------------------------------- Yaw rate.
        yaw_x = self.Surface3
        self.yaw_y = ((0.1875 * yaw_x) + 0.5679)
        self.yaw_value.set("{:.3f}".format(self.yaw_y))


        # Check current values against user-defined limits and update display
        self.CheckLimits_ElevatorPitch()
        self.mainframe.update()
        self.paramsToLog = [self.telemetry_data["<Clock>[ms]"], self.Surface6, self.pitch_y, self.Surface0, self.roll_y, self.Surface3, self.yaw_y]

        # Check if user opened a log file. If so, write to log.
        if (self.logCreated == 1):
            print("To Log --> ", self.paramsToLog)
            self.WriteToLog()

        self.elapsedTime = (time.time() - self.startTime)
        self.elapsedTimeValue.set(time.strftime("Elapsed Time: %H:%M:%S", time.gmtime(self.elapsedTime)))

    # ====================================================================================================================== Retrive PCC Log()
    def RetrievePCCLog(self):
        fh = self.fh        # Initialize local file header encase corrupted (allows restart with correct file header)

        # Iterate while incoming data
        while 1:

            # Initialize empty arrays to store values until pushed to dictionary
            tempArr = []
            dataSegment = []
            overFlow = []

            line = fh.readline()

            # If current line is not empty string, split and store in temporary array
            if not len(line.strip()) == 0:
                tempArr = line.split()

                # If temporary array contains less than a full data set, set complete
                # segment to false (PCC records 200 fields per 1 full set. Operating on incomplete
                # set will cause data curruptions and mis-calculations later on).
                if len(tempArr) < 200:
                    completeSegment = 0

                    while not completeSegment:

                        line = fh.readline()        # Read in a new line to complete the segment

                        # If new line is not empty string, split and move to condition
                        if not len(line.strip()) == 0:
                            line = line.split()

                            # Append each element in new line to temporary array
                            for each in line:
                                tempArr.append(each)

                            # If temporary array contains more than one complete set, set complete segment to true
                            # and splice the complete portion into dataSegment array. Move overflowed elements to overFlow array.
                            if len(tempArr) >= 200:
                                completeSegment = 1
                                dataSegment = tempArr[0:200]
                                overFlow = tempArr[201:]

                # If temporary array contains a full data set after first line read, splice one full set into dataSegment array
                # and move overflowed elements to overFlow array
                if len(tempArr) >= 200:
                    dataSegment = tempArr[0:200]
                    overFlow = tempArr[201:]

            else:
                continue

            # Pass complete data segment for use in populating dictionary
            self.PopulateDict(dataSegment)

            # If overFlow is not null and contains a full data set, pass to function for use in populating dictionary
            # if len(overFlow) == 200:
            #     self.PopulateDict(overFlow)


    # ====================================================================================================================== Populate Dict()
    def PopulateDict(self, dataSegment):
        position = 0        # Initialize for index tracking

        # Iterate through each key in dictionary
        for key in self.telemetry_data:

            # If position moved pass index length, break from loop
            if position >= len(dataSegment):
                break

            # If position is valid, copy corresponding dataSegment value to dictionary key and increment position
            else:
                self.telemetry_data[key] = dataSegment[position]
                position += 1

        # Pull values from populated dictionary for quality checking, Keys used are parameters needed for display
        # or special values which will be corrupted by minor character shifts in the dictionary
        try:
            integrity01 = self.telemetry_data['<AP_Global>']
            integrity02 = self.telemetry_data['<NavMode>']
            integrity03 = self.telemetry_data['<AlignSolnType>']
            integrity04 = self.telemetry_data['<Clock>[ms]']
            integrity05 = self.telemetry_data['<Surface3>']
            integrity06 = self.telemetry_data['<Surface6>']
            integrity07 = self.telemetry_data['<Surface0>']

            # If integrity values 1-3 are not alphabetical characters only, integrity check fails. If alphabetical
            # move to integrity values 4-6.
            check01 = integrity01.isalpha()
            check02 = integrity02.isalpha()
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
            print("Integrity Check Failed: truncating entry. --> ", self.telemetry_data['<Clock>[ms]'], self.telemetry_data['<AP_Global>'],
                  self.telemetry_data['<NavMode>'], self.telemetry_data['<AlignSolnType>'], self.telemetry_data['<Surface3>'],
                  self.telemetry_data['<Surface0>'], self.telemetry_data['<Surface6>'], '\n--> currupt entry', self.telemetry_data)

        else:
            # If integrity check passes, push dictionary for values to be used in updating display
            print(self.telemetry_data)
            self.UpdateHUD(self.telemetry_data)


    # ====================================================================================================================== Start Program()
    def StartProgram(self):
        self.getStartTime = datetime.datetime.now()
        self.startTime = time.time()
        self.startTimeValue.set(self.getStartTime.strftime("Start Time: %H:%M:%S"))

        # self.logCreated = 0
        self.runStatusValue.set("Status: Running")
        self.RetrievePCCLog()


# ========================================================================================================================== Main()
root = Tk()
root.title("Raspet Flight Display   v1.0.0")
#                w   h   x  y
root.geometry('1200x500+25+25')
HUD = Interface(root)
root.mainloop()