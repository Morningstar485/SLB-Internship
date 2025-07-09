from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(637, 525)
        self.verticalLayout_5 = QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(41, 41))
        self.label_9.setMaximumSize(QSize(41, 41))
        self.label_9.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_1 = QLabel(self.frame_8)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_2.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.frame_8)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(75, 25))
        self.lineEdit_1.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_1)


        self.horizontalLayout.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(75, 25))
        self.lineEdit_2.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.horizontalLayout.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(75, 25))
        self.lineEdit_3.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_5.addWidget(self.lineEdit_3)


        self.horizontalLayout.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit_4 = QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(75, 25))
        self.lineEdit_4.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_6.addWidget(self.lineEdit_4)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.frame_12)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(75, 25))
        self.lineEdit_5.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_7.addWidget(self.lineEdit_5)


        self.horizontalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.frame_13)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(75, 25))
        self.lineEdit_6.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_8.addWidget(self.lineEdit_6)


        self.horizontalLayout_4.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.frame_3)

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

        self.verticalLayout_5.addWidget(self.checkBox_1)

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

        self.verticalLayout_5.addWidget(self.checkBox_2)

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

        self.verticalLayout_5.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(Dialog)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_7)

        self.frame_28 = QFrame(Dialog)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_28)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_28)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.frame_28)


        self.retranslateUi(Dialog)

        self.frame_3.hide()
        self.checkBox_1.hide()
        self.checkBox_2.hide()
        self.checkBox_3.hide()
        self.checkBox_4.hide()
        self.checkBox_5.hide()
        self.checkBox_6.hide()
        self.checkBox_7.hide()
        self.pushButton.hide()

        # Show frame_3 only when all three line edits in frame_2 are filled with numbers
        def frame2_filled():
            try:
                float(self.lineEdit_1.text())
                float(self.lineEdit_2.text())
                float(self.lineEdit_3.text())
                return True
            except ValueError:
                return False

        # Show checkBox_1 only when all three line edits in frame_3 are filled with numbers
        def frame3_filled():
            try:
                float(self.lineEdit_4.text())
                float(self.lineEdit_5.text())
                float(self.lineEdit_6.text())
                return True
            except ValueError:
                return False

        def update_sequence_visibility():
            self.frame_3.setVisible(frame2_filled())
            self.checkBox_1.setVisible(frame3_filled())

        self.lineEdit_1.textChanged.connect(update_sequence_visibility)
        self.lineEdit_2.textChanged.connect(update_sequence_visibility)
        self.lineEdit_3.textChanged.connect(update_sequence_visibility)
        self.lineEdit_4.textChanged.connect(update_sequence_visibility)
        self.lineEdit_5.textChanged.connect(update_sequence_visibility)
        self.lineEdit_6.textChanged.connect(update_sequence_visibility)
        update_sequence_visibility()

        self.checkBox_1.toggled.connect(lambda checked: self.checkBox_2.setVisible(checked))
        self.checkBox_2.toggled.connect(lambda checked: self.checkBox_3.setVisible(checked))
        self.checkBox_3.toggled.connect(lambda checked: self.checkBox_4.setVisible(checked))
        self.checkBox_4.toggled.connect(lambda checked: self.checkBox_5.setVisible(checked))
        self.checkBox_5.toggled.connect(lambda checked: self.checkBox_6.setVisible(checked))
        self.checkBox_6.toggled.connect(lambda checked: self.checkBox_7.setVisible(checked))
        self.checkBox_7.toggled.connect(lambda checked: self.pushButton.setVisible(checked))
        

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Caution</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic; color:#231f20;\">Current Limit for a single MRPO is 8.5A [MREL] and 8A [Legacy]</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Sample PO</span></p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PMPRESS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Total Current</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Differential Pressure</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Gaurd PO</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PMPRESS</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Total Current</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Differential Pressure</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"After 4 strokes on each PO \u2013 set restrictor pressure to zero (OPEN Restrictor)", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Stop the pumps and open the BYPASS valve", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Remove the bottle fill tank and connect shop air to the probe barrel", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Remove the restrictors from the exit ports", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Increase the pump speed to 2000 rpm and start pump to flush the flowline with air", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Confirm that the SOL3 is switching with the strokes", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Stop the pump when only air is coming out of the flowline", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

from .Perform_MRPO_GS_7 import Perform_MRPO_GS_7

class Perform_MRPO_GS_6(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # Collect all relevant user input directly into self.child_metadata (flat dict, like MRFA)
        ui = self.ui
        if self.child_metadata is None:
            self.child_metadata = {}
        # Frame 2 (Sample PO)
        self.child_metadata['sample_pmpress'] = ui.lineEdit_1.text()
        self.child_metadata['sample_total_current'] = ui.lineEdit_2.text()
        self.child_metadata['sample_diff_pressure'] = ui.lineEdit_3.text()
        # Frame 3 (Guard PO)
        self.child_metadata['guard_pmpress'] = ui.lineEdit_4.text()
        self.child_metadata['guard_total_current'] = ui.lineEdit_5.text()
        self.child_metadata['guard_diff_pressure'] = ui.lineEdit_6.text()
        # Checkboxes
        self.child_metadata['after_4_strokes_open_restrictor'] = ui.checkBox_1.isChecked()
        self.child_metadata['stop_pumps_open_bypass'] = ui.checkBox_2.isChecked()
        self.child_metadata['remove_bottle_fill_connect_air'] = ui.checkBox_3.isChecked()
        self.child_metadata['remove_restrictors'] = ui.checkBox_4.isChecked()
        self.child_metadata['increase_speed_flush_air'] = ui.checkBox_5.isChecked()
        self.child_metadata['sol3_switching'] = ui.checkBox_6.isChecked()
        self.child_metadata['stop_pump_air_only'] = ui.checkBox_7.isChecked()

        dialog7 = Perform_MRPO_GS_7(self.child_metadata, self.admin_metadata)
        if dialog7.exec() == QDialog.Accepted:
            self.accept()  # ✅ Close this dialog and continue chain

