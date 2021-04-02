from pathlib import Path
import os
import pandas as pd
import numpy as np

def get_dos(fchk_path):
    
    '''

    '''

    if type(fchk_path) is str:
        fchk_path = Path(fchk_path)

    with open('./guoxiangpara.txt', 'w+') as p:
        p.write('10\n2\n-20,4,2\n0\n3\n0\n-10\nq\n')


    doslist = []
    for fchk in fchk_path.rglob('*.fchk'):

        os.system('Multiwfn '+str(fchk)+'<guoxiangpara.txt')

        curve_txt = fchk.stem+'_DOS_curve.txt'

        df = pd.read_csv(str(curve_txt), sep='    ', engine='python', header=None, index_col=None)
        df2 = pd.DataFrame(df.iloc[:,1].T)
        df2['cindex'] = fchk.stem

        doslist.append(df2)


    os.remove('DOS_curve.txt')
    os.remove('DOS_line.txt')
    os.remove('guoxiangpara.txt')

    return doslist

print(get_dos('../gamma/substituted_benzene_meta_'))