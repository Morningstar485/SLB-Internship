from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(510, 246)
        self.verticalLayout_6 = QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(125, 25))
        self.lineEdit_3.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 25))
        self.pushButton.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("Select Module")
        self.comboBox.addItem("LEH - QT")
        self.comboBox.addItem("EDTC")
        self.comboBox.addItem("EDTA")
        self.comboBox.addItem("MRHY")
        self.comboBox.addItem("MRPQ")
        self.comboBox.addItem("MRPO")
        self.comboBox.addItem("MRPC")
        self.comboBox.addItem("MRMS")
        self.comboBox.addItem("MRSC")
        self.comboBox.addItem("MRFA")
        self.comboBox.addItem("MRBN")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 25))
        self.comboBox.setMaximumSize(QSize(150, 25))

        self.verticalLayout.addWidget(self.comboBox)

        # --- Add MRDU row placeholder for static row ---
        self.mrdu_row = None
        self.comboBox.currentIndexChanged.connect(lambda idx, cb=self.comboBox: self.handle_module_special_selection(cb, None, idx, is_static=True))

        # Store mapping of dynamic comboBoxes to their MRDU rows
        self.dynamic_mrdu_rows = {}
        self.dynamic_mrpq_rows = {}

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_1 = QLineEdit(self.frame_2)
        self.lineEdit_1.setObjectName(u"lineEdit")
        self.lineEdit_1.setMinimumSize(QSize(125, 25))
        self.lineEdit_1.setMaximumSize(QSize(125, 25))

        self.verticalLayout_2.addWidget(self.lineEdit_1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(125, 25))
        self.lineEdit_2.setMaximumSize(QSize(125, 25))

        self.verticalLayout_3.addWidget(self.lineEdit_2)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frame_4)

        # Add a layout to hold all module rows
        self.moduleRowsLayout = QVBoxLayout()
        self.moduleRowsLayout.setObjectName(u"moduleRowsLayout")
        self.moduleRowsLayout.setSpacing(-2)  # Reduce space between rows
        self.moduleRowsLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.addLayout(self.moduleRowsLayout)
        

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.add_module_rows)

        # --- Add Next button at the bottom in its own frame ---
        self.bottomFrame = QFrame(Dialog)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.bottomLayout = QVBoxLayout(self.bottomFrame)
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.bottomLayout.setContentsMargins(0, 0, 0, 0)

        self.nextButton = QPushButton(self.bottomFrame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setText("Start")
        self.nextButton.setMinimumHeight(25)
        self.nextButton.setMinimumHeight(25)
        self.bottomLayout.addWidget(self.nextButton)

        self.verticalLayout_6.addWidget(self.bottomFrame)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Input Toolstring Information</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">The first module would be at the top of the toolstring</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Enter the number of modules in the toolstring</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Select the Module</span></p></body></html>", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Module", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Module Code</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Serial Number</span></p></body></html>", None))
    # retranslateUi

    def add_module_rows(self):
        # Clear previous rows and MRDU rows
        while self.moduleRowsLayout.count():
            item = self.moduleRowsLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.dynamic_mrdu_rows.clear()

        try:
            num_rows = int(self.lineEdit_3.text())
        except ValueError:
            num_rows = 0

        for _ in range(num_rows - 1):
            new_frame = QFrame()
            new_frame.setFrameShape(QFrame.Shape.StyledPanel)
            new_frame.setFrameShadow(QFrame.Shadow.Raised)
            new_frame.setMinimumHeight(30)
            new_frame.setMaximumHeight(30)

            row_layout = QHBoxLayout(new_frame)
            row_layout.setContentsMargins(0, 0, 0, 0)

            # --- Module selection (ComboBox only, no label) ---
            comboBox = QComboBox(new_frame)
            for i in range(self.comboBox.count()):
                comboBox.addItem(self.comboBox.itemText(i))
            comboBox.setMinimumSize(QSize(150, 25))
            comboBox.setMaximumSize(QSize(150, 25))
            row_layout.addWidget(comboBox)

            # --- Module Code (LineEdit only, no label) ---
            lineEdit = QLineEdit(new_frame)
            lineEdit.setMinimumSize(QSize(125, 25))
            lineEdit.setMaximumSize(QSize(125, 25))
            row_layout.addWidget(lineEdit)

            # --- Serial Number (LineEdit only, no label) ---
            lineEdit_2 = QLineEdit(new_frame)
            lineEdit_2.setMinimumSize(QSize(125, 25))
            lineEdit_2.setMaximumSize(QSize(125, 25))
            row_layout.addWidget(lineEdit_2)

            self.moduleRowsLayout.addWidget(new_frame)

            # Connect MRPO handler for this comboBox
            comboBox.currentIndexChanged.connect(lambda idx, cb=comboBox, frame=new_frame: self.handle_module_special_selection(cb, frame, idx, is_static=False))

    def handle_module_special_selection(self, comboBox, parent_frame, index, is_static=False):
        # Remove MRDU row if it exists for this comboBox
        if is_static:
            if self.mrdu_row:
                self.moduleRowsLayout.removeWidget(self.mrdu_row)
                self.mrdu_row.deleteLater()
                self.mrdu_row = None
            if hasattr(self, "mrpq_row") and self.mrpq_row:
                self.moduleRowsLayout.removeWidget(self.mrpq_row)
                self.mrpq_row.deleteLater()
                self.mrpq_row = None
        else:
            if comboBox in self.dynamic_mrdu_rows:
                mrdu_row = self.dynamic_mrdu_rows.pop(comboBox)
                self.moduleRowsLayout.removeWidget(mrdu_row)
                mrdu_row.deleteLater()
            if comboBox in self.dynamic_mrpq_rows:
                mrpq_row = self.dynamic_mrpq_rows.pop(comboBox)
                self.moduleRowsLayout.removeWidget(mrpq_row)
                mrpq_row.deleteLater()

        # If MRPO is selected, add MRDU row (dropdown only, no line edits)
        if comboBox.currentText() == "MRPO":
            mrdu_row = QFrame()
            mrdu_row.setFrameShape(QFrame.Shape.StyledPanel)
            mrdu_row.setFrameShadow(QFrame.Shadow.Raised)
            row_layout = QHBoxLayout(mrdu_row)
            row_layout.setContentsMargins(0, 0, 0, 0)

            mrdu_combo = QComboBox(mrdu_row)
            mrdu_combo.addItem("Select MRDU")
            mrdu_combo.addItem("STD")
            mrdu_combo.addItem("HP")
            mrdu_combo.addItem("XHP")
            mrdu_combo.addItem("XXP")
            mrdu_combo.setMinimumSize(QSize(150, 25))
            mrdu_combo.setMaximumSize(QSize(150, 25))
            row_layout.addWidget(mrdu_combo)

            idx = 0 if is_static else self.moduleRowsLayout.indexOf(parent_frame) + 1
            self.moduleRowsLayout.insertWidget(idx, mrdu_row)
            if is_static:
                self.mrdu_row = mrdu_row
            else:
                self.dynamic_mrdu_rows[comboBox] = mrdu_row

        # If MRPQ is selected, add Probe and Piston dropdowns
        elif comboBox.currentText() == "MRPQ":
            mrpq_row = QFrame()
            mrpq_row.setFrameShape(QFrame.Shape.StyledPanel)
            mrpq_row.setFrameShadow(QFrame.Shadow.Raised)
            row_layout = QHBoxLayout(mrpq_row)
            row_layout.setContentsMargins(0, 0, 0, 0)

            # Probe dropdown
            probe_combo = QComboBox(mrpq_row)
            probe_combo.addItem("Select Probe")
            probe_combo.addItem("MPMP")
            probe_combo.addItem("MRLD")
            probe_combo.addItem("MRSD")
            probe_combo.setMinimumSize(QSize(150, 25))
            probe_combo.setMaximumSize(QSize(150, 25))
            row_layout.addWidget(probe_combo)

            # Piston dropdown
            piston_combo = QComboBox(mrpq_row)
            piston_combo.addItem("Select Piston")
            piston_combo.addItem("MRSL")
            piston_combo.addItem("MRLH")
            piston_combo.addItem("STD Kit")
            piston_combo.setMinimumSize(QSize(150, 25))
            piston_combo.setMaximumSize(QSize(150, 25))
            row_layout.addWidget(piston_combo)

            idx = 0 if is_static else self.moduleRowsLayout.indexOf(parent_frame) + 1
            self.moduleRowsLayout.insertWidget(idx, mrpq_row)
            if is_static:
                self.mrpq_row = mrpq_row
            else:
                self.dynamic_mrpq_rows[comboBox] = mrpq_row

    def get_selected_tools(self):
        tools = []

        # First row (static)
        tool = self.comboBox.currentText().strip().lower()
        if tool and tool != "select module":
            tools.append(tool)

        # Additional dynamic rows
        for i in range(self.moduleRowsLayout.count()):
            row = self.moduleRowsLayout.itemAt(i).widget()
            if row:
                combo = row.findChildren(QComboBox)[0]
                tool = combo.currentText().strip().lower()
                if tool and tool != "select module":
                    tools.append(tool)

        return tools
    
    def get_metadata(self):
        module_data_list = []

        # --- Static row ---
        tool = self.comboBox.currentText().strip().lower()
        code = self.lineEdit_1.text().strip()
        serial = self.lineEdit_2.text().strip()

        if tool and tool != "select module":
            entry = {
                "tool": tool,
                "tool_code": code,
                "serial_number": serial
            }

            if tool == "mrpo" and hasattr(self, "mrdu_row"):
                entry["mrdu_type"] = self.mrdu_row.findChildren(QComboBox)[0].currentText().strip()
            if tool == "mrpq" and hasattr(self, "mrpq_row"):
                probe, piston = self.mrpq_row.findChildren(QComboBox)
                entry["probe"] = probe.currentText().strip()
                entry["piston"] = piston.currentText().strip()

            module_data_list.append(entry)

        # --- Dynamic rows ---
        for i in range(self.moduleRowsLayout.count()):
            row = self.moduleRowsLayout.itemAt(i).widget()
            if row:
                lineedits = row.findChildren(QLineEdit)
                if len(lineedits) < 2:
                    continue  # Skip non-module rows
                combo = row.findChildren(QComboBox)[0]
                code = lineedits[0].text().strip()
                serial = lineedits[1].text().strip()
                tool = combo.currentText().strip().lower()

                if tool and tool != "select module":
                    entry = {
                        "tool": tool,
                        "tool_code": code,
                        "serial_number": serial
                    }

                    if tool == "mrpo" and combo in self.dynamic_mrdu_rows:
                        entry["mrdu_type"] = self.dynamic_mrdu_rows[combo].findChildren(QComboBox)[0].currentText().strip()

                    if tool == "mrpq" and combo in self.dynamic_mrpq_rows:
                        probe, piston = self.dynamic_mrpq_rows[combo].findChildren(QComboBox)
                        entry["probe"] = probe.currentText().strip()
                        entry["piston"] = piston.currentText().strip()

                    module_data_list.append(entry)

        return module_data_list


class mod_selec(QDialog):
    def __init__(self, admin_metadata):
        super().__init__()
        self.admin_metadata = admin_metadata

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # ✅ Now safe to connect buttons
        self.ui.nextButton.clicked.connect(self.confirm_and_continue)

    def confirm_and_continue(self):
        tools = self.ui.get_selected_tools()
        if not tools:
            QMessageBox.warning(self, "No Tools Selected", "Please select at least one module before continuing.")
            return

        module_metadata = self.ui.get_metadata()
        self.admin_metadata["modules"] = module_metadata  # ← Now a list of dicts
        self.accept()
