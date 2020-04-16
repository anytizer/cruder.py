from os import path
from tools import sanitizer


"""
Pick up a configuration from a pool
"""
import configs._hrs as program
import configs._gardens as program

NAME = sanitizer.sql(program.name)
OUTPUT = program.output.replace("\\", "/").rstrip("/")
DATABASE = path.abspath(program.database)
CUSTOM_TEMPLATE = program.template_custom.rstrip("/")
CRUDS = program.cruds


"""
Manage config data sanity
"""
assert NAME != "", "Program name error"
assert path.isdir(OUTPUT), "Output directory error"
#assert path.isdir(CUSTOM_TEMPLATE), "Custom template path does not exist."
assert path.isfile(DATABASE), "Application won't connect to the given database."
assert len(CRUDS) >= 1, "CRUDs does not mention configurations"
