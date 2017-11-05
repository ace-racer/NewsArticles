import unittest
import utility


class TestUtilityMethods(unittest.TestCase):

    def test_when_string_with_placeholders_and_placeholder_replacements_are_provided_then_updated_string_is_returned(self):
        string_with_placeholders = "This is the {0} position in the {1} collection"
        replacements = ["4", "Names"]
        string_with_placeholders_replaced = utility.replace_placeholders_in_string(string_with_placeholders, replacements)
        self.assertEqual(string_with_placeholders_replaced, "This is the 4 position in the Names collection")


if __name__ == '__main__':
    unittest.main()
