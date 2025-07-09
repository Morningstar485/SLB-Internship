# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MRMS_UI_2bKNxkH.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(674, 654)
        self.verticalLayout_6 = QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(Dialog)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.radioButton_1 = QRadioButton(self.frame)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.radioButton_2)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(41, 41))
        self.label_14.setMaximumSize(QSize(41, 41))
        self.label_14.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_1 = QCheckBox(self.frame_5)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_1)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_6 = QGroupBox(self.frame_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Radio_Frame_6 = QFrame(self.groupBox_6)
        self.Radio_Frame_6.setObjectName(u"Radio_Frame_6")
        self.Radio_Frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Radio_Frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_3 = QRadioButton(self.Radio_Frame_6)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.Radio_Frame_6)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_4)


        self.verticalLayout_11.addWidget(self.Radio_Frame_6)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.checkBox_2 = QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout.addWidget(self.checkBox_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_7 = QGroupBox(self.frame_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(280, 0))
        self.groupBox_7.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Radio_Frame_7 = QFrame(self.groupBox_7)
        self.Radio_Frame_7.setObjectName(u"Radio_Frame_7")
        self.Radio_Frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Radio_Frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_5 = QRadioButton(self.Radio_Frame_7)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.Radio_Frame_7)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_6)


        self.verticalLayout_13.addWidget(self.Radio_Frame_7)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_3 = QCheckBox(self.frame_6)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame_6)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_4)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_9 = QFrame(Dialog)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(510, 220))
        self.label_2.setMaximumSize(QSize(510, 220))
        self.label_2.setPixmap(QPixmap(resource_path("Icons/Img_19.png")))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.frame_3 = QFrame(self.frame_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frame_9)


        self.retranslateUi(Dialog)

        self.pushButton.hide()
        self.groupBox_6.hide()
        self.groupBox_7.hide()
        self.frame_13.hide()
        self.label_2.hide()
        self.frame_5.hide()
        self.checkBox_2.hide()
        self.checkBox_3.hide()
        self.checkBox_4.hide()

        self.radioButton_1.toggled.connect(self.frame_13.setVisible)
        self.radioButton_1.toggled.connect(self.frame_5.setVisible)
        self.radioButton_2.toggled.connect(self.groupBox_6.setVisible)
        self.radioButton_3.toggled.connect(self.checkBox_2.setVisible)
        self.radioButton_4.toggled.connect(self.groupBox_7.setVisible)
        self.radioButton_4.toggled.connect(self.label_2.setVisible)
        self.radioButton_5.toggled.connect(self.checkBox_3.setVisible)
        self.radioButton_6.toggled.connect(self.checkBox_4.setVisible)
        self.checkBox_1.toggled.connect(self.groupBox_6.setVisible)
        self.checkBox_2.toggled.connect(self.groupBox_7.setVisible)
        self.checkBox_2.toggled.connect(self.label_2.setVisible)
        self.checkBox_3.toggled.connect(self.pushButton.setVisible)
        self.checkBox_4.toggled.connect(self.pushButton.setVisible)
        self.checkBox_1.toggled.connect(self.groupBox_6.setVisible)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Sampling Type</span></p></body></html>", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Revesre Shock Mode", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Low Shock Mode", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Please get in touch with </span></p><p><span style=\" font-size:16pt; font-style:italic;\">PSD/JDL for tools preparation</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"MRMS is located above MRPO", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"The relief valve plug (H730586) is \n"
"installed in the lower waterline port", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Upper waterline port is used as an exit port only", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Mud check valve (H730507) is installed", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"The relief valve plug (H730586) isinstalled", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

from .Prepare_MRMS_3 import Prepare_MRMS_3

class Prepare_MRMS_2(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # Sampling Type
        if self.ui.radioButton_1.isChecked():
            self.child_metadata["Sampling Type"] = "Reverse Shock Mode"
        elif self.ui.radioButton_2.isChecked():
            self.child_metadata["Sampling Type"] = "Low Shock Mode"
        else:
            self.child_metadata["Sampling Type"] = None

        # Done checkbox for Sampling Type
        self.child_metadata["Sampling Type Check Done"] = self.ui.checkBox_1.isVisible() and self.ui.checkBox_1.isChecked()

        # MRMS is located above MRPO
        if self.ui.groupBox_6.isVisible():
            if self.ui.radioButton_3.isChecked():
                self.child_metadata["MRMS Above MRPO"] = "Yes"
            elif self.ui.radioButton_4.isChecked():
                self.child_metadata["MRMS Above MRPO"] = "No"
            else:
                self.child_metadata["MRMS Above MRPO"] = None
        else:
            self.child_metadata["MRMS Above MRPO"] = None

        # The relief valve plug (H730586) is installed in the lower waterline port
        self.child_metadata["Relief Valve Plug Installed (Lower Waterline)"] = self.ui.checkBox_2.isVisible() and self.ui.checkBox_2.isChecked()

        # Upper waterline port is used as an exit port only
        if self.ui.groupBox_7.isVisible():
            if self.ui.radioButton_5.isChecked():
                self.child_metadata["Upper Waterline Port Exit Only"] = "Yes"
            elif self.ui.radioButton_6.isChecked():
                self.child_metadata["Upper Waterline Port Exit Only"] = "No"
            else:
                self.child_metadata["Upper Waterline Port Exit Only"] = None
        else:
            self.child_metadata["Upper Waterline Port Exit Only"] = None

        # Mud check valve (H730507) is installed
        self.child_metadata["Mud Check Valve Installed"] = self.ui.checkBox_3.isVisible() and self.ui.checkBox_3.isChecked()

        # The relief valve plug (H730586) is installed (again, for upper port)
        self.child_metadata["Relief Valve Plug Installed (Upper Port)"] = self.ui.checkBox_4.isVisible() and self.ui.checkBox_4.isChecked()

        dialog3 = Prepare_MRMS_3(self.child_metadata, self.admin_metadata)
        if dialog3.exec() == QDialog.Accepted:
            self.accept()  # ✅ Close this dialog and continue chain

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())