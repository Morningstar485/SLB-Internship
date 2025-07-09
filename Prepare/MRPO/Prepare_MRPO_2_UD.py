# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MRPO_UI_UD_1EzFLIA.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(530, 190)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_1 = QCheckBox(Dialog)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_6)


        self.retranslateUi(Dialog)

        self.checkBox_2.hide()
        self.checkBox_3.hide()
        self.pushButton_2.hide()

        self.checkBox_1.toggled.connect(lambda: self.checkBox_2.setVisible(self.checkBox_1.isChecked()))
        self.checkBox_2.toggled.connect(lambda: self.checkBox_3.setVisible(self.checkBox_2.isChecked()))
        self.checkBox_3.toggled.connect(lambda: self.pushButton_2.setVisible(self.checkBox_3.isChecked()))

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Set the MRPO to run in the Up/Down mode", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Confirm the drain plug (H217193) with O-ring (B013118) is installed", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Verify that the manual 3-way flowline valve is set for Up/Down operations", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Check Configuration from InTouch", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

from .Prepare_MRPO_3 import Prepare_MRPO_3 

class Prepare_MRPO_2_UD(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.next_step)
        self.ui.pushButton.clicked.connect(self.open_link)

    def next_step(self):
        # Collect user input into child_metadata
        if self.child_metadata is not None:
            self.child_metadata['Set MRPO to Up/Down mode'] = self.ui.checkBox_1.isChecked()
            self.child_metadata['Drain plug (H217193) with O-ring (B013118) installed'] = self.ui.checkBox_2.isChecked()
            self.child_metadata['Manual 3-way flowline valve set for Up/Down'] = self.ui.checkBox_3.isChecked()

        dialog = Prepare_MRPO_3(self.child_metadata, self.admin_metadata)
        if dialog.exec() == QDialog.Accepted:
                self.accept()  # ✅ Close this dialog and continue chain

    def open_link(self):
        QDesktopServices.openUrl(QUrl("https://intouchsupport.com/index.cfm?event=content.preview&contentId=7033048&FromRefPage=Y"))
