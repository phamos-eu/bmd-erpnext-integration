# Copyright (c) 2023, Phamos GmbH and contributors
# For license information, please see license.txt

import frappe, json
from frappe.model.document import Document

class BMDBuErfExport(Document):
	pass


@frappe.whitelist()
def get_invoice_list_in_buerf_format(invoice_type, start_date, end_date, only_submitted_documents):
	invoices = frappe.db.get_list(invoice_type, 
				filters=[["posting_date", ">=", start_date], 
						 ["posting_date", "<=", end_date],
						 ["exported", "=", 0],
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
		# steuercode = frappe.db.get_value(tax_table + " Template", invoice["taxes_and_charges"], "steuercode")

		# get tax rate
		# taxes = frappe.db.get_list(tax_table, filters={"parent": invoice["name"]}, fields=["rate"])
		# tax_rate = 0
		# if len(taxes) > 0:
		# 	tax_rate = taxes[0]["rate"]
		taxes = get_taxes(invoice_type, invoice["name"])

		for tax in taxes:
			result.append({
				"satzart": invoice["satzart"],
				"konto": party_bank_account,
				"gkonto": company_bank_account,
				"belegnr": invoice["name"],
				"belegdatum": invoice["posting_date"],
				"buchsymbol": buchsymbol,
				"buchcode": buchcode,
				"prozent": tax["rate"],
				"steuercode": tax["tax_code"],
				"betrag": tax["amount"],
				"steuer": tax["tax_amount"],
				"text": text,
				"kost": invoice["cost_center"],
				"extbelegnr": extbelegnr
			})
	return result

def get_tax_code(doc, item_code):
	for item in doc.items:
		if item.item_code == item_code:
			return frappe.db.get_value("Item Tax Template", item.item_tax_template, "steuercode")
	return ""

def get_taxes(invoice_type, invoice_name):
	doc = frappe.get_doc(invoice_type, invoice_name)
	result = []
	for tax in doc.taxes:
		item_wise_tax_detail = json.loads(tax.item_wise_tax_detail)
		for item_code in item_wise_tax_detail.keys():
			if item_wise_tax_detail[item_code][1] > 0 and item_wise_tax_detail[item_code][0] > 0:
				result.append({
					"rate": item_wise_tax_detail[item_code][0],
					"tax_amount": str(round(item_wise_tax_detail[item_code][1], 3)),
					"tax_code": get_tax_code(doc, item_code),
					"amount": str(round(item_wise_tax_detail[item_code][1] / (item_wise_tax_detail[item_code][0] / 100), 3))
				})

	return result
