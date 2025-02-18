# Copyright (c) 2025, nfinity and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudentExtraDetails(Document):
    def after_insert(self):
        if self.current_college:
            college = frappe.get_doc("College", self.current_college)
            country = frappe.get_doc("Country", college.country)
            user = frappe.get_doc("User", self.user)
            if college.pincode and college.name:
                self.student_code = f"S{country.custom_mobile_number_extension}{college.pincode}{college.name}{self.name}"
                self.college_name = college.college_name
                self.full_name = user.full_name
                self.db_update()
