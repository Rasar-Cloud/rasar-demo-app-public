from rasar_demo_app import __version__
from rasar_demo_app.protected.license_guard import check_demo_license
from rasar_demo_app.protected.sensitive_logic import get_demo_status


def ping_demo():
    status = get_demo_status()
    license_status = check_demo_license()

    return {
        "ok": True,
        "app": "rasar_demo_app",
        "version": __version__,
        "message": "Rasar Demo App funcionando",
        "demo_status": status.get("demo_status"),
        "protected_layer": status.get("protected_layer"),
        "license": license_status,
    }
