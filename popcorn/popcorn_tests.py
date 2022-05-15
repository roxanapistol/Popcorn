import unittest
import popcorn_methods as methods

class PopcornPositiveTestCases(unittest.TestCase): # container for our tests

    @staticmethod # signal to unittest that this is a function inside class , there is also classmethod
    def test_webpage(): # test in the name is mandatory
        methods.setUp()
        methods.check_homepage()
        methods.check_who_we_are()
        methods.verify_service_page()
        methods.case_studies()
        methods.jobs_page()
        methods.check_blog()
        methods.check_contact_us_page()
        methods.tearDown()
