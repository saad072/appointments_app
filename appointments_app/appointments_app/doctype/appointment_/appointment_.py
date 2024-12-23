# Copyright (c) 2024, Saad and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Appointment_(Document):
	def after_insert(self):
		print("Your Queue number: ",self.add_to_appointment_queue())

	def add_to_appointment_queue(self):
		q = frappe.get_doc("Appointment Queue", {
			"date": self.date,
			"shift": self.shift,
			clinic: self.clinic
		})

		q.apppend("queue", {
			"appointment": self.name,
			"status": "Pending"
		})
		
		q.save(ignore_permissions=True)

		return len(q.queue)