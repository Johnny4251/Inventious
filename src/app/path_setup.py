import Utils
import os
import sys

# Assert project src directory to python path
try:
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.dirname(curr_dir)
    sys.path.append(src_dir)
    if Utils.DEBUG_MODE: print("SYS-PATH APPENDED:", src_dir)
except Exception as e:
    print("FOUND EXCEPTION DURING PATH ASSERTION:", e)
    print("exiting...")
    exit(1)