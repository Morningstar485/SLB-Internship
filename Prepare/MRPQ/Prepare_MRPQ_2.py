# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MRPQ_UI_2cfsvHd.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(796, 568)
        self.verticalLayout_10 = QVBoxLayout(Dialog)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(41, 41))
        self.label_4.setMaximumSize(QSize(41, 41))
        self.label_4.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_6)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_4 = QCheckBox(self.frame_2)
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


        self.verticalLayout_2.addWidget(self.frame_2)

        self.groupBox_1 = QGroupBox(self.frame)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(280, 0))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Radio_Frame_1 = QFrame(self.groupBox_1)
        self.Radio_Frame_1.setObjectName(u"Radio_Frame_1")
        self.Radio_Frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Radio_Frame_1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_1 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_3)


        self.verticalLayout_11.addWidget(self.Radio_Frame_1)


        self.verticalLayout_2.addWidget(self.groupBox_1)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_3 = QCheckBox(self.frame_7)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_3)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(330, 190))
        self.label_2.setMaximumSize(QSize(330, 190))
        self.label_2.setPixmap(QPixmap(resource_path("Icons/Img_21.png")))
        self.label_2.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_7)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_11 = QFrame(Dialog)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_11)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 25))
        self.comboBox.setMaximumSize(QSize(100, 25))

        self.verticalLayout_4.addWidget(self.comboBox)

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

        self.verticalLayout_4.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_2)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.groupBox_2 = QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(280, 0))
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Radio_Frame_2 = QFrame(self.groupBox_2)
        self.Radio_Frame_2.setObjectName(u"Radio_Frame_2")
        self.Radio_Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Radio_Frame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.radioButton_4 = QRadioButton(self.Radio_Frame_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.Radio_Frame_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.Radio_Frame_2)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.Radio_Frame_2)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_7)


        self.verticalLayout_13.addWidget(self.Radio_Frame_2)


        self.verticalLayout_7.addWidget(self.groupBox_2)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.frame_10)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Radio_Frame_3 = QFrame(self.groupBox_3)
        self.Radio_Frame_3.setObjectName(u"Radio_Frame_3")
        self.Radio_Frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Radio_Frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_8 = QRadioButton(self.Radio_Frame_3)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.Radio_Frame_3)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_9)


        self.verticalLayout_15.addWidget(self.Radio_Frame_3)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(41, 41))
        self.label_12.setMaximumSize(QSize(41, 41))
        self.label_12.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_9.addWidget(self.frame_9)


        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.frame_11)


        self.retranslateUi(Dialog)

        self.groupBox_1.hide()
        self.checkBox_1.hide()
        self.comboBox.hide()
        self.checkBox_2.hide()
        self.groupBox_2.hide()
        self.groupBox_3.hide()
        self.frame_7.hide()
        self.frame_12.hide()
        self.pushButton.hide()

        self.checkBox_4.toggled.connect(lambda: self.groupBox_1.setVisible(self.checkBox_4.isChecked()))
        self.radioButton_1.toggled.connect(lambda: self.comboBox.setVisible(self.radioButton_1.isChecked()))
        self.radioButton_2.toggled.connect(lambda: self.comboBox.setVisible(self.radioButton_2.isChecked()))
        self.radioButton_3.toggled.connect(lambda: self.comboBox.setVisible(self.radioButton_3.isChecked()))
        self.radioButton_4.toggled.connect(lambda: self.frame_7.setVisible(self.radioButton_4.isChecked()))
        self.radioButton_5.toggled.connect(lambda: self.frame_7.setVisible(self.radioButton_5.isChecked()))
        self.radioButton_6.toggled.connect(lambda: self.frame_7.setVisible(self.radioButton_6.isChecked()))
        self.radioButton_7.toggled.connect(lambda: self.frame_7.setVisible(self.radioButton_7.isChecked()))
        self.checkBox_3.toggled.connect(lambda: self.groupBox_3.setVisible(self.checkBox_3.isChecked()))
        self.radioButton_8.toggled.connect(lambda: self.pushButton.setVisible(self.radioButton_8.isChecked()))
        self.radioButton_9.toggled.connect(lambda: self.frame_12.setVisible(self.radioButton_9.isChecked()))
        self.comboBox.currentIndexChanged.connect(self.update_checkbox_1_text)
      
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def update_checkbox_1_text(self):
        idx = self.comboBox.currentIndex()
        # Hide both by default
        self.checkBox_1.hide()
        self.checkBox_2.hide()
        if idx == 1 or idx == 2 or idx == 4:  # MPMP, MPEP, MRSD
            self.checkBox_1.show()
            self.checkBox_2.hide()
            self.checkBox_1.toggled.connect(lambda: self.groupBox_2.setVisible(self.checkBox_1.isChecked()))
            if idx == 1 or idx == 2:
                self.checkBox_1.setText("Check the packer according to the hole size")
            elif idx == 4:
                self.checkBox_1.setText("Please remove guard flowline socket and joint")
        elif idx == 3:  # MRLD
            self.checkBox_1.show()
            self.checkBox_1.setText("Please remove guard flowline socket and joint")
            self.checkBox_1.toggled.connect(lambda: self.checkBox_2.setVisible(self.checkBox_1.isChecked()))
            self.checkBox_2.toggled.connect(lambda: self.groupBox_2.setVisible(self.checkBox_2.isChecked()))
        else:
            self.checkBox_1.hide()
            self.checkBox_2.hide()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Check that sensor ports match the program</span></p></body></html>", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Warning</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Resistivity cell must always be installed in the Sensor Port 1</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Which cell is put in Sensor Port 2", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Dummy", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"DV Rod", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"H2S Coupon", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Check ISO valve, Bypass valve Screw Out till the truarc ring from Hydraulic side", None))
        self.label_2.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Probe", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"MPMP", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"MPEP", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"MRLD", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"MRSD", None))

        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Please remove guard flowline socket and joint", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Install 100238610 Plug for MRPQ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Installing Anchoring Piston According to Size", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"17.5 In - MRSL", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"12.25 In - MRLH", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"8.5 In - STD Piston (SRTP)", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"6 In - STD Piston (SRTP) with inner piston locked with B030664 Retaining ring", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"MRPQ probe jig available in RB?", None))
        self.radioButton_8.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_9.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Can't check SG Pressure without jig </span></p><p><span style=\" font-size:16pt; font-style:italic;\">and sync pumping. Inform Base</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi


class Prepare_MRPQ_2(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # Collect metadata from UI, using label text as keys, directly into self.child_metadata
        ui = self.ui
        if self.child_metadata is None:
            self.child_metadata = {}
        self.child_metadata['Sensor Port 2'] = ui.comboBox.currentText()
        if ui.checkBox_1.isVisible():
            self.child_metadata[ui.checkBox_1.text()] = ui.checkBox_1.isChecked()
        if ui.checkBox_2.isVisible():
            self.child_metadata[ui.checkBox_2.text()] = ui.checkBox_2.isChecked()
        if ui.checkBox_3.isVisible():
            self.child_metadata[ui.checkBox_3.text()] = ui.checkBox_3.isChecked()
        if ui.checkBox_4.isVisible():
            self.child_metadata[ui.checkBox_4.text()] = ui.checkBox_4.isChecked()
        # Radio buttons in groupBox_1
        if ui.radioButton_1.isVisible():
            self.child_metadata[ui.radioButton_1.text()] = ui.radioButton_1.isChecked()
        if ui.radioButton_2.isVisible():
            self.child_metadata[ui.radioButton_2.text()] = ui.radioButton_2.isChecked()
        if ui.radioButton_3.isVisible():
            self.child_metadata[ui.radioButton_3.text()] = ui.radioButton_3.isChecked()
        # Radio buttons in groupBox_2
        if ui.radioButton_4.isVisible():
            self.child_metadata[ui.radioButton_4.text()] = ui.radioButton_4.isChecked()
        if ui.radioButton_5.isVisible():
            self.child_metadata[ui.radioButton_5.text()] = ui.radioButton_5.isChecked()
        if ui.radioButton_6.isVisible():
            self.child_metadata[ui.radioButton_6.text()] = ui.radioButton_6.isChecked()
        if ui.radioButton_7.isVisible():
            self.child_metadata[ui.radioButton_7.text()] = ui.radioButton_7.isChecked()
        # Radio buttons in groupBox_3
        if ui.radioButton_8.isVisible():
            self.child_metadata[ui.radioButton_8.text()] = ui.radioButton_8.isChecked()
        if ui.radioButton_9.isVisible():
            self.child_metadata[ui.radioButton_9.text()] = ui.radioButton_9.isChecked()
        self.accept()  # ✅ Close this dialog and continue chain

