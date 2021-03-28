from pathlib import Path

# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt

# from rdkit import Chem
import cclib

logfiles_gamma_path = list(Path('./gamma/Sn2').rglob('*.log'))
logfiles_gamma_name = [filename.stem for filename in logfiles_gamma_path]#this row and the next row can not be changed
logfiles_gamma_str = [str(file) for file in logfiles_gamma_path]
print(logfiles_gamma_str)

def phasedata (logfile):
    data = cclib.io.ccread(logfile)

pass