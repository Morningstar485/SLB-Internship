from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(558, 476)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 25))
        self.comboBox.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.frame_4)

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

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 0))
        self.lineEdit_6.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_6)


        self.verticalLayout.addWidget(self.frame)

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

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.lineEdit_7 = QLineEdit(self.frame_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 0))
        self.lineEdit_7.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_7)


        self.verticalLayout.addWidget(self.frame_2)

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

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.lineEdit_8 = QLineEdit(self.frame_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 0))
        self.lineEdit_8.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_8)


        self.verticalLayout.addWidget(self.frame_3)

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


        self.retranslateUi(Dialog)

        self.frame_14.hide()
        self.frame_15.hide()
        self.frame_16.hide()
        self.frame_17.hide()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.pushButton.hide()

        def update_frames_visibility():
            # "Exit Port" is at index 3, "Low Shock" is 1, "Water Receptacle" is 2
            idx = self.comboBox.currentIndex()
            if self.checkBox_1.isChecked():
                if idx == 3:
                    self.frame.setVisible(True)
                    self.frame_2.setVisible(True)
                    self.frame_3.setVisible(True)
                    self.frame_14.setVisible(True)
                elif idx in (1, 2):
                    self.frame.setVisible(True)
                    self.frame_2.setVisible(True)
                    self.frame_3.setVisible(False)
                else:
                    self.frame.setVisible(False)
                    self.frame_2.setVisible(False)
                    self.frame_3.setVisible(False)
            else:
                self.frame.setVisible(False)
                self.frame_2.setVisible(False)
                self.frame_3.setVisible(False)

        self.checkBox_1.toggled.connect(update_frames_visibility)
        self.comboBox.currentIndexChanged.connect(update_frames_visibility)
        update_frames_visibility()

        # --- Show/hide frame_15 if lineEdit_6 is outside 122-138 ---
        def check_lineEdit_6():
            try:
                val = float(self.lineEdit_6.text())
                self.frame_15.setVisible(val < 122 or val > 138)
            except ValueError:
                self.frame_15.setVisible(False)
        self.lineEdit_6.textChanged.connect(check_lineEdit_6)
        check_lineEdit_6()

        # --- Show/hide frame_16 if lineEdit_7 is outside -5 to 5 ---
        def check_lineEdit_7():
            try:
                val = float(self.lineEdit_7.text())
                self.frame_16.setVisible(val < -5 or val > 5)
            except ValueError:
                self.frame_16.setVisible(False)
        self.lineEdit_7.textChanged.connect(check_lineEdit_7)
        check_lineEdit_7()

        # --- Show/hide frame_17 if lineEdit_8 is outside 122-138 ---
        def check_lineEdit_8():
            try:
                val = float(self.lineEdit_8.text())
                self.frame_17.setVisible(val < 122 or val > 138)
            except ValueError:
                self.frame_17.setVisible(False)
        self.lineEdit_8.textChanged.connect(check_lineEdit_8)
        check_lineEdit_8()

        # --- Show pushButton only if all line edits are in their specified range ---
        def all_lineedits_acceptable():
            idx = self.comboBox.currentIndex()
            try:
                v6 = float(self.lineEdit_6.text())
                v7 = float(self.lineEdit_7.text())
                if idx == 3:
                    v8 = float(self.lineEdit_8.text())
            except ValueError:
                return False
            if not (122 <= v6 <= 138): return False
            if not (-5 <= v7 <= 5): return False
            if idx == 3:
                if not (122 <= v8 <= 138): return False
            return True

        def update_pushButton_visibility():
            self.pushButton.setVisible(all_lineedits_acceptable())

        self.lineEdit_6.textChanged.connect(update_pushButton_visibility)
        self.lineEdit_7.textChanged.connect(update_pushButton_visibility)
        self.lineEdit_8.textChanged.connect(update_pushButton_visibility)
        self.comboBox.currentIndexChanged.connect(update_pushButton_visibility)
        update_pushButton_visibility()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select MRSC Type", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Low Shock", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Water Receptacle", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Exit Port", None))

        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Close seal valve and reset valve position (SVLVPOS=0)", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Open seal Valve</span></p></body></html>", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Open seal Valve Value must be between 122 to 138</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Close seal Valve</span></p></body></html>", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Open seal Valve Value must be between -5 to 5</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Open seal Valve</span></p></body></html>", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Open seal Valve Value must be between 122 to 138</span></p></body></html>", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Keep OPEN till Guard PO Initialize and Mode set</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

class Perform_MRSC_1(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # Collect all relevant user input into child_metadata (flat dict, like MRMS)
        ui = self.ui

        if self.child_metadata is None:
            self.child_metadata = {}
        self.child_metadata['mrsc_type'] = ui.comboBox.currentText()
        self.child_metadata['close_seal_valve'] = ui.checkBox_1.isChecked()
        self.child_metadata['open_seal_valve'] = ui.lineEdit_6.text()
        self.child_metadata['close_seal_valve_value'] = ui.lineEdit_7.text()
        self.child_metadata['open_seal_valve_2'] = ui.lineEdit_8.text()
        
        self.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())