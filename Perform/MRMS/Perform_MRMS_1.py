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
        Dialog.resize(523, 700)
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

        self.verticalLayout.addWidget(self.checkBox_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit_1 = QLineEdit(self.frame_5)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(0, 0))
        self.lineEdit_1.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_1)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_2)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_15 = QFrame(Dialog)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(41, 41))
        self.label_17.setMaximumSize(QSize(41, 41))
        self.label_17.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_16.addWidget(self.label_18)


        self.verticalLayout.addWidget(self.frame_15)

        self.frame_16 = QFrame(Dialog)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.label_19 = QLabel(self.frame_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(41, 41))
        self.label_19.setMaximumSize(QSize(41, 41))
        self.label_19.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_19.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_17.addWidget(self.label_20)


        self.verticalLayout.addWidget(self.frame_16)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.frame_8 = QFrame(Dialog)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.frame_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_10.addWidget(self.lineEdit_3)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.lineEdit_4 = QLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_11.addWidget(self.lineEdit_4)


        self.horizontalLayout_9.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_17 = QFrame(Dialog)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(41, 41))
        self.label_21.setMaximumSize(QSize(41, 41))
        self.label_21.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_17)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_18.addWidget(self.label_22)


        self.verticalLayout.addWidget(self.frame_17)

        self.frame_18 = QFrame(Dialog)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.label_23 = QLabel(self.frame_18)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(41, 41))
        self.label_23.setMaximumSize(QSize(41, 41))
        self.label_23.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_23)

        self.label_26 = QLabel(self.frame_18)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_20.addWidget(self.label_26)


        self.verticalLayout.addWidget(self.frame_18)

        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.frame_11 = QFrame(Dialog)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.lineEdit_5 = QLineEdit(self.frame_12)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_13.addWidget(self.lineEdit_5)


        self.horizontalLayout_12.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.lineEdit_6 = QLineEdit(self.frame_13)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_14.addWidget(self.lineEdit_6)


        self.horizontalLayout_12.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame_11)

        self.frame_19 = QFrame(Dialog)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setSpacing(15)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.label_29 = QLabel(self.frame_19)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(41, 41))
        self.label_29.setMaximumSize(QSize(41, 41))
        self.label_29.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_29.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_29)

        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_22.addWidget(self.label_28)


        self.verticalLayout.addWidget(self.frame_19)

        self.frame_20 = QFrame(Dialog)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.label_27 = QLabel(self.frame_20)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(41, 41))
        self.label_27.setMaximumSize(QSize(41, 41))
        self.label_27.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_27)

        self.label_30 = QLabel(self.frame_20)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_21.addWidget(self.label_30)


        self.verticalLayout.addWidget(self.frame_20)

        self.frame_14 = QFrame(Dialog)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setSpacing(15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(41, 41))
        self.label_15.setMaximumSize(QSize(41, 41))
        self.label_15.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_15.addWidget(self.label_16)


        self.verticalLayout.addWidget(self.frame_14)

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

        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_11.hide()
        self.frame_14.hide()
        self.frame_15.hide()
        self.frame_16.hide()
        self.frame_17.hide()
        self.frame_18.hide()
        self.frame_19.hide()
        self.frame_20.hide()
        self.label_5.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.pushButton.hide()

        # Show/hide label_5, frame_7, and frame_14 based on checkBox_1
        self.checkBox_1.toggled.connect(lambda checked: self.label_5.setVisible(checked))
        self.checkBox_1.toggled.connect(lambda checked: self.label_13.setVisible(checked))
        self.checkBox_1.toggled.connect(lambda checked: self.label_14.setVisible(checked))
        self.checkBox_1.toggled.connect(lambda checked: self.frame_7.setVisible(checked))
        self.checkBox_1.toggled.connect(lambda checked: self.frame_8.setVisible(checked))
        self.checkBox_1.toggled.connect(lambda checked: self.frame_11.setVisible(checked))
        self.checkBox_1.toggled.connect(lambda checked: self.frame_14.setVisible(checked))

        # Show/hide frame_15 if lineEdit_1 is outside 122-138 (exclusive)
        def check_lineEdit_1():
            try:
                val = float(self.lineEdit_1.text())
                self.frame_15.setVisible(val < 122 or val > 138)
            except ValueError:
                self.frame_15.setVisible(False)
        self.lineEdit_1.textChanged.connect(check_lineEdit_1)
        check_lineEdit_1()

        # Show/hide frame_16 if lineEdit_2 is outside 122-138 (exclusive)
        def check_lineEdit_2():
            try:
                val = float(self.lineEdit_2.text())
                self.frame_16.setVisible(val < 122 or val > 138)
            except ValueError:
                self.frame_16.setVisible(False)
        self.lineEdit_2.textChanged.connect(check_lineEdit_2)
        check_lineEdit_2()

        def check_lineEdit_3():
            try:
                val = float(self.lineEdit_3.text())
                self.frame_17.setVisible(val < -5 or val > 5)
            except ValueError:
                self.frame_17.setVisible(False)
        self.lineEdit_3.textChanged.connect(check_lineEdit_3)
        check_lineEdit_3()

        def check_lineEdit_4():
            try:
                val = float(self.lineEdit_4.text())
                self.frame_18.setVisible(val < -5 or val > 5)
            except ValueError:
                self.frame_18.setVisible(False)
        self.lineEdit_4.textChanged.connect(check_lineEdit_4)
        check_lineEdit_4()

        def check_lineEdit_5():
            try:
                val = float(self.lineEdit_5.text())
                self.frame_19.setVisible(val < 122 or val > 138)
            except ValueError:
                self.frame_19.setVisible(False)
        self.lineEdit_5.textChanged.connect(check_lineEdit_5)
        check_lineEdit_5()

        def check_lineEdit_6():
            try:
                val = float(self.lineEdit_6.text())
                self.frame_20.setVisible(val < 122 or val > 138)
            except ValueError:
                self.frame_20.setVisible(False)
        self.lineEdit_6.textChanged.connect(check_lineEdit_6)
        check_lineEdit_6()

        # Helper to check if all line edits are in acceptable range
        def all_lineedits_acceptable():
            try:
                v1 = float(self.lineEdit_1.text())
                v2 = float(self.lineEdit_2.text())
                v3 = float(self.lineEdit_3.text())
                v4 = float(self.lineEdit_4.text())
                v5 = float(self.lineEdit_5.text())
                v6 = float(self.lineEdit_6.text())
            except ValueError:
                return False
            if not (122 < v1 < 138): return False
            if not (122 < v2 < 138): return False
            if not (-5 < v3 < 5): return False
            if not (-5 < v4 < 5): return False
            if not (122 < v5 < 138): return False
            if not (122 < v6 < 138): return False
            return True

        def update_pushButton_visibility():
            # Only show pushButton if checkBox_1 is checked and all line edits are acceptable
            self.pushButton.setVisible(self.checkBox_1.isChecked() and all_lineedits_acceptable())

        self.checkBox_1.toggled.connect(update_pushButton_visibility)
        self.lineEdit_1.textChanged.connect(update_pushButton_visibility)
        self.lineEdit_2.textChanged.connect(update_pushButton_visibility)
        self.lineEdit_3.textChanged.connect(update_pushButton_visibility)
        self.lineEdit_4.textChanged.connect(update_pushButton_visibility)
        self.lineEdit_5.textChanged.connect(update_pushButton_visibility)
        self.lineEdit_6.textChanged.connect(update_pushButton_visibility)
        update_pushButton_visibility()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Initialize MRMS", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Open USV and LSV</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">USV</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">LSV</span></p></body></html>", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">USV Open Value must be between 122 and 138</span></p></body></html>", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">LSV Open Value must be between 122 and 138</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Close USV and LSV</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">USV</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">LSV</span></p></body></html>", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">USV Close Value should be between -5 to +5</span></p></body></html>", None))
        self.label_23.setText("")
        self.label_26.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">LSV Close Value should be between -5 to +5</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Open USV and LSV</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">USV</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">LSV</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_28.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">USV Open Value must be between 122 and 138</span></p></body></html>", None))
        self.label_27.setText("")
        self.label_30.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">LSV Open Value must be between 122 and 138</span></p></body></html>", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Check physical movement of seal valve piston</span></p><p><span style=\" font-size:14pt; font-weight:700;\">while operating. If not, tool is \u201cFailed\u201d</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

class Perform_MRMS_1(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        ui = self.ui
        if self.child_metadata is None:
            self.child_metadata = {}
        self.child_metadata['Initialize_MRMS'] = ui.checkBox_1.isChecked()
        self.child_metadata['USV_Open_1'] = ui.lineEdit_1.text()
        self.child_metadata['LSV_Open_1'] = ui.lineEdit_2.text()
        self.child_metadata['USV_Closed_1'] = ui.lineEdit_3.text()
        self.child_metadata['LSV_Closed_1'] = ui.lineEdit_4.text()
        self.child_metadata['USV_Open_2'] = ui.lineEdit_5.text()
        self.child_metadata['LSV_Open_2'] = ui.lineEdit_6.text()

        self.accept()  # ✅ Close this dialog and continue chain

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())