from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget, QDialog)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(295, 190)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Legacy MRPC already in </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">NO TW mode</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Okay", None))
    # retranslateUi

class Prepare_MRPC_10(QDialog):
    def __init__(self, child_metadata=None, admin_metadata=None):
        super().__init__()
        self.child_metadata = child_metadata
        self.admin_metadata = admin_metadata

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.next_step)

    def next_step(self):
        self.child_metadata["Legacy MRPC in No TW Mode"] = None
        self.accept()  # ✅ Close this dialog and continue chain