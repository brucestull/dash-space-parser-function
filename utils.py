import re

def parse_by_line_break_dash_space(text):
    """
    Separate text by line break, dash, and space so that each section can be saved as a separate object in a list.
    """
    # `s.strip()` removes leading and trailing whitespace
    # `(?<=\n)` is a positive lookbehind assertion that matches a dash
    # preceded by a newline.
    # A `positive lookbehind assertion` is a regex pattern that matches
    # a group of characters that are preceded by another group of characters.
    # `(?<=\n)-` matches a dash preceded by a newline.
    # `(?<=\n)- ` matches a dash preceded by a newline and a space.
    # `(?<=\n)- ` matches a dash preceded by a newline and multiple spaces.
    # `r"(?<=\n)- "` is a raw string literal that matches a dash preceded
    # by a newline and a space.
    # `re.split(r"(?<=\n)- ", text)` splits the text by space preceded by
    # a dash preceded by a newline.
    # `re.split(r"(?<=\n)- ", text)` returns a list of strings.
    # `[s.strip() for s in re.split(r"(?<=\n)- ", text)]` returns a list
    # of strings with leading and trailing whitespace removed.
    return [s.strip() for s in re.split(r"(?<=\n)- ", text)][1:]

text = """

Grits and gravy

- This is a test text.
- It has multiple lines.
- It also has multiple dashes -- and multiple spaces   .
"""

sections = parse_by_line_break_dash_space(text)
print(sections)
    