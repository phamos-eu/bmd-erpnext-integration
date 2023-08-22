// Copyright (c) 2023, Phamos GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('BMD BuErf Export', {
	refresh: function(frm) {
		frm.set_value("start_date", frappe.datetime.month_start())
		frm.set_value("end_date", frappe.datetime.month_end())
		frm.disable_save()
	},

	get_data: function(frm) {
		// frm.clear_table("bmd_buerf_export_table").refresh()
		frappe.call({
			method: "bmd_erpnext_integration.bmd_erpnext_integration.doctype.bmd_buerf_export.bmd_buerf_export.get_invoice_list_in_buerf_format",
			args: {
				invoice_type: frm.doc.invoice_type, 
				start_date: frm.doc.start_date, 
				end_date: frm.doc.end_date
			},
			callback: function(r) {
				console.log(r);
				r.message.forEach(row => {
					var child = frm.add_child("bmd_buerf_export_table")
					child = Object.assign(child, row)
					console.log(child);
				});
				frm.fields_dict['bmd_buerf_export_table'].refresh();
			}
		})
	},

	download_csv: function(frm){
		// create the CSV content
		var csvContent = "satzart,konto,gkonto,belegnr,belegdatum,buchsymbol,buchcode,prozent,steuercode,betrag,steuer,text,kost\n";
		frm.doc.bmd_buerf_export_table.forEach(function(row) {
			csvContent += `"${row.satzart}","${row.konto}","${row.gkonto}","${row.belegnr}","${row.belegdatum}","${row.buchsymbol}","${row.buchcode}","${row.prozent}","${row.steuercode}","${row.betrag}","${row.steuer}","${row.text}","${row.kost}"\n`
		});
		console.log(csvContent);

		// download the file
		var blob = new Blob([csvContent], { type: 'text/csv' });
		var downloadUrl = URL.createObjectURL(blob);
		var link = document.createElement('a');
		link.href = downloadUrl;
		link.download = 'child_table_data.csv';
		link.click();
		URL.revokeObjectURL(downloadUrl);
	}
});
