import os
from pathlib import Path
import pandas as pd

def getgamma(log_path):

    if type(log_path) is str:
        log_path = Path(log_path)
    #the variable `log_path` is a Path, not a string
    with open('paraguoxiang.txt', 'w+') as para:
        para.write('200\n7\n-4\n7\n')
    outinfo = os.popen('multiwfn '+str(log_path)+' <paraguoxiang.txt')
    gamma_value = float(outinfo.readlines()[138][-16:-1].strip(' '))
    name = log_path.stem
    os.remove('paraguoxiang.txt')
    os.remove('./alpha.txt')
    os.remove('./gamma.txt')
    return name,gamma_value

def getallgamma(gamma_path,data_path,idx_keywords='*.log'):
    if type(gamma_path) is str:
        gamma_path = Path(gamma_path)
    #the variable `gamma_path` is a string, but type of `data_path` is a str
    name_list = []
    magnitude_gamma_list = []
    for gamma_log in Path(gamma_path).rglob(idx_keywords):
        name_list.append(getgamma(gamma_log)[0])
        magnitude_gamma_list.append(getgamma(gamma_log)[1])
    gamma_data = pd.DataFrame({'cindex':name_list,'magnitude_gamma':magnitude_gamma_list})
    gamma_data.to_csv(data_path+'/'+gamma_log.stem+'_gamma.csv')
    return gamma_data

# temp = getallgamma('./gamma','./data',idx_keywords='*mono*.log')
# print(temp)