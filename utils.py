import re


def parse_by_line_break_dash_space(text):
    """
    Separate text by line break, dash, and space so that each section can be saved as a separate object in a list.
    """
    try:
        sections = [s.strip() for s in re.split(r"(?<=\n)- ", text)]
        if len(sections) >= 2:
            sections = sections[1:]
        else:
            sections = []
    except (AttributeError, IndexError, TypeError) as e:
        print(e)
        sections = []
    return sections


# text = """

# Grits and gravy

# - This is a test text.
# - It has multiple lines.
# - It also has multiple dashes -- and multiple spaces   .
# """

text = "123"

# text = """
# - This is a test text.
# """

# text = """- This is a test text."""


sections = parse_by_line_break_dash_space(text)
print(sections)
