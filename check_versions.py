import sys
import torch
import cv2
import numpy as np
import matplotlib
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR


python_version = sys.version

pyTorch_version = torch.__version__
cv_version = cv2.__version__
np_version = np.__version__
matplotlib_version = matplotlib.__version__

print("YOUR PYTHON VERSIONS:")
print("==============")
print("Python Version:", python_version)
print("PyTorch Version:", pyTorch_version)
print("OpenCV version:", cv_version)
print("Numpy Version:", np_version)
print("Matplotlib Version:", matplotlib_version)
print("PyQt:", PYQT_VERSION_STR)
print("Qt:", QT_VERSION_STR)
print("==============")