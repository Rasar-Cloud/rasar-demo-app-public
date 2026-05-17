import frappe
from rasar_demo_app.public_api.demo import ping_demo as ping_demo_public


@frappe.whitelist()
def ping_demo():
    if frappe.session.user == "Guest":
        raise frappe.PermissionError

    return ping_demo_public()
