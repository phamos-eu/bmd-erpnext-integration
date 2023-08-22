# Copyright (c) 2023, Phamos GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BMDBuErfExport(Document):
	pass


@frappe.whitelist()
def get_invoice_list_in_buerf_format(invoice_type, start_date, end_date):
	invoices = frappe.db.get_list(invoice_type, 
				filters=[["posting_date", ">=", start_date], ["posting_date", "<=", end_date]],
				fields=["*"])

	result = []
	for invoice in invoices:
		customer_bank_account = frappe.db.get_value("Customer", invoice["customer"], "default_bank_account")
		company_bank_account = frappe.db.get_value("Company", invoice["company"], "default_bank_account")

		# get tax rate
		taxes = frappe.db.get_list("Sales Taxes and Charges", filters={"parent": "ACC-SINV-2023-00006"}, fields=["rate"])
		tax_rate = 0
		if len(taxes) > 0:
			tax_rate = taxes[0]["rate"]

		result.append({
			"satzart": invoice["satzart"],
			"konto": customer_bank_account,
			"gkonto": company_bank_account,
			"belegnr": invoice["name"],
			"belegdatum": invoice["posting_date"],
			"buchsymbol": "AR",
			"buchcode": 1, # TODO
			"prozent": tax_rate,
			"steuercode": "", # TODO 
			"betrag": invoice["grand_total"],
			"steuer": invoice["total_taxes_and_charges"],
			"text": invoice_type,
			"kost": invoice["cost_center"]
		})
	return result