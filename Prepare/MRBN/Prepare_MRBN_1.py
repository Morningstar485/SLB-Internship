# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MRBN_UIohDDjv.ui'
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
    QGroupBox, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(608, 448)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Radio_Frame_4 = QFrame(self.groupBox_4)
        self.Radio_Frame_4.setObjectName(u"Radio_Frame_4")
        self.Radio_Frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Radio_Frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.radioButton_10 = QRadioButton(self.Radio_Frame_4)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.Radio_Frame_4)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.radioButton_11)


        self.verticalLayout_7.addWidget(self.Radio_Frame_4)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_1 = QCheckBox(self.frame_2)
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


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(570, 130))
        self.label.setMaximumSize(QSize(570, 130))
        self.label.setPixmap(QPixmap(resource_path("Icons/Img_22.png")))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_2 = QCheckBox(self.frame_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.retranslateUi(Dialog)
        self.checkBox_1.hide()
        self.label.hide()
        self.label_2.hide()
        self.checkBox_2.hide()
        self.pushButton.hide()

        self.radioButton_10.toggled.connect(self.checkBox_1.setVisible)
        self.radioButton_11.toggled.connect(self.checkBox_1.setVisible)
        self.checkBox_1.toggled.connect(self.label.setVisible)
        self.checkBox_1.toggled.connect(self.label_2.setVisible)
        self.checkBox_1.toggled.connect(self.checkBox_2.setVisible)
        self.checkBox_2.toggled.connect(self.pushButton.setVisible)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"22-Socket Pin", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"No damage at surface", None))
        self.radioButton_11.setText(QCoreApplication.translate("Dialog", u"Rederessed/Replaced damaged parts", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Drain Plug is installed", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Rest all resistances are &gt; 20M</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"All the resistances are arroding to guide", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

class Prepare_MRBN_1(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # GroupBox 4: 22-Socket Pin
        if self.ui.groupBox_4.isVisible():
            if self.ui.radioButton_10.isChecked():
                self.child_metadata["22-Socket Pin Condition"] = "No damage at surface"
            elif self.ui.radioButton_11.isChecked():
                self.child_metadata["22-Socket Pin Condition"] = "Redressed/Replaced damaged parts"
            else:
                self.child_metadata["22-Socket Pin Condition"] = None
        else:
            self.child_metadata["22-Socket Pin Condition"] = None

        # Drain Plug installed
        self.child_metadata["Drain Plug Installed"] = self.ui.checkBox_1.isVisible() and self.ui.checkBox_1.isChecked()

        # Rest all resistances > 20M (label shown if checkBox_1 is checked)
        self.child_metadata["Rest Resistances > 20M"] = self.ui.label.isVisible()

        # All resistances according to guide
        self.child_metadata["All Resistances According to Guide"] = self.ui.checkBox_2.isVisible() and self.ui.checkBox_2.isChecked()

        self.accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())