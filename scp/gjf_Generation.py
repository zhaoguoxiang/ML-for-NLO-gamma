import os
from rdkit import Chem 
from rdkit.Chem import AllChem 


def gjfgen(title, smifile, opt_path, keywords):
    sc32041 = '''%nprocshared=24
%mem=32GB
#p opt freq b3lyp/6-31g(d) em=gd3 nosymm
'''

    sc71468 = '''%nprocshared=64
%mem=96GB
#p opt freq b3lyp/6-31g(d) em=gd3 nosymm
'''
    with open (smifile,'r+') as f:
        smiles = f.readlines()
    for i in range(len(smiles)):
        smiles[i] = smiles[i].strip('\n')

    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    mols = [Chem.AddHs(mol) for mol in mols]#TM Chem 函数和AllChem函数不一样，必须得这样写

    for mol in mols:
        AllChem.EmbedMolecule(mol)
        AllChem.MMFFOptimizeMolecule(mol) 

    for i in range(len(mols)):
        with open(opt_path+'/'+title+str(i)+'.gjf', 'w') as f:
            f.write('%chk='+title+str(i)+'.chk\n'+keywords+'\n'+title+str(i)+'\n\n'+'0 1\n')
            for atom in mols[i].GetAtoms():
                idx = atom.GetIdx()
                x = mols[i].GetConformer(0).GetAtomPosition(idx).x
                if x>=0:
                    x = ' '+str(x)
                else:
                    x = str(x)
                x = x[0:10]
                y = mols[i].GetConformer(0).GetAtomPosition(idx).y
                if y>=0:
                    y = ' '+str(y)
                else:
                    y = str(y)
                y = y[0:10]
                z = mols[i].GetConformer(0).GetAtomPosition(idx).z
                if z>=0:
                    z = ' '+str(z)
                else:
                    z = str(z)
                z = z[0:10]
                f.write(' '+atom.GetSymbol()+'                '+x+'   '+y+'   '+z+'\n')
            f.write('\n\n')  
    if keywords==sc32041:
        head = '''#!/bin/bash
#SBATCH -p v3_64
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 24
export g16ROOT=/public1/home/sc32041/soft/g16
export PATH=$g16ROOT:$PATH
source $g16ROOT/bsd/g16.profile
export GAUSS_SCRDIR=/public1/home/sc32041/soft/g16/tmp
export GAUSS_EXEDIR=$g16ROOT
'''

        with open(opt_path+'/opt-'+title+'.sh', 'w') as f:
            f.write(head)
            for i in range(len(mols)):
                f.write('srun -c 24 g16 '+title+str(i)+'.gjf\n')
                f.write('formchk '+title+str(i)+'.chk\n')
    elif keywords==sc71468:
        head = '''#!/bin/bash
#SBATCH -p amd_256
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 64
#SBATCH -o %J.out
#SBATCH -e %J.err
export PGI_FASTMATH_CPU=sandybridge
export g16ROOT=/public3/home/sc71468/test/gaussian/g16
export PATH=$g16ROOT:$PATH
source $g16ROOT/bsd/g16.profile
export GAUSS_SCRDIR=/public3/home/sc71468/test/gaussian/tmp
export GAUSS_EXEDIR=$g16ROOT
'''
        with open(opt_path+'/opt-'+title+'.sh', 'w') as f:
            f.write(head)
            for i in range(len(mols)):
                f.write('g16 '+title+str(i)+'.gjf\n')
                f.write('formchk '+title+str(i)+'.chk\n')
    else:
        pass