import importlib
from PySide6.QtWidgets import QDialog, QMessageBox, QApplication
from PySide6.QtCore import QDateTime, Qt
from utils import generate_pdf_report
from SFT_Dialog import SFT_Dialog  # Assuming SFT_Dialog is in the same directory

class Controller_class:
    def __init__(self, selected_tools: list[str], admin_metadata: dict):
        self.selected_tools = selected_tools  # E.g., ["MRHY", "MRPO"]
        self.admin_metadata = admin_metadata
        self.steps = ["Prepare", "Perform"]

    # def get_tool_instance_metadata(self, tool, instance_index):
    #     """Return the `instance_index`-th metadata dict matching the tool name."""
    #     all_tools = self.admin_metadata.get("modules", [])
    #     matches = [d for d in all_tools if d.get("tool") == tool.lower()]
    #     return matches[instance_index] if instance_index < len(matches) else {}


    def run_all(self):
        # 1. Add timestamp to admin metadata
        self.admin_metadata["design_end_time"] = QDateTime.currentDateTime().toString(Qt.ISODate)

        # 2. Show confirmation after design
        self.show_message("Design Complete", "Design phase has been completed. Proceed to Prepare phase?")

        #2.5 Open the SFT Dialog Box
        dialog = SFT_Dialog()
        dialog.exec()

        # 3. Run prepare phase
        self.run_prepare()

        # 4. Confirm before perform
        self.show_message("Prepare Complete", "Prepare phase has been completed. Proceed to Perform phase?")

        # 5. Run perform phase
        self.run_perform()

        # 6. Final completion dialog
        self.show_message("OST Complete", "All steps have been completed. OST is now complete.")

        QApplication.quit()  # Guarantees the event loop exits


    def run_prepare(self):
        for idx, tool in enumerate(self.selected_tools):
            print(f"Launching {tool} - Prepare phase")
            child_metadata = {}

            first_dialog_class = self.get_first_dialog_class(tool, "Prepare")
            if first_dialog_class is None:
                continue

            # tool_metadata = self.get_tool_instance_metadata(tool, idx)
            # child_metadata.update(tool_metadata)

            dialog = first_dialog_class(child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                print(f"{tool} - Prepare completed")

                generate_pdf_report(child_metadata, self.admin_metadata, step="Prepare", tool=f"{tool}_{idx}")


    def run_perform(self):
        print("Launching Perform admin dialogs")
        admin_child_metadata = {}
        perform_admin_class = self.get_first_admin_perform_class()
        if perform_admin_class is not None:
            dialog = perform_admin_class(admin_child_metadata, self.admin_metadata)
            if dialog.exec() != QDialog.Accepted:
                print("Perform admin step cancelled")
                return
            generate_pdf_report(admin_child_metadata, self.admin_metadata, step="PerformAdmin", tool="Admin")

        for idx, tool in enumerate(self.selected_tools):
            print(f"Launching {tool} - Perform phase")
            child_metadata = {}

            first_dialog_class = self.get_first_dialog_class(tool, "Perform")
            if first_dialog_class is None:
                continue

            # tool_metadata = self.get_tool_instance_metadata(tool, idx)
            # child_metadata.update(tool_metadata)

            dialog = first_dialog_class(child_metadata, self.admin_metadata)
            if dialog.exec() == QDialog.Accepted:
                print(f"{tool} - Perform completed")
                generate_pdf_report(child_metadata, self.admin_metadata, step="Perform", tool=f"{tool}_{idx}")


    def get_first_dialog_class(self, tool, step):
        step_cap = step.capitalize()
        tool_upper = tool.upper()
        file_name = f"{step_cap}_{tool_upper}_1"
        module_path = f"{step_cap}.{tool_upper}.{file_name}"

        try:
            module = importlib.import_module(module_path)
            return getattr(module, file_name)
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"[Error] Could not load {file_name} for {tool}-{step}: {e}")
            return None

    def get_first_admin_perform_class(self):
        try:
            module = importlib.import_module("Perform.Admin.Perform_Admin_1")
            return getattr(module, "Perform_Admin_1")
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"[Error] Could not load Perform_Admin_1: {e}")
            return None

    def show_message(self, title, message):
        QMessageBox.information(None, title, message)
