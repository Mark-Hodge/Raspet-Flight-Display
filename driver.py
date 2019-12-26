
from PCCLogHandler import *
from mainInterface import *
from limitsdialog import Ui_Dialog as Form


def openPCCTelemetryFile(self):
    try:
        self.PCCTelemetryFile = QFileDialog.getOpenFileName()
        self.label_toolBar_PCCFile.setText("PCC Telemetry File: " + self.PCCTelemetryFile[0])
        print(str(self.PCCTelemetryFile))
        print(type(self.PCCTelemetryFile))
        print(type(self.PCCTelemetryFile[0]))

    except Exception as ex:
        print("Could not open Telemetry File (check file type and try again).", ex)

def openLimitsDialog(self):
    Dialog = QtWidgets.QDialog()
    ui = Form()
    ui.setupUi(Dialog)
    Dialog.exec()
    # sys.exit(app.exec_())


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())