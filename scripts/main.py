from multiprocessing.spawn import import_main_path
from multiprocessing import freeze_support
from pathlib import Path
from smi_gen import smi_monosubstituent
from md_gen import get_md
from ecfp_gen import get_ecfp
from gjf_gen import gjf_gen
from pathlib import Path

if __name__ == "__main__":
    freeze_support()
    
    
    for smi_path in Path('./data').rglob('*.smi'):
    #smi_path = Path(smi_monosubstituent('./data')[1])
        print(smi_path)
        ecfp = get_ecfp(smi_path,'./data')
        md = get_md(smi_path,'./data')

    #gjf_gen(smi_path)
