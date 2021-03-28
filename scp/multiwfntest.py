import os
from pathlib import Path

def getgamma(gamma_path):
    #the variable gamma_path is a string
    def mulgamma(file):
        #the variable `file` is a Path, not a string
        with open('paraguoxiang.txt', 'w+') as para:
            para.write('200\n7\n-4\n7\n')
        outinfo = os.popen('multiwfn '+str(file)+' <paraguoxiang.txt')
        gamma_value = float(outinfo.readlines()[138][-16:-1].strip(' '))
        name = file.stem
        os.remove('paraguoxiang.txt')
        os.remove('./alpha.txt')
        os.remove('./gamma.txt')
        return {name:gamma_value}

    logfiles_gamma_path = list(Path(gamma_path).rglob('*.log'))
    gamma_list = [mulgamma(file) for file in logfiles_gamma_path]

    return gamma_list
