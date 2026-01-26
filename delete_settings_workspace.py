#!/usr/bin/env python3
"""
Script to delete Settings workspace from database
Run with: bench --site mex execute mexico_einvoice.delete_settings_workspace.delete_settings_workspace
"""

import frappe

def delete_settings_workspace():
	"""Delete Settings workspace if it exists"""
	frappe.init(site='mex')
	frappe.connect()
	
	# Check if Settings workspace exists
	if frappe.db.exists("Workspace", "Settings"):
		print("Deleting Settings workspace...")
		frappe.delete_doc("Workspace", "Settings", force=1, ignore_permissions=True)
		frappe.db.commit()
		print("Settings workspace deleted successfully")
	else:
		print("Settings workspace does not exist")
	
	frappe.db.close()

if __name__ == "__main__":
	delete_settings_workspace()
