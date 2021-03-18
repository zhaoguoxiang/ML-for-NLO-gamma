from initiation import *
import os


title = 'substituted_benzene_orth_'
gammadir = '../gamma/'+title
parameterfile = './parameter/gamma.txt'
data_path = '../data/'+title

gammadict = {}
name = []
val = []
for file in listfiles('.log',gammadir):
    molname = file.split('/')[-1].rstrip('.log')
    command = 'multiwfn '+file+' <'+parameterfile
    outinfo = os.popen(command).readlines()
    gammaval = float(outinfo[138][-16:-1].strip(' '))
    name.append(molname)
    val.append(gammaval)
    gammadict = {'name':name, 'gamma':val}

gammadata = pd.DataFrame.from_dict(gammadict)
gammadata.to_csv(data_path+'/'+title+'gamma.csv', index=False)

os.remove('./alpha.txt')
os.remove('./gamma.txt')