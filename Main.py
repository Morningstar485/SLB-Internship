from PySide6.QtWidgets import QApplication, QDialog
from flow_controller import Controller_class
from Design.Design_1 import Design_1  # Only the first design dialog
from Module_Selection import mod_selec       # Used later for extracting tool info
import sys
from utils import generate_Design_report

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 1. Create global admin metadata
    admin_metadata = {}

    # 2. Start the design phase (all 8 dialogs internally linked)
    design_start = Design_1(admin_metadata)
    if design_start.exec() != QDialog.Accepted:
        sys.exit()  # Exit if user cancels anywhere in the design chain

    # 3. After design ends, get tool selection + tool-specific metadata
    selector_dialog = mod_selec(admin_metadata)
    if selector_dialog.exec() == QDialog.Accepted:
        generate_Design_report(admin_metadata)
        selected_tools = selector_dialog.ui.get_selected_tools()

        # 4. Launch Prepare & Perform controller
        controller = Controller_class(selected_tools, admin_metadata)
        controller.run_all()
    sys.exit(0)
