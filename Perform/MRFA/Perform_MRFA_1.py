# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MRFA_UI_1tuJcVG.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(818, 540)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_1 = QGroupBox(self.frame)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(260, 0))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.radioButton_1 = QRadioButton(self.groupBox_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.groupBox_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.radioButton_2)


        self.horizontalLayout.addWidget(self.groupBox_1)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_2 = QGroupBox(self.frame_12)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(260, 0))
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_4)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.frame_6 = QFrame(self.frame_12)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(41, 41))
        self.label_12.setMaximumSize(QSize(41, 41))
        self.label_12.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(260, 0))
        self.groupBox_3.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_5 = QRadioButton(self.groupBox_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_6)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_9.addWidget(self.label_17)


        self.horizontalLayout_3.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(260, 0))
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_7 = QRadioButton(self.groupBox_4)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.groupBox_4)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_8)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(260, 0))
        self.groupBox_5.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.radioButton_9 = QRadioButton(self.groupBox_5)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.groupBox_5)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.radioButton_10)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.frame_13 = QFrame(self.frame_2)
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


        self.horizontalLayout_2.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_6 = QGroupBox(self.frame_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(275, 0))
        self.groupBox_6.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setChecked(False)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_11 = QRadioButton(self.groupBox_6)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.groupBox_6)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_12)


        self.horizontalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.frame_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(260, 0))
        self.groupBox_7.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.radioButton_13 = QRadioButton(self.groupBox_7)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_17.addWidget(self.radioButton_13)

        self.radioButton_14 = QRadioButton(self.groupBox_7)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_17.addWidget(self.radioButton_14)


        self.horizontalLayout_4.addWidget(self.groupBox_7)

        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(41, 41))
        self.label_18.setMaximumSize(QSize(41, 41))
        self.label_18.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)


        self.horizontalLayout_4.addWidget(self.frame_15)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_8 = QGroupBox(self.frame_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(295, 0))
        self.groupBox_8.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_8.setCheckable(False)
        self.groupBox_8.setChecked(False)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.radioButton_15 = QRadioButton(self.groupBox_8)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_18.addWidget(self.radioButton_15)

        self.radioButton_16 = QRadioButton(self.groupBox_8)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_18.addWidget(self.radioButton_16)


        self.horizontalLayout_5.addWidget(self.groupBox_8)

        self.frame_16 = QFrame(self.frame_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(41, 41))
        self.label_20.setMaximumSize(QSize(41, 41))
        self.label_20.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_11.addWidget(self.label_21)


        self.horizontalLayout_5.addWidget(self.frame_16)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_28 = QFrame(Dialog)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_28)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_28)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_28)


        self.retranslateUi(Dialog)

        self.frame_6.hide()
        self.frame_14.hide()
        self.frame_13.hide()
        self.frame_15.hide()
        self.frame_16.hide()
        self.pushButton.hide()
        self.groupBox_2.hide()
        self.groupBox_3.hide()
        self.groupBox_4.hide()
        self.groupBox_5.hide()
        self.groupBox_6.hide()
        self.groupBox_7.hide()
        self.groupBox_8.hide()

        self.radioButton_1.toggled.connect(lambda checked: self.groupBox_2.setVisible(checked))
        self.radioButton_2.toggled.connect(lambda checked: self.frame_6.setVisible(checked))
        self.radioButton_3.toggled.connect(lambda checked: self.groupBox_3.setVisible(checked))
        self.radioButton_4.toggled.connect(lambda checked: self.frame_6.setVisible(checked))
        self.radioButton_5.toggled.connect(lambda checked: self.groupBox_4.setVisible(checked))
        self.radioButton_6.toggled.connect(lambda checked: self.frame_14.setVisible(checked))
        self.radioButton_7.toggled.connect(lambda checked: self.groupBox_6.setVisible(checked))
        self.radioButton_8.toggled.connect(lambda checked: self.groupBox_5.setVisible(checked))
        self.radioButton_9.toggled.connect(lambda checked: self.groupBox_6.setVisible(checked))
        self.radioButton_10.toggled.connect(lambda checked: self.frame_13.setVisible(checked))
        self.radioButton_11.toggled.connect(lambda checked: self.groupBox_8.setVisible(checked))
        self.radioButton_12.toggled.connect(lambda checked: self.groupBox_7.setVisible(checked))
        self.radioButton_13.toggled.connect(lambda checked: self.groupBox_8.setVisible(checked))
        self.radioButton_14.toggled.connect(lambda checked: self.frame_15.setVisible(checked))
        self.radioButton_15.toggled.connect(lambda checked: self.pushButton.setVisible(checked))
        self.radioButton_16.toggled.connect(lambda checked: self.frame_16.setVisible(checked))
        


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Are all the FASW Data Channels Green?", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Are all the FAAS Data Channels Green?", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Contact IE</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Are all the RSPC Data Channels Green?", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Contact IE</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"ACOM Pass?", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_8.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Redo ACOM Pass?", None))
        self.radioButton_9.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Please Contact IE</span></p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"FAMO Data channel value changing while ACOM?", None))
        self.radioButton_11.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_12.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Is it changing after Redo?", None))
        self.radioButton_13.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_14.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Please Contact IE</span></p></body></html>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dialog", u"Are all RSPC channels are between 1.35 V and 3.2 V?", None))
        self.radioButton_15.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_16.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Contact IE</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

class Perform_MRFA_1(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # Collect all relevant user input directly into child_metadata (flat dict, like MRMS)
        ui = self.ui
        if self.child_metadata is None:
            self.child_metadata = {}
        self.child_metadata['fasw_green'] = "yes" if ui.radioButton_1.isChecked() else "no" if ui.radioButton_2.isChecked() else ""
        self.child_metadata['faas_green'] = "yes" if ui.radioButton_3.isChecked() else "no" if ui.radioButton_4.isChecked() else ""
        self.child_metadata['rspc_green'] = "yes" if ui.radioButton_5.isChecked() else "no" if ui.radioButton_6.isChecked() else ""
        self.child_metadata['acom_pass'] = "yes" if ui.radioButton_7.isChecked() else "no" if ui.radioButton_8.isChecked() else ""
        self.child_metadata['redo_acom_pass'] = "yes" if ui.radioButton_9.isChecked() else "no" if ui.radioButton_10.isChecked() else ""
        self.child_metadata['famo_changing_acom'] = "yes" if ui.radioButton_11.isChecked() else "no" if ui.radioButton_12.isChecked() else ""
        self.child_metadata['changing_after_redo'] = "yes" if ui.radioButton_13.isChecked() else "no" if ui.radioButton_14.isChecked() else ""
        self.child_metadata['rspc_between_1_35_3_2'] = "yes" if ui.radioButton_15.isChecked() else "no" if ui.radioButton_16.isChecked() else ""
        self.accept()
