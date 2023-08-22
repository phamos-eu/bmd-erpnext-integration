from . import __version__ as app_version

app_name = "bmd_erpnext_integration"
app_title = "Bmd Erpnext Integration"
app_publisher = "Phamos GmbH"
app_description = "Bmd Erpnext Integration"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@phamos.eu[Du"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bmd_erpnext_integration/css/bmd_erpnext_integration.css"
# app_include_js = "/assets/bmd_erpnext_integration/js/bmd_erpnext_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/bmd_erpnext_integration/css/bmd_erpnext_integration.css"
# web_include_js = "/assets/bmd_erpnext_integration/js/bmd_erpnext_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bmd_erpnext_integration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bmd_erpnext_integration.install.before_install"
# after_install = "bmd_erpnext_integration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bmd_erpnext_integration.uninstall.before_uninstall"
# after_uninstall = "bmd_erpnext_integration.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bmd_erpnext_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"bmd_erpnext_integration.tasks.all"
#	],
#	"daily": [
#		"bmd_erpnext_integration.tasks.daily"
#	],
#	"hourly": [
#		"bmd_erpnext_integration.tasks.hourly"
#	],
#	"weekly": [
#		"bmd_erpnext_integration.tasks.weekly"
#	]
#	"monthly": [
#		"bmd_erpnext_integration.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "bmd_erpnext_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "bmd_erpnext_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "bmd_erpnext_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["bmd_erpnext_integration.utils.before_request"]
# after_request = ["bmd_erpnext_integration.utils.after_request"]

# Job Events
# ----------
# before_job = ["bmd_erpnext_integration.utils.before_job"]
# after_job = ["bmd_erpnext_integration.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"bmd_erpnext_integration.auth.validate"
# ]


fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Sales Invoice-satzart"
            ]
        ]
    ]}
]