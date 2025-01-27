import os

def return_app_dir():
    return os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(path=__file__))

BASE_DIR = os.path.dirname(os.path.abspath(return_app_dir()))
