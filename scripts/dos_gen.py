from pathlib import Path
import os
import pandas as pd


def get_dos(fchk_path):
    
    '''
    TODO: need a better way to name the csv file
    '''

    if type(fchk_path) is str:
        fchk_path = Path(fchk_path)

    with open('./guoxiangpara.txt', 'w+') as p:
        p.write('10\n2\n-20,4,2\n0\n3\n0\n-10\nq\n')


    doslist = []
    for fchk in fchk_path.rglob('*.fchk'):
        print(str(fchk))
        os.system('Multiwfn '+str(fchk)+'<guoxiangpara.txt')


        df = pd.read_csv('DOS_curve.txt', sep='    ', engine='python', header=None, index_col=None)
        df2 = pd.DataFrame(df.iloc[:,1]).T
        df2['cindex'] = fchk.stem

        doslist.append(df2)

    df3 = pd.concat(doslist,join='inner', ignore_index=True)
    df3.to_csv('../data/substituted_benzene_para_dos.csv')

    os.remove('DOS_curve.txt')
    os.remove('DOS_line.txt')
    os.remove('guoxiangpara.txt')

    return doslist

print(get_dos('../gamma/substituted_benzene_para_'))