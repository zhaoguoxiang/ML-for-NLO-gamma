import os
from pathlib import Path

def getgamma(file):
    #the variable `file` is a Path, not a string
    with open('paraguoxiang.txt', 'w+') as para:
        para.write('200\n7\n-4\n7\n')
    outinfo = os.popen('multiwfn '+str(file)+' <paraguoxiang.txt')
    gamma_value = float(outinfo.readlines()[138][-16:-1].strip(' '))
    name = file.stem
    os.remove('paraguoxiang.txt')
    os.remove('./alpha.txt')
    os.remove('./gamma.txt')
    return name,gamma_value

def getallgamma(gamma_path):
    #the variable gamma_path is a string
    name_list = []
    magnitude_gamma_list = []
    for gamma_log in list(Path(gamma_path).rglob('*.log')):
        name_list.append(getgamma(gamma_log)[0])
        magnitude_gamma_list.append(getgamma(gamma_log)[1])
    return {'cindex':name_list,'magnitude_gamma':magnitude_gamma_list}

