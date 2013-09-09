import os
def here(x):
    return os.path.join(os.path.abspath(''), x)#os.path.dirname(__file__)
