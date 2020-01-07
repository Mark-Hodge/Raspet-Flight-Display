# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'limitsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from limitsDialogHandler import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 194)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_limitsDialog_header = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_limitsDialog_header.setFont(font)
        self.label_limitsDialog_header.setObjectName("label_limitsDialog_header")
        self.verticalLayout_5.addWidget(self.label_limitsDialog_header)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_elevatorPosition = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_elevatorPosition.sizePolicy().hasHeightForWidth())
        self.label_elevatorPosition.setSizePolicy(sizePolicy)
        self.label_elevatorPosition.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_elevatorPosition.setFont(font)
        self.label_elevatorPosition.setObjectName("label_elevatorPosition")
        self.verticalLayout_2.addWidget(self.label_elevatorPosition)
        self.label_aileronPosition = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_aileronPosition.sizePolicy().hasHeightForWidth())
        self.label_aileronPosition.setSizePolicy(sizePolicy)
        self.label_aileronPosition.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_aileronPosition.setFont(font)
        self.label_aileronPosition.setObjectName("label_aileronPosition")
        self.verticalLayout_2.addWidget(self.label_aileronPosition)
        self.label_rudderPosition = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rudderPosition.sizePolicy().hasHeightForWidth())
        self.label_rudderPosition.setSizePolicy(sizePolicy)
        self.label_rudderPosition.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_rudderPosition.setFont(font)
        self.label_rudderPosition.setObjectName("label_rudderPosition")
        self.verticalLayout_2.addWidget(self.label_rudderPosition)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.doubleSpinBox_elevatorPosition = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_elevatorPosition.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_elevatorPosition.setSizePolicy(sizePolicy)
        self.doubleSpinBox_elevatorPosition.setMinimumSize(QtCore.QSize(60, 0))
        self.doubleSpinBox_elevatorPosition.setObjectName("doubleSpinBox_elevatorPosition")
        self.verticalLayout.addWidget(self.doubleSpinBox_elevatorPosition)
        self.doubleSpinBox_aileronPosition = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_aileronPosition.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_aileronPosition.setSizePolicy(sizePolicy)
        self.doubleSpinBox_aileronPosition.setMinimumSize(QtCore.QSize(60, 0))
        self.doubleSpinBox_aileronPosition.setObjectName("doubleSpinBox_aileronPosition")
        self.verticalLayout.addWidget(self.doubleSpinBox_aileronPosition)
        self.doubleSpinBox_rudderPosition = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_rudderPosition.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_rudderPosition.setSizePolicy(sizePolicy)
        self.doubleSpinBox_rudderPosition.setMinimumSize(QtCore.QSize(60, 0))
        self.doubleSpinBox_rudderPosition.setObjectName("doubleSpinBox_rudderPosition")
        self.verticalLayout.addWidget(self.doubleSpinBox_rudderPosition)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_pitchRate = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pitchRate.sizePolicy().hasHeightForWidth())
        self.label_pitchRate.setSizePolicy(sizePolicy)
        self.label_pitchRate.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_pitchRate.setFont(font)
        self.label_pitchRate.setObjectName("label_pitchRate")
        self.verticalLayout_4.addWidget(self.label_pitchRate)
        self.label_rollRate = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rollRate.sizePolicy().hasHeightForWidth())
        self.label_rollRate.setSizePolicy(sizePolicy)
        self.label_rollRate.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_rollRate.setFont(font)
        self.label_rollRate.setObjectName("label_rollRate")
        self.verticalLayout_4.addWidget(self.label_rollRate)
        self.label_yawRate = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_yawRate.sizePolicy().hasHeightForWidth())
        self.label_yawRate.setSizePolicy(sizePolicy)
        self.label_yawRate.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_yawRate.setFont(font)
        self.label_yawRate.setObjectName("label_yawRate")
        self.verticalLayout_4.addWidget(self.label_yawRate)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.doubleSpinBox_pitchRate = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_pitchRate.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_pitchRate.setSizePolicy(sizePolicy)
        self.doubleSpinBox_pitchRate.setMinimumSize(QtCore.QSize(60, 0))
        self.doubleSpinBox_pitchRate.setObjectName("doubleSpinBox_pitchRate")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_pitchRate)
        self.doubleSpinBox_rollRate = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_rollRate.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_rollRate.setSizePolicy(sizePolicy)
        self.doubleSpinBox_rollRate.setMinimumSize(QtCore.QSize(60, 0))
        self.doubleSpinBox_rollRate.setObjectName("doubleSpinBox_rollRate")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_rollRate)
        self.doubleSpinBox_yawRate = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_yawRate.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_yawRate.setSizePolicy(sizePolicy)
        self.doubleSpinBox_yawRate.setMinimumSize(QtCore.QSize(60, 0))
        self.doubleSpinBox_yawRate.setObjectName("doubleSpinBox_yawRate")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_yawRate)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.connector_buttonBoxAccept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Limits"))
        self.label_limitsDialog_header.setText(_translate("Dialog", "Enter limits as positive values. System will account for change (+/-)."))
        self.label_elevatorPosition.setText(_translate("Dialog", "Elevator Position:"))
        self.label_aileronPosition.setText(_translate("Dialog", "Aileron Position:"))
        self.label_rudderPosition.setText(_translate("Dialog", "Rudder Position:"))
        self.label_pitchRate.setText(_translate("Dialog", "Pitch Rate:"))
        self.label_rollRate.setText(_translate("Dialog", "Roll Rate:"))
        self.label_yawRate.setText(_translate("Dialog", "Yaw Rate:"))

    def connector_buttonBoxAccept(self):
        limitsDialogHandler(self)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
