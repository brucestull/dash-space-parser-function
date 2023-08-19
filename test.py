import unittest
from utils import parse_by_line_break_dash_space

class TestParseByLineBreakDashSpace(unittest.TestCase):
    
    def test_empty_string(self):
        text = ""
        expected = []
        self.assertEqual(parse_by_line_break_dash_space(text), expected)
        
    def test_single_section(self):
        text = "This is a test section."
        expected = []
        self.assertEqual(parse_by_line_break_dash_space(text), expected)
        
    def test_multiple_sections(self):
        text = """
        Section 1
        - This is the first section.
        
        Section 2
        - This is the second section.
        
        Section 3
        - This is the third section.
        """
        expected = ["This is the first section.", "This is the second section.", "This is the third section."]
        self.assertEqual(parse_by_line_break_dash_space(text), expected)
        
    def test_no_line_breaks(self):
        text = "- This is a test section."
        expected = []
        self.assertEqual(parse_by_line_break_dash_space(text), expected)
        
    def test_no_dashes(self):
        text = """
        Section 1
        This is the first section.
        
        Section 2
        This is the second section.
        
        Section 3
        This is the third section.
        """
        expected = []
        self.assertEqual(parse_by_line_break_dash_space(text), expected)
        
    def test_no_spaces(self):
        text = """
        Section 1
        -This is the first section.
        
        Section 2
        -This is the second section.
        
        Section 3
        -This is the third section.
        """
        expected = ["This is the first section.", "This is the second section.", "This is the third section."]
        self.assertEqual(parse_by_line_break_dash_space(text), expected)
        
    def test_mixed_line_breaks(self):
        text = """
        Section 1
        - This is the first section.
        
        Section 2 - This is the second section.
        
        Section 3
        - This is the third section.
        """
        expected = ["This is the first section.", "This is the third section."]
        self.assertEqual(parse_by_line_break_dash_space(text), expected)
        
if __name__ == '__main__':
    unittest.main()