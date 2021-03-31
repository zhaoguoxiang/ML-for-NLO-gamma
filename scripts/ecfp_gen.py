from os import name
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys
import pandas as pd
from pathlib import Path


def get_ecfp(smi_path,data_path='./',):

    if type(smi_path) is str:
        smi_path = Path(smi_path)

    def get_smi(smifile):
        smiles = {}
        with open(str(smifile),'r+') as f:
            lines = f.readlines() 
            smiles = pd.DataFrame({'cindex':[smifile.stem+'_'+str(idx) for idx, content in enumerate(lines)],
                                    'smiles':[content.strip('\n') for idx, content in enumerate(lines)]})
        return smiles

    smiles = get_smi(smi_path)['smiles']

    mols = [Chem.MolFromSmiles(smi) for smi in smiles]

    fingerprints = [MACCSkeys.GenMACCSKeys(molecule) for molecule in mols]
    fingerprints_bit = [list(fp.ToBitString()) for fp in fingerprints]
    fingerprints_df = pd.DataFrame(fingerprints_bit)

    data = pd.concat([fingerprints_df, get_smi(smi_path)], axis=1)
    data.to_csv(data_path+'/'+smi_path.stem+'_fp.csv')

    return data

