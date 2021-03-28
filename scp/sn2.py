from urllib import request
from openbabel import pybel
from multiprocessing.spawn import import_main_path
from multiprocessing import freeze_support
from mordred import Calculator, descriptors
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem 
import cclib
from pathlib import Path

gammalogs = Path('./gamma/Sn2')
gammafiles = list(gammalogs.rglob('*.log'))

def log2xyz(logfiles):  
    for logfile in logfiles:
        data = cclib.io.ccread(str(logfile))
        data.writexyz(str(logfile).rstrip('.log')+'.xyz')

def xyz2mols(xyzfiles):
    mols = []
    for xyzfile in xyzfiles:
        bel_mol = pybel.readfile('xyz',str(xyzfile)).__next__()
        smi = smi = bel_mol.write('smi').split('\t')[0]
        mol = Chem.MolFromSmiles(smi,sanitize=False)
        mols.append(mol)
    
    return mols
#log2xyz(gammafiles)

xyzfiles = list(gammalogs.rglob('*.xyz'))

mols = xyz2mols(xyzfiles)

if __name__ == "__main__":
    freeze_support()
    calc = Calculator(descriptors)
    data = calc.pandas(mols)

    namelist = []
    for file in gammafiles:
        name = file.stem
        namelist.append(name)
    namedict = {'name':namelist}
    df = pd.DataFrame.from_dict(namedict)
    n = pd.concat([data, df], axis=1)
    print(n)




#         bel_mol = pybel.readfile('xyz',str(logfile)).__next__()
#         

# def mdgen(mols):

#     if __name__ == "__main__":
#         freeze_support()
#         calc = Calculator(descriptors)
#         data = calc.pandas(mols)

#     return data  

# mols=log2mol(gammafiles)
# data = mdgen(mols)

# namelist = []
# for file in gammafiles:
#     name = file.split('\\')[-1].rstrip('.log')
#     namelist.append(name)
# namedict = {'name':namelist}
# df = pd.DataFrame.from_dict(namedict)
# n = pd.concat([data, df], axis=1)
# print(n)