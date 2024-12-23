// Copyright (c) 2024, Saad and contributors
// For license information, please see license.txt

frappe.ui.form.on("Appointment_", {
	refresh(frm) {
        frm.set_query("shift", (doc) => {
            return {
                "filters": {
                    "clinic": doc.clinic
                }
            }
        })
	},
});
