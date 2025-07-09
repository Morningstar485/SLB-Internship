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
        Dialog.resize(605, 537)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(41, 41))
        self.label_7.setMaximumSize(QSize(41, 41))
        self.label_7.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.verticalLayout_4.addWidget(self.checkBox_2)

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


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_3 = QCheckBox(self.frame_5)
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

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.lineEdit_4 = QLineEdit(self.frame_13)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(75, 25))
        self.lineEdit_4.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_9.addWidget(self.lineEdit_4)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)

        self.lineEdit_5 = QLineEdit(self.frame_14)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(75, 25))
        self.lineEdit_5.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_10.addWidget(self.lineEdit_5)


        self.horizontalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.lineEdit_6 = QLineEdit(self.frame_15)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(75, 25))
        self.lineEdit_6.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_11.addWidget(self.lineEdit_6)


        self.horizontalLayout_8.addWidget(self.frame_15)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_16 = QFrame(Dialog)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_4 = QCheckBox(self.frame_16)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_4)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, -1)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.lineEdit_7 = QLineEdit(self.frame_18)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(75, 25))
        self.lineEdit_7.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_7)


        self.horizontalLayout_12.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_14.addWidget(self.label_17)

        self.lineEdit_8 = QLineEdit(self.frame_19)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(75, 25))
        self.lineEdit_8.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_14.addWidget(self.lineEdit_8)


        self.horizontalLayout_12.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_15.addWidget(self.label_18)

        self.lineEdit_9 = QLineEdit(self.frame_20)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(75, 25))
        self.lineEdit_9.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_15.addWidget(self.lineEdit_9)


        self.horizontalLayout_12.addWidget(self.frame_20)


        self.verticalLayout_6.addWidget(self.frame_17)


        self.verticalLayout.addWidget(self.frame_16)

        self.frame_21 = QFrame(Dialog)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_21)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.checkBox_5 = QCheckBox(self.frame_21)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_7.addWidget(self.checkBox_5)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, 0, -1)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.label_19 = QLabel(self.frame_23)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_17.addWidget(self.label_19)

        self.lineEdit_10 = QLineEdit(self.frame_23)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(75, 25))
        self.lineEdit_10.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_17.addWidget(self.lineEdit_10)


        self.horizontalLayout_16.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame_24)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_18.addWidget(self.label_20)

        self.lineEdit_11 = QLineEdit(self.frame_24)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(75, 25))
        self.lineEdit_11.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_18.addWidget(self.lineEdit_11)


        self.horizontalLayout_16.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.label_21 = QLabel(self.frame_25)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_19.addWidget(self.label_21)

        self.lineEdit_12 = QLineEdit(self.frame_25)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(75, 25))
        self.lineEdit_12.setMaximumSize(QSize(1000, 25))

        self.horizontalLayout_19.addWidget(self.lineEdit_12)


        self.horizontalLayout_16.addWidget(self.frame_25)


        self.verticalLayout_7.addWidget(self.frame_22)


        self.verticalLayout.addWidget(self.frame_21)

        self.frame_28 = QFrame(Dialog)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_28)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton = QPushButton(self.frame_28)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_9.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_28)


        self.retranslateUi(Dialog)

        self.frame_5.hide()
        self.frame_16.hide()
        self.frame_21.hide()
        self.pushButton.hide()

        def frame2_filled():
            try:
                float(self.lineEdit_1.text())
                float(self.lineEdit_2.text())
                float(self.lineEdit_3.text())
                return True
            except ValueError:
                return False

        def frame5_filled():
            try:
                float(self.lineEdit_4.text())
                float(self.lineEdit_5.text())
                float(self.lineEdit_6.text())
                return True
            except ValueError:
                return False

        def frame16_filled():
            try:
                float(self.lineEdit_7.text())
                float(self.lineEdit_8.text())
                float(self.lineEdit_9.text())
                return True
            except ValueError:
                return False

        def frame21_filled():
            try:
                float(self.lineEdit_10.text())
                float(self.lineEdit_11.text())
                float(self.lineEdit_12.text())
                return True
            except ValueError:
                return False

        def update_sequence_visibility():
            # Frame 2 is visible if checkBox_1 is checked (already handled)
            # Frame 5: only if checkBox_2 is checked and frame2_filled
            show5 = self.checkBox_2.isChecked() and frame2_filled()
            self.frame_5.setVisible(show5)
            # Frame 16: only if checkBox_3 is checked and frame5_filled
            show16 = self.checkBox_3.isChecked() and frame5_filled()
            self.frame_16.setVisible(show16)
            # Frame 21: only if checkBox_4 is checked and frame16_filled
            show21 = self.checkBox_4.isChecked() and frame16_filled()
            self.frame_21.setVisible(show21)
            # PushButton: only if checkBox_5 is checked and frame21_filled
            showBtn = self.checkBox_5.isChecked() and frame21_filled()
            self.pushButton.setVisible(showBtn)

        # Connect all relevant signals
        self.checkBox_2.toggled.connect(update_sequence_visibility)
        self.lineEdit_1.textChanged.connect(update_sequence_visibility)
        self.lineEdit_2.textChanged.connect(update_sequence_visibility)
        self.lineEdit_3.textChanged.connect(update_sequence_visibility)

        self.checkBox_3.toggled.connect(update_sequence_visibility)
        self.lineEdit_4.textChanged.connect(update_sequence_visibility)
        self.lineEdit_5.textChanged.connect(update_sequence_visibility)
        self.lineEdit_6.textChanged.connect(update_sequence_visibility)

        self.checkBox_4.toggled.connect(update_sequence_visibility)
        self.lineEdit_7.textChanged.connect(update_sequence_visibility)
        self.lineEdit_8.textChanged.connect(update_sequence_visibility)
        self.lineEdit_9.textChanged.connect(update_sequence_visibility)

        self.checkBox_5.toggled.connect(update_sequence_visibility)
        self.lineEdit_10.textChanged.connect(update_sequence_visibility)
        self.lineEdit_11.textChanged.connect(update_sequence_visibility)
        self.lineEdit_12.textChanged.connect(update_sequence_visibility)

        update_sequence_visibility()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Caution</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic; color:#231f20;\">Current Limit for a single MRPO is 8.5A [MREL] and 8A [Legacy]</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -500 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1000 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1500 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -2000 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

from .Perform_MRPO_SS_3 import Perform_MRPO_SS_3

class Perform_MRPO_SS_2_extra(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # Collect all relevant user input directly into child_metadata under "Restrictor Pressure : 1500 PSI"
        ui = self.ui
        if self.child_metadata is None:
            self.child_metadata = {}
        self.child_metadata['rpm_500_checked_1500'] = ui.checkBox_2.isChecked()
        self.child_metadata['rpm_500_hpress_1500'] = ui.lineEdit_1.text()
        self.child_metadata['rpm_500_motor_current_1500'] = ui.lineEdit_2.text()
        self.child_metadata['rpm_500_stroke_time_1500'] = ui.lineEdit_3.text()
        self.child_metadata['rpm_1000_checked_1500'] = ui.checkBox_3.isChecked()
        self.child_metadata['rpm_1000_hpress_1500'] = ui.lineEdit_4.text()
        self.child_metadata['rpm_1000_motor_current_1500'] = ui.lineEdit_5.text()
        self.child_metadata['rpm_1000_stroke_time_1500'] = ui.lineEdit_6.text()
        self.child_metadata['rpm_1500_checked_1500'] = ui.checkBox_4.isChecked()
        self.child_metadata['rpm_1500_hpress_1500'] = ui.lineEdit_7.text()
        self.child_metadata['rpm_1500_motor_current_1500'] = ui.lineEdit_8.text()
        self.child_metadata['rpm_1500_stroke_time_1500'] = ui.lineEdit_9.text()
        self.child_metadata['rpm_2000_checked_1500'] = ui.checkBox_5.isChecked()
        self.child_metadata['rpm_2000_hpress_1500'] = ui.lineEdit_10.text()
        self.child_metadata['rpm_2000_motor_current_1500'] = ui.lineEdit_11.text()
        self.child_metadata['rpm_2000_stroke_time_1500'] = ui.lineEdit_12.text()

        dialog3 = Perform_MRPO_SS_3(self.child_metadata, self.admin_metadata)
        if dialog3.exec() == QDialog.Accepted:
            self.accept()  # ✅ Close this dialog and continue chain
