import frappe
import json
from frappe.utils import validate_email_address, get_url
from frappe.core.doctype.user.user import generate_keys
from frappe.utils.password import update_password

@frappe.whitelist(allow_guest=True)
def user_signup(full_name, email, password):
    """
    API to create a new user with the 'LMS Student' role.
    """

    if not validate_email_address(email):
        return {"status": "error", "field": "email", "message": "Invalid email format"}

    # Check if user already exists
    if frappe.db.exists("User", email):
        return {"status": "error", "field": "email", "message": "Email is already registered"}

    try:
        # Create new user
        user = frappe.get_doc({
            "doctype": "User",
            "email": email,
            "first_name": full_name,
            "enabled": 1,
            "new_password": password,
            "send_welcome_email": 1
        })
        print(password,"*"*100)
        user.flags.ignore_permissions = True
        user.flags.ignore_password_policy = True
        user.insert()
        update_password(user=user.name,pwd=password)

        # Assign LMS Student role
        user.add_roles("LMS Student")
        default_role = frappe.db.get_single_value("Portal Settings", "default_role")
        if default_role:
            user.add_roles(default_role)

        return {"status": "success", "message": "Signup successful! Please check your email."}

    except Exception as e:
        frappe.log_error(f"User Signup Error: {str(e)}")
        return {"status": "error", "message": "An error occurred during signup."}
