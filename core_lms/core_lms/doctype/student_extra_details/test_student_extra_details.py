# Copyright (c) 2025, nfinity and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestStudentExtraDetails(UnitTestCase):
	"""
	Unit tests for StudentExtraDetails.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestStudentExtraDetails(IntegrationTestCase):
	"""
	Integration tests for StudentExtraDetails.
	Use this class for testing interactions between multiple components.
	"""

	pass
