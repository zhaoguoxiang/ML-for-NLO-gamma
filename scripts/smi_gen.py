from rdkit import Chem

def smi_paraorienting(data_path):
    #此处生成smiles并去重，标准化
    withdrawing = ['(N(=O)(=O))','(C#N)','(C(=O)(O))','(S(=O)(=O)(O))','(CO)','(C(=O)(C))',]
    donor = ['(N)','(NC)','(N(C)(C))','(O)','(NC(=O)C)','(OC(=O)(C))','(C)','(F)','(Cl)',]

    paraorienting = []
    for group in withdrawing:
        for g in withdrawing:
            paraorienting.append('c1'+group+'ccc'+g+'cc1')
        for f in donor:
            paraorienting.append('c1'+group+'ccc'+f+'cc1')
    for group in donor:
        for g in withdrawing:
            paraorienting.append('c1'+group+'ccc'+g+'cc1')
        for f in donor:
            paraorienting.append('c1'+group+'ccc'+f+'cc1')
    #去重
    mols = [Chem.MolFromSmiles(smi) for smi in paraorienting]
    paraorienting =list(set([Chem.MolToSmiles(mol) for mol in mols]))

    #以下生成smi文件
    smifile = data_path+'/paraorienting.smi'
    with open (smifile,'w') as f:
        f.writelines([line+'\n' for line in paraorienting])

    return paraorienting, smifile

def smi_metasubstitution(data_path):
    withdrawing = ['(N(=O)(=O))','(C#N)','(C(=O)(O))','(S(=O)(=O)(O))','(CO)','(C(=O)(C))',]
    donor = ['(N)','(NC)','(N(C)(C))','(O)','(NC(=O)C)','(OC(=O)(C))','(C)','(F)','(Cl)',]

    # metasubstitution
    metasubstitution = []
    for group in withdrawing:
        for g in withdrawing:
            metasubstitution.append('c1'+group+'cc'+g+'ccc1')
        for f in donor:
            metasubstitution.append('c1'+group+'cc'+f+'ccc1')
    for group in donor:
        for g in withdrawing:
            metasubstitution.append('c1'+group+'cc'+g+'ccc1')
        for f in donor:
            metasubstitution.append('c1'+group+'cc'+f+'ccc1')
    #去重
    mols = [Chem.MolFromSmiles(smi) for smi in metasubstitution]
    metasubstitution =list(set( [Chem.MolToSmiles(mol) for mol in mols]))

    #以下生成smi文件
    smifile = data_path+'/metasubstitution.smi'
    with open (smifile,'w') as f:
        f.writelines([line+'\n' for line in metasubstitution])

    return metasubstitution, smifile

def smi_orthosubstituent(data_path):
    withdrawing = ['(N(=O)(=O))','(C#N)','(C(=O)(O))','(S(=O)(=O)(O))','(CO)','(C(=O)(C))',]
    donor = ['(N)','(NC)','(N(C)(C))','(O)','(NC(=O)C)','(OC(=O)(C))','(C)','(F)','(Cl)',]

    orthosubstituent = []
    for group in withdrawing:
        for g in withdrawing:
            orthosubstituent.append('c1'+group+'c'+g+'cccc1')
        for f in donor:
            orthosubstituent.append('c1'+group+'c'+f+'cccc1')
    for group in donor:
        for g in withdrawing:
            orthosubstituent.append('c1'+group+'c'+g+'cccc1')
        for f in donor:
            orthosubstituent.append('c1'+group+'c'+f+'cccc1')
    #去重
    mols = [Chem.MolFromSmiles(smi) for smi in orthosubstituent]
    orthosubstituent =list(set( [Chem.MolToSmiles(mol) for mol in mols]))

    #以下生成smi文件
    smifile = data_path+'/orthosubstituent.smi'
    with open (smifile,'w') as f:
        f.writelines([line+'\n' for line in orthosubstituent])

    return orthosubstituent, smifile

def smi_monosubstituent(data_path):
    withdrawing = ['(N(=O)(=O))','(C#N)','(C(=O)(O))','(S(=O)(=O)(O))','(CO)','(C(=O)(C))']
    donor = ['(N)','(NC)','(N(C)(C))','(O)','(NC(=O)C)','(OC(=O)(C))','(C)','(F)','(Cl)',]
    # benzene and its monosubstituent
    bnezene = 'c1ccccc1'
    monosubstituent = []
    for group in withdrawing:
        monosubstituent.append(bnezene+group)
    for group in donor:
        monosubstituent.append(bnezene+group)
    #去重
    mols = [Chem.MolFromSmiles(smi) for smi in monosubstituent]
    monosubstituent =list(set( [Chem.MolToSmiles(mol) for mol in mols]))

    #以下生成smi文件
    smifile = data_path+'/monosubstituent.smi'
    with open (smifile,'w') as f:
        f.writelines([line+'\n' for line in monosubstituent])

    return monosubstituent, smifile

# print(smi_paraorienting('./data')[1])
# print(smi_orthosubstituent('./data')[1])
# print(smi_metasubstitution('./data')[1])
# print(smi_monosubstituent('./data')[1])