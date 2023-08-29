// Copyright (c) 2023, Phamos GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('BMD BuErf Export', {
	refresh: function(frm) {
		frm.set_value("start_date", frappe.datetime.month_start())
		frm.set_value("end_date", frappe.datetime.month_end())
		frm.disable_save()
	},

	get_data: function(frm) {
		frm.clear_table("bmd_buerf_export_table")
		frm.refresh()
		frappe.call({
			method: "bmd_erpnext_integration.bmd_erpnext_integration.doctype.bmd_buerf_export.bmd_buerf_export.get_invoice_list_in_buerf_format",
			args: {
				invoice_type: frm.doc.invoice_type, 
				start_date: frm.doc.start_date, 
				end_date: frm.doc.end_date,
				only_submitted_documents: frm.doc.only_submitted_documents
			},
			callback: function(r) {
				if (r.message.length > 0){
					r.message.forEach(row => {
						var child = frm.add_child("bmd_buerf_export_table")
						child = Object.assign(child, row)
					});
					frm.fields_dict['bmd_buerf_export_table'].refresh();
				}else{
					frappe.msgprint("No invoices were fetched for this filters.")
				}
			}
		})
	},

	download_csv: function(frm){
		frappe.confirm("By downloading the CSV file, all the invoices listed here will be marked as 'Exported'. Are you sure you want to continue?", 
		() => {
			// create the CSV content
			var csvContent = "satzart,konto,gkonto,belegnr,belegdatum,buchsymbol,buchcode,prozent,steuercode,betrag,steuer,text,kost";
			csvContent += frm.doc.invoice_type == "Purchase Invoice" ? ",extbelegnr\n" : "\n"
			
			frm.doc.bmd_buerf_export_table.forEach(function(row) {
				csvContent += `"${row.satzart}","${row.konto}","${row.gkonto}","${row.belegnr}","${row.belegdatum}","${row.buchsymbol}","${row.buchcode}","${row.prozent}","${row.steuercode}","${row.betrag}","${row.steuer}","${row.text}","${row.kost}"`
				csvContent += frm.doc.invoice_type == "Purchase Invoice" ? `,"${row.extbelegnr}"\n` : "\n"
			});
	
			// download the file
			var blob = new Blob([csvContent], { type: 'text/csv' });
			var downloadUrl = URL.createObjectURL(blob);
			var link = document.createElement('a');
			link.href = downloadUrl;
			link.download = `BMD BuErf Export - ${frm.doc.invoice_type} - ${frm.doc.start_date} - ${frm.doc.end_date}.csv`;
			link.click();
			URL.revokeObjectURL(downloadUrl);

			mark_invoices_as_exported(frm.doc.invoice_type, frm.doc.bmd_buerf_export_table)
		})
	}
});

var mark_invoices_as_exported = function(type, table){
	var invoices = [...new Set(cur_frm.doc.bmd_buerf_export_table.map((e)=>e["belegnr"]))]
	invoices.forEach(invoice => {
		frappe.db.set_value(type, invoice, "exported", 1)
	});
}