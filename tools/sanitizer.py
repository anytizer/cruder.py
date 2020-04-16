import re


# SQL Safety
def sql(string=""):
    safe = re.sub(r'[^a-z0-9_]', '', string)
    assert safe != "", "Sanitizer returned empty string"
    return safe
