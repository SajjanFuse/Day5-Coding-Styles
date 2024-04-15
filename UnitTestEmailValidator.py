import unittest
import re

def validate_email(email):
    """
    Validates an email address as:
    - Proper format: Presence of '@' symbol and no spaces in the address.
    - Valid email provider like Gmail, Yahoo, Outlook,

    Args
    ----
        email: The email address to validate (string).

    Returns
    -------
        True if the email is valid, False otherwise.
    """

    # Regular expression for checking for '@' and no spaces
    if not re.match(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", email):
        return False

    # Check for valid email providers
    valid_providers = ['gmail.com', 'yahoo.com', 'outlook.com']
    if email.split('@')[-1].lower() in valid_providers:
        return True

    return False


class EmailValidatorTest(unittest.TestCase):
    """
    A test suite for validating email addresses.
    """
    def test_valid_emails(self):
        """
        Tests the validation of valid email addresses.
        """
        valid_emails = [
            'john.doe@gmail.com',
            'user.name123@gmail.com',
            'john_doe123@yahoo.com',
        ]

        for email in valid_emails:
            self.assertTrue(validate_email(email), f"{email} should be valid but failed.")

    def test_invalid_emails(self):
        """
        Tests the validation of invalid email addresses.
        """
        invalid_emails = [
            'nodotemail',
            'too.many.dots@outlook..com',
            'user name@yahoo.com'
        ]
        
        for email in invalid_emails:
            self.assertFalse(validate_email(email), f"{email} should be invalid but passed.")

if __name__ == '__main__':
    unittest.main()
