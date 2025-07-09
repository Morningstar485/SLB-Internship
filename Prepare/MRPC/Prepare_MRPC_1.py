from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget, QDialog)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(338, 304)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_1 = QRadioButton(self.frame)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout.addWidget(self.radioButton_1)


        self.verticalLayout_4.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Are any of the following </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">modules required in the string</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">- MIFA</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">- MRBA</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">- Tools below MDT</span></p></body></html>", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Yes", None))
        self.radioButton_1.setText(QCoreApplication.translate("Form", u"No", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Next", None))
    # retranslateUi

from .Prepare_MRPC_2 import Prepare_MRPC_2
from .Prepare_MRPC_7 import Prepare_MRPC_7

class Prepare_MRPC_1(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        if self.ui.radioButton_2.isChecked():
            dialog = Prepare_MRPC_2(self.child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                self.accept()  # ✅ Close this dialog and continue chain
        elif self.ui.radioButton_1.isChecked():
            dialog = Prepare_MRPC_7(self.child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                self.accept()  # ✅ Close this dialog and continue chain

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())