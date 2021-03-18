from Molecule_Generation import smigen3


from gjf_Generation import gjfgen
import os

import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem 
from multiprocessing.spawn import import_main_path
from multiprocessing import freeze_support
from mordred import Calculator, descriptors

def mdgen(title, smifile, data_path):
    with open(smifile,'r+') as f:
        a = f.readlines()
    smiles = []
    for b in range(len(a)):
        smiles.append(a[b].strip('\n'))

    mols = [Chem.MolFromSmiles(smi) for smi in smiles]

    if __name__ == "__main__":
        freeze_support()

        calc = Calculator(descriptors)
        data = calc.pandas(mols)
        # 需要对dataframe添加名字列，好和γ值对应
        namelist = []
        for i in range(len(mols)):
            namelist.append(title+str(i))
        namedict = {'name':namelist}
        df = pd.DataFrame.from_dict(namedict)
        n = pd.concat([data, df], axis=1)
        n.to_csv(data_path+'/'+title+'md.csv',index=False)
########
title = 'substituted_benzene_orth_'
##########
opt_path = '../opt/'+title
gamma_path = '../gamma/'+title
data_path = '../data/'+title
opt_keywords_sc32041 = '''%nprocshared=24
%mem=32GB
#p opt freq b3lyp/6-31g(d) em=gd3 nosymm
'''
opt_keywords_sc71468 = '''%nprocshared=64
%mem=96GB
#p opt freq b3lyp/6-31g(d) em=gd3 nosymm
'''
if os.path.exists(opt_path)==False:
    os.makedirs(opt_path)
if os.path.exists(gamma_path)==False:
    os.makedirs(gamma_path)
if os.path.exists(data_path)==False:
    os.makedirs(data_path)

#生成分子及smi文件
smifile = smigen3(title, data_path)
###############################


#计算分子描述符
#mdgen(title, smifile, data_path)

# 生成gjf文件
gjfgen(title, smifile,opt_path,keywords=opt_keywords_sc71468)

