from os import path

"""
Pick up a configuration from a pool
"""
import configs.hrs as program

OUTPUT = program.output.rstrip("/")
DATABASE = program.database
CUSTOM_TEMPLATE = program.template_custom.rstrip("/")
CRUDS = program.cruds


"""
Manage config data sanity
"""
assert path.isdir(OUTPUT), "Output directory error"
assert path.isdir(CUSTOM_TEMPLATE), "Custom template path does not exist."
assert path.isfile(DATABASE), "Application won't connect to the given database."
assert len(CRUDS) >= 1, "CRUDs does not mention configurations"
