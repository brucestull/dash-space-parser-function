import re


def parse_by_line_break_dash_space(text):
    """
    Separate text by line break, dash, and space so that each section can be saved as a separate object in a list.
    """
    sections = [s.strip() for s in re.split(r"(?<=\n)- ", text)][1:]
    return sections


text = """

Grits and gravy

- This is a test text.
- It has multiple lines.
- It also has multiple dashes -- and multiple spaces   .
"""

text = "123"

text = """
- This is a test text.
"""

text = """- This is a test text."""

text = """
Section 1
- This is the first section.

Section 2 - This is the second section.

Section 3
- This is the third section.
"""


sections = parse_by_line_break_dash_space(text)
print(sections)
