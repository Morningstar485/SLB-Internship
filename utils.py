import os
import sys
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def resource_path(relative_path):
    """ Get absolute path to resource (for dev and for PyInstaller bundle) """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generate_pdf_report(child_metadata, admin_metadata, step, tool):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Report_{tool}_{step}_{timestamp}.pdf"
    save_path = os.path.join("Reports", filename)
    os.makedirs("Reports", exist_ok=True)

    c = canvas.Canvas(save_path, pagesize=A4)

    # ✅ Tool info lookup from module list
    def get_tool_instance_metadata(admin_metadata, tool, instance_index):
        all_tools = admin_metadata.get("modules", [])
        matches = [d for d in all_tools if d.get("tool", "").lower() == tool.lower()]
        return matches[instance_index] if instance_index < len(matches) else {}

    # Inside generate_pdf_report()
    tool_metadata = get_tool_instance_metadata(admin_metadata, tool, instance_index=0)
    tool_code = tool_metadata.get("tool_code", "N/A")
    serial = tool_metadata.get("serial_number", "N/A")



    # --- Page 1: Step-specific Metadata ---
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, f"{tool.upper()} - {step} Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"Tool Code: {tool_code}")
    c.drawString(300, 780, f"Serial Number: {serial}")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 750, "Step-specific Metadata:")
    y = 730
    for key, value in child_metadata.items():
        c.setFont("Helvetica", 12)
        c.drawString(50, y, f"{key}: {value}")
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    # --- Page 2: Admin Metadata ---
    c.showPage()
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Global Admin Metadata")
    y = 780
    for key, value in admin_metadata.items():
        if key == "modules":
            continue  # Skip module data here
        c.setFont("Helvetica", 12)
        if isinstance(value, dict):
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, f"[{key.upper()}]")
            y -= 20
            for subkey, subval in value.items():
                c.setFont("Helvetica", 12)
                c.drawString(70, y, f"{subkey}: {subval}")
                y -= 20
        else:
            c.drawString(50, y, f"{key}: {value}")
            y -= 20
        if y < 50:
            c.showPage()
            y = 800

    c.save()
    print(f"PDF saved: {save_path}")

# --- Optional: Report for Design Phase ---
def generate_Design_report(admin_metadata):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Report_Design_{timestamp}.pdf"
    save_path = os.path.join("Reports", filename)
    os.makedirs("Reports", exist_ok=True)

    c = canvas.Canvas(save_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Design Phase Report")
    y = 780

    # Print everything except "modules" first
    for key, value in admin_metadata.items():
        if key == "modules":
            continue
        c.setFont("Helvetica", 12)
        c.drawString(50, y, f"{key}: {value}")
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    # Print module list
    y -= 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Toolstring Configuration:")
    y -= 20

    for i, tool in enumerate(admin_metadata.get("modules", []), start=1):
        name = tool.get("tool", "UNKNOWN").upper()
        code = tool.get("tool_code", "N/A")
        serial = tool.get("serial_number", "N/A")
        c.setFont("Helvetica", 12)
        c.drawString(50, y, f"{i}. {name} | Code: {code} | Serial: {serial}")
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    c.save()
    print(f"PDF saved: {save_path}")
