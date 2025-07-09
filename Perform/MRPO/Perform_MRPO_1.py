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
        Dialog.resize(672, 407)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(125, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_1 = QGroupBox(self.frame_2)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(110, 0))
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


        self.horizontalLayout_2.addWidget(self.groupBox_1)

        self.frame_12 = QFrame(self.frame_2)
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


        self.horizontalLayout_2.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(140, 0))
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_6)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.frame_13 = QFrame(self.frame)
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


        self.horizontalLayout.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.radioButton_3 = QRadioButton(self.frame_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.frame_3)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.radioButton_4)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_28 = QFrame(Dialog)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_28)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_28)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_28)


        self.retranslateUi(Dialog)

        # Hide all relevant widgets initially
        self.groupBox_1.hide()
        self.groupBox_2.hide()
        self.pushButton.hide()
        self.frame_3.hide()
        self.frame_12.hide()
        self.frame_13.hide()

        # Show groupBox_1 only when a choice is selected in the combo box (not index 0)
        def update_groupbox_1_visibility():
            self.groupBox_1.setVisible(self.comboBox.currentIndex() > 0)
        self.comboBox.currentIndexChanged.connect(update_groupbox_1_visibility)
        update_groupbox_1_visibility()

        # Show groupBox_2 only if radioButton_1 is selected, frame_12 if radioButton_2 is selected
        def update_groupbox_2_and_frame_12():
            self.groupBox_2.setVisible(self.radioButton_1.isChecked())
            self.frame_12.setVisible(self.radioButton_2.isChecked())
        self.radioButton_1.toggled.connect(update_groupbox_2_and_frame_12)
        self.radioButton_2.toggled.connect(update_groupbox_2_and_frame_12)
        update_groupbox_2_and_frame_12()

        # Show frame_3 if radioButton_3 is selected, frame_13 if radioButton_4 is selected
        def update_frame3_frame13():
            self.frame_3.setVisible(self.radioButton_3.isChecked())
            self.frame_13.setVisible(self.radioButton_4.isChecked())
        self.radioButton_3.toggled.connect(update_frame3_frame13)
        self.radioButton_4.toggled.connect(update_frame3_frame13)
        update_frame3_frame13()

        # Show pushButton only if either radioButton_3 or radioButton_4 is selected
        def update_pushButton_visibility():
            self.pushButton.setVisible(self.radioButton_3.isChecked() or self.radioButton_4.isChecked())
        self.radioButton_3.toggled.connect(update_pushButton_visibility)
        self.radioButton_4.toggled.connect(update_pushButton_visibility)
        update_pushButton_visibility()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select MRDU Type", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"STD", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"HP", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"XP", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"XXP", None))

        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"PO Initialize Ok?", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Check Solenoid </span><span style=\" font-size:16pt; font-weight:700; font-style:italic;\">3 </span><span style=\" font-size:16pt; font-style:italic;\">Status : Charging or not<br/>Recycle Power</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"PO Mode change Ok?", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Check Solenoid </span><span style=\" font-size:16pt; font-weight:700; font-style:italic;\">1 &amp; 2</span><span style=\" font-size:16pt; font-weight:700; font-style:italic;\"/><span style=\" font-size:16pt; font-style:italic;\">Status : Charging or not<br/>Recycle Power</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">What is the type of MRPO</span></p></body></html>", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Sample Side MRPO", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"Gaurd Side MRPO", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

from .Perform_MRPO_GS_2 import Perform_MRPO_GS_2
from .Perform_MRPO_SS_2 import Perform_MRPO_SS_2

class Perform_MRPO_1(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        # Store selected MRPO type in child_metadata and collect PO/Mode info
        if self.child_metadata is not None:
            self.child_metadata['mrpo_choice'] = self.ui.comboBox.currentText()
            if self.ui.radioButton_3.isChecked():
                self.child_metadata['mrpo_type'] = 'Sample Side MRPO'
            elif self.ui.radioButton_4.isChecked():
                self.child_metadata['mrpo_type'] = 'Gaurd Side MRPO'
            # Add PO Initialize and PO Mode change info
            self.child_metadata['po_initialize_ok'] = "yes" if self.ui.radioButton_1.isChecked() else "no" if self.ui.radioButton_2.isChecked() else ""
            self.child_metadata['po_mode_change_ok'] = "yes" if self.ui.radioButton_5.isChecked() else "no" if self.ui.radioButton_6.isChecked() else ""

        # Open the appropriate dialog based on the selected radio button
        if self.ui.radioButton_3.isChecked():
            dialog = Perform_MRPO_SS_2(self.child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                self.accept()  # ✅ Close this dialog and continue chain
        elif self.ui.radioButton_4.isChecked():
            dialog = Perform_MRPO_GS_2(self.child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                self.accept()  # ✅ Close this dialog and continue chain

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())