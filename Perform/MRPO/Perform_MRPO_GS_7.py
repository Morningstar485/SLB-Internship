from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(791, 447)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_1 = QCheckBox(self.frame)
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

        self.checkBox_2 = QCheckBox(self.frame)
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

        self.checkBox_3 = QCheckBox(self.frame)
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

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(100, 25))
        self.lineEdit_2.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addWidget(self.frame_9)

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
        self.lineEdit_1.setMinimumSize(QSize(100, 25))
        self.lineEdit_1.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_1)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.frame)
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


        self.verticalLayout.addWidget(self.frame_12)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(100, 25))
        self.lineEdit_4.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_5.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(100, 25))
        self.lineEdit_3.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_9.addWidget(self.label_17)


        self.verticalLayout.addWidget(self.frame_13)

        self.checkBox_5 = QCheckBox(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.frame)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_6)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
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


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(41, 41))
        self.label_18.setMaximumSize(QSize(41, 41))
        self.label_18.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.checkBox_7 = QCheckBox(self.frame_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.frame_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setEnabled(True)
        self.checkBox_8.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.frame_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setEnabled(True)
        self.checkBox_9.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.frame_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setEnabled(True)
        self.checkBox_10.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(self.frame_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setEnabled(True)
        self.checkBox_11.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_11)

        self.frame_28 = QFrame(self.frame_2)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_28)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_28)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_28)
        self.horizontalLayout.addWidget(self.frame_2)
        self.retranslateUi(Dialog)

        self.checkBox_2.hide()
        self.checkBox_3.hide()
        self.checkBox_4.hide()
        self.checkBox_5.hide()
        self.checkBox_6.hide()
        self.checkBox_7.hide()
        self.checkBox_8.hide()
        self.checkBox_9.hide()
        self.checkBox_10.hide()
        self.checkBox_11.hide()

        self.frame_9.hide()
        self.frame_8.hide()
        self.frame_12.hide()
        self.frame_11.hide()
        self.frame_10.hide()
        self.frame_13.hide()
        self.groupBox_2.hide()
        self.frame_14.hide()

        self.pushButton.hide()

        # --- Custom logic for showing/hiding frames and checkboxes based on line edits ---

        def update_lineedit_2_logic():
            try:
                val = float(self.lineEdit_2.text())
                if val > 3100:
                    self.frame_12.setVisible(True)
                    self.frame_8.setVisible(False)
                else:
                    self.frame_12.setVisible(False)
                    self.frame_8.setVisible(True)
            except ValueError:
                self.frame_12.setVisible(False)
                self.frame_8.setVisible(False)
        self.lineEdit_2.textChanged.connect(update_lineedit_2_logic)
        update_lineedit_2_logic()

        def update_lineedit_1_logic():
            try:
                val = float(self.lineEdit_1.text())
                if val > 3100:
                    self.frame_12.setVisible(True)
                    self.checkBox_4.setVisible(False)
                else:
                    self.frame_12.setVisible(False)
                    self.checkBox_4.setVisible(True)
            except ValueError:
                self.frame_12.setVisible(False)
                self.checkBox_4.setVisible(False)
        self.lineEdit_1.textChanged.connect(update_lineedit_1_logic)
        update_lineedit_1_logic()

        def update_lineedit_4_logic():
            try:
                val = float(self.lineEdit_4.text())
                if val > 3100:
                    self.frame_13.setVisible(True)
                    self.frame_10.setVisible(False)
                else:
                    self.frame_13.setVisible(False)
                    self.frame_10.setVisible(True)
            except ValueError:
                self.frame_13.setVisible(False)
                self.frame_10.setVisible(False)
        self.lineEdit_4.textChanged.connect(update_lineedit_4_logic)
        update_lineedit_4_logic()

        def update_lineedit_3_logic():
            try:
                val = float(self.lineEdit_3.text())
                if val > 3100:
                    self.frame_13.setVisible(True)
                    self.checkBox_5.setVisible(False)
                else:
                    self.frame_13.setVisible(False)
                    self.checkBox_5.setVisible(True)
            except ValueError:
                self.frame_13.setVisible(False)
                self.checkBox_5.setVisible(False)
        self.lineEdit_3.textChanged.connect(update_lineedit_3_logic)
        update_lineedit_3_logic()

        self.checkBox_1.toggled.connect(lambda checked: self.checkBox_2.setVisible(checked))
        self.checkBox_2.toggled.connect(lambda checked: self.checkBox_3.setVisible(checked))
        self.checkBox_3.toggled.connect(lambda checked: self.frame_9.setVisible(checked))
        self.checkBox_4.toggled.connect(lambda checked: self.frame_11.setVisible(checked))
        self.checkBox_5.toggled.connect(lambda checked: self.checkBox_6.setVisible(checked))
        self.checkBox_6.toggled.connect(lambda checked: self.groupBox_2.setVisible(checked))
        self.radioButton_3.toggled.connect(lambda checked: self.checkBox_7.setVisible(checked))
        self.radioButton_4.toggled.connect(lambda checked: self.frame_14.setVisible(checked))
        self.checkBox_7.toggled.connect(lambda checked: self.checkBox_8.setVisible(checked))
        self.checkBox_8.toggled.connect(lambda checked: self.checkBox_9.setVisible(checked))
        self.checkBox_9.toggled.connect(lambda checked: self.checkBox_10.setVisible(checked))
        self.checkBox_10.toggled.connect(lambda checked: self.checkBox_11.setVisible(checked))
        self.checkBox_11.toggled.connect(lambda checked: self.pushButton.setVisible(checked))

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"MRFA showing GAS data in station log while pumping Air", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Remove the MPMP jig", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Retract the Probe", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraluic Pressure</span></p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Pressure Must be below 3100 Psi</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Check Auto Retract</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Set the Probe", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraluic Pressure</span></p></body></html>", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Pressure Must be below 3100 Psi</span></p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Down the 50V switch from MRPP", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"50V data showing \u201c0V\u201d ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Auto retract Pop up Window appeared", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Investigate and report to IE</span></p></body></html>", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Choose NO in the popup window which tells\n"
"you not to open the AUTO Retract probe", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Wait for 1 minute and verify that the\n"
"Probe & Piston did not Retracted", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"Subsequently, choose YES in the\n"
"popup window to Auto retract probe", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"Generate station dlis with naming\n"
"\u201cMDT OST_Rig name_Section_Date\"", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"Create Job spec dlis with naming\n"
"\u201cMDT PQ#--- FA#--- _date\"", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

class Perform_MRPO_GS_7(QDialog):
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
        self.child_metadata['mrfa_gas_data'] = ui.checkBox_1.isChecked()
        self.child_metadata['remove_mpmp_jig'] = ui.checkBox_2.isChecked()
        self.child_metadata['retract_probe'] = ui.checkBox_3.isChecked()
        self.child_metadata['hydraulic_pressure'] = ui.lineEdit_2.text()
        self.child_metadata['set_line_pressure_1'] = ui.lineEdit_1.text()
        self.child_metadata['set_probe'] = ui.checkBox_4.isChecked()
        self.child_metadata['set_line_pressure_2'] = ui.lineEdit_4.text()
        self.child_metadata['hydraulic_pressure_2'] = ui.lineEdit_3.text()
        self.child_metadata['down_50v_switch'] = ui.checkBox_5.isChecked()
        self.child_metadata['fifty_v_data_zero'] = ui.checkBox_6.isChecked()
        self.child_metadata['auto_retract_popup'] = "yes" if ui.radioButton_3.isChecked() else "no" if ui.radioButton_4.isChecked() else ""
        self.child_metadata['choose_no_popup'] = ui.checkBox_7.isChecked()
        self.child_metadata['wait_and_verify'] = ui.checkBox_8.isChecked()
        self.child_metadata['choose_yes_popup'] = ui.checkBox_9.isChecked()
        self.child_metadata['generate_station_dlis'] = ui.checkBox_10.isChecked()
        self.child_metadata['create_job_spec_dlis'] = ui.checkBox_11.isChecked()

        self.accept()  # ✅ Close this dialog and continue chain

