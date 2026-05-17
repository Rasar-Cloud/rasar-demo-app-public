// Copyright (c) 2026, Rasar Cloud and contributors
// For license information, please see LICENSE.md

frappe.ui.form.on("Rasar Demo Registro", {
	refresh(frm) {
		if (!frm.doc.nota_tecnica) {
			frm.set_value("nota_tecnica", __("Registro demo para validacion RasarCheck."));
		}
	},
});
