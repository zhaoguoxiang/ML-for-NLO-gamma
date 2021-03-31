from pathlib import Path
from rdkit import Chem
from rdkit.Chem import AllChem 

sc32041 = '''%nprocshared=24
%mem=32GB
#p opt freq b3lyp/6-31g(d) em=gd3 nosymm
'''

sc71468 = '''%nprocshared=64
%mem=96GB
#p opt freq b3lyp/6-31g(d) em=gd3 nosymm
'''



def gjf_gen(smi_path, keywords=sc71468, opt_path='./opt'):
    
    if type(smi_path) is str:
        smi_path = Path(smi_path)

    with open (smi_path,'r+') as f:
        smiles = f.readlines()
    for idx, content in enumerate(smiles):
        smiles[idx] = content.strip('\n')
    # for i in range(len(smiles)):
    #     smiles[i] = smiles[i].strip('\n')

    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    mols = [Chem.AddHs(mol) for mol in mols]#TM Chem 函数和AllChem函数不一样，必须得这样写

    for id, mol in enumerate(mols):
        AllChem.EmbedMolecule(mol)
        AllChem.MMFFOptimizeMolecule(mol) 
    
        xyzdata = Chem.MolToXYZBlock(mol)
        
        with open(''.join([opt_path,'/',smi_path.stem,'_',str(id),'.gjf']),'w+') as f:
            f.write(''.join(['%chk=',smi_path.stem,'_',str(id),'.chk\n',keywords,'\n'+smi_path.stem,'_',str(id),'\n\n','0 1\n']))
            f.writelines([line+'\n' for line in xyzdata.split('\n')[2:-1]])
    print('The gjf files has been build successfully!')
#gjf_gen('./data/monosubstituent.smi')


