import unittest
import utility


class TestUtilityMethods(unittest.TestCase):

    def test_when_string_with_placeholders_and_placeholder_replacements_are_provided_then_updated_string_is_returned(self):
        string_with_placeholders = "This is the {0} position in the {1} collection"
        replacements = ["4", "Names"]
        string_with_placeholders_replaced = utility.replace_placeholders_in_string(string_with_placeholders, replacements)
        self.assertEqual(string_with_placeholders_replaced, "This is the 4 position in the Names collection")

    def test_when_placeholder_number_does_not_start_with_zero_then_error_is_returned(self):
        string_with_placeholders = "This is the {1} position in the {2} collection"
        replacements = ["4", "Names"]
        with self.assertRaises(IndexError):
            utility.replace_placeholders_in_string(string_with_placeholders, replacements)

    def test_when_number_of_replacements_does_not_equal_number_of_placeholders_then_error_is_returned(self):
        string_with_placeholders = "This is the {0} position in the {1} collection"
        replacements = ["4"]
        with self.assertRaises(ValueError):
            utility.replace_placeholders_in_string(string_with_placeholders, replacements)

if __name__ == '__main__':
    unittest.main()
