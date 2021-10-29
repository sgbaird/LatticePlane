from os.path import join, exists
from os import chdir, mkdir
from pymatgen.io.cif import CifWriter
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.core.structure import Structure
from pymatgen.ext.matproj import MPRester
import pandas as pd
import pickle

#directory
epdo_dir = '/uufs/chpc.utah.edu/common/home/sparks-thermoelectric/epdo/'
chdir(epdo_dir)
cifdir = join('cif','stable_elastic')
if not exists(cifdir):
    mkdir('cif')
    mkdir(cifdir)

#MPRester
props = ['task_id','cif','elasticity']
with MPRester() as m:
    results = m.query({'e_above_hull': {"$lt": 0.5}, "elasticity": {"$exists": True}}, properties=props) #could replace with get_entries() which would allow getting conventional_cell more directly

#parsing
#separate mpids, stable CIFs, and other properties
mpids = [d['task_id'] for d in results]
stableCIFs = [d['cif'] for d in results]
elasticity = [d['elasticity'] for d in results]
K_VRH = [d['K_VRH'] for d in elasticity]

#pymatgen
nids = len(mpids)
for i in range(nids):
    mpid = mpids[i]
    path = join(cifdir, mpid+'.cif')
    cif = stableCIFs[i]
    structure = Structure.from_str( cif, fmt="cif")
    sga = SpacegroupAnalyzer(structure)
    conventional_structure = sga.get_conventional_standard_structure()
    w = CifWriter( conventional_structure, symprec=0.1 )
    w.write_file( path )

#save the data to various formats
with open('stable_elasticity_CIFs.pkl', 'wb') as f:
    pickle.dump(stableCIFs, f)

df = pd.DataFrame({
    'mp-ids': mpids,
    'K_VRH': K_VRH
})
df.to_csv('stable_elasticity_mp-ids.csv',index=False)
