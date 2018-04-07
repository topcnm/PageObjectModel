import unittest

from Tests.RegistrationPageTests import RegistrationPageTests
from Tests.SignOnPageTests import SignOnPageTests
from Tests.HomePageTests import HomePageTests

# Get all tests from SignOnTests and RegistrationTests classes
registration_tests = unittest.TestLoader().loadTestsFromTestCase(RegistrationPageTests)
sign_on_tests = unittest.TestLoader().loadTestsFromTestCase(SignOnPageTests)
home_page_sign_on_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)

# Create a test suite combining registration_tests and sign_on_tests
smoke_tests = unittest.TestSuite([registration_tests, sign_on_tests, home_page_sign_on_tests])

# Run tess suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)