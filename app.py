import os
import sys
CURPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([CURPATH])
sys.path = list(set(sys.path))
from Core import System
from UI import MainWindow


if __name__ == "__main__":
    pass
