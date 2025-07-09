from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(314, 496)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_1 = QGroupBox(Dialog)
        self.groupBox_1.setObjectName(u"groupBox_1")
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


        self.verticalLayout_11.addWidget(self.Radio_Frame_1)


        self.verticalLayout_3.addWidget(self.groupBox_1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.comboBox)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(31, 31))
        self.label_6.setMaximumSize(QSize(31, 31))
        self.label_6.setPixmap(QPixmap(resource_path("Icons/Info.png")))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Radio_Frame_3 = QFrame(self.groupBox_2)
        self.Radio_Frame_3.setObjectName(u"Radio_Frame_3")
        self.Radio_Frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Radio_Frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_5 = QRadioButton(self.Radio_Frame_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.Radio_Frame_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_6)


        self.verticalLayout_15.addWidget(self.Radio_Frame_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.retranslateUi(Dialog)

        self.comboBox.hide()
        self.frame_4.hide()
        self.groupBox_2.hide()
        self.pushButton.hide()

        self.radioButton_1.toggled.connect(lambda: self.comboBox.setVisible(self.radioButton_1.isChecked()))
        self.radioButton_2.toggled.connect(lambda: self.comboBox.setVisible(self.radioButton_2.isChecked()))
        self.radioButton_5.toggled.connect(lambda: self.pushButton.setVisible(self.radioButton_5.isChecked()))
        self.radioButton_6.toggled.connect(lambda: self.pushButton.setVisible(self.radioButton_6.isChecked()))

        self.comboBox.currentIndexChanged.connect(self.update_groupbox_and_frame)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def update_groupbox_and_frame(self):
        idx = self.comboBox.currentIndex()
        # Show groupBox_2 for any selection except default (index 0)
        self.groupBox_2.setVisible(idx != 0)
        # Show frame_4 only if XXP (index 4) is selected
        self.frame_4.setVisible(idx == 4)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Select MRPO Purpose", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Sample Side", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Gaurd Side", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select DU", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"STD", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"HP", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"XP", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"XXP", None))

        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Note</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Please check the XXP stabber : MRDU-XX </span></p><p><span style=\" font-size:11pt;\">Stabber (100275502) and O-rings </span></p><p><span style=\" font-size:11pt;\">(B013113 (SP3) ,100739726 (XP3)) are </span></p><p><span style=\" font-size:11pt;\">different compared to all other 3 MRDU's</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Select Mode", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"UP/DOWN", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"IN/OUT", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

from .Prepare_MRPO_2_IO import Prepare_MRPO_2_IO
from .Prepare_MRPO_2_UD import Prepare_MRPO_2_UD

class Prepare_MRPO_1(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # MRPO Purpose
        if self.ui.radioButton_1.isChecked():
            self.child_metadata['MRPO Purpose'] = 'Sample Side'
        elif self.ui.radioButton_2.isChecked():
            self.child_metadata['MRPO Purpose'] = 'Gaurd Side'
        else:
            self.child_metadata['MRPO Purpose'] = None
        # MRPO DU
        du_idx = self.ui.comboBox.currentIndex()
        
        if du_idx > 0:
            self.child_metadata['MRPO DU'] = self.ui.comboBox.currentText()
        else:
            self.child_metadata['MRPO DU'] = None
        # MRPO Mode
        if self.ui.radioButton_5.isChecked():
            self.child_metadata['MRPO Mode'] = 'UP/DOWN'
        elif self.ui.radioButton_6.isChecked():
            self.child_metadata['MRPO Mode'] = 'IN/OUT'
        else:
            self.child_metadata['MRPO Mode'] = None

        # Open the appropriate dialog based on the selected radio button
        if self.ui.radioButton_5.isChecked():
            dialog = Prepare_MRPO_2_UD(self.child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                self.accept()  # ✅ Close this dialog and continue chain
        elif self.ui.radioButton_6.isChecked():
            dialog = Prepare_MRPO_2_IO(self.child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                self.accept()  # ✅ Close this dialog and continue chain

