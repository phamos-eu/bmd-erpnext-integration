# Copyright (c) 2023, Phamos GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BMDBuErfExport(Document):
	pass


@frappe.whitelist()
def get_invoice_list_in_buerf_format(invoice_type, start_date, end_date, only_submitted_documents):
	invoices = frappe.db.get_list(invoice_type, 
				filters=[["posting_date", ">=", start_date], 
						 ["posting_date", "<=", end_date],
						 ["docstatus", "=", only_submitted_documents]],
				fields=["*"])

	result = []
	for invoice in invoices:
		if invoice_type == "Sales Invoice":
			party_name = "Customer"
			buchsymbol = "AR"
			buchcode = 1,
			text = "Ausgangsrechnung"
			extbelegnr = ""
			tax_table = "Sales Taxes and Charges"
		elif invoice_type == "Purchase Invoice":
			party_name = "Supplier"
			buchsymbol = "ER"
			buchcode = 2
			text = "Eingangsrechnung"
			extbelegnr = invoice["bill_no"]
			tax_table = "Purchase Taxes and Charges"

		party_bank_account = frappe.db.get_value(party_name, invoice[party_name.lower()], "default_bank_account")
		company_bank_account = frappe.db.get_value("Company", invoice["company"], "default_bank_account")

		# get tax rate
		taxes = frappe.db.get_list(tax_table, filters={"parent": invoice["name"]}, fields=["rate"])
		tax_rate = 0
		if len(taxes) > 0:
			tax_rate = taxes[0]["rate"]

		result.append({
			"satzart": invoice["satzart"],
			"konto": party_bank_account,
			"gkonto": company_bank_account,
			"belegnr": invoice["name"],
			"belegdatum": invoice["posting_date"],
			"buchsymbol": buchsymbol,
			"buchcode": buchcode,
			"prozent": tax_rate,
			"steuercode": "", # TODO 
			"betrag": invoice["grand_total"],
			"steuer": invoice["total_taxes_and_charges"],
			"text": text,
			"kost": invoice["cost_center"],
			"extbelegnr": extbelegnr
		})
	return result