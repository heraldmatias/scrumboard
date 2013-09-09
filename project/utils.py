from os.path import dirname, join, realpath, split

SYSTEM_PATH, PROJECT_DIR = split(realpath(dirname(__file__)))

print(SYSTEM_PATH, PROJECT_DIR)
