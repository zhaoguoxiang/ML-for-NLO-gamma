from pathlib import Path 
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem 
from multiprocessing.spawn import import_main_path
from multiprocessing import freeze_support
from mordred import Calculator, descriptors



def get_md(smi_path, data_path='./'):

    if type(smi_path) is str:
        smi_path = Path(smi_path)

    def get_smi(smi_path):
        smiles = {}
        with open(str(smi_path),'r+') as f:
            lines = f.readlines() 
            smiles = pd.DataFrame({'cindex':[smi_path.stem+'_'+str(idx) for idx, content in enumerate(lines)],
                                    'smiles':[content.strip('\n') for idx, content in enumerate(lines)]})
        return smiles

    smiles = get_smi(smi_path)['smiles']
    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    calc = Calculator(descriptors)
    md = calc.pandas(mols)
    data = pd.concat([md, pd.DataFrame(get_smi(smi_path))], axis=1)
    data.to_csv(data_path+'/'+smi_path.stem+'_md.csv')
    return data

    