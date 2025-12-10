

import h5py
import os
import numpy as np
from pathlib import Path


# synthesizer_dir = '/cosma7/data/dp004/dc-payy1/my_files/synthesizer/synthesizer-pipeline/Eagle/L0100N1504/PE/REFERENCE/data/photometry_'

synthesizer_dir = '/cosma7/data/dp004/dc-payy1/my_files/synthesizer-project/recipes/Eagle/L0100N1504/PE/REFERENCE/data/photometry_'

subfind_dir = '/cosma7/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/REFERENCE/data'



snapshot = '003_z008p988'



filename = f'{subfind_dir}/groups_{snapshot}/eagle_subfind_tab_{snapshot}.0.hdf5'

with h5py.File(filename) as hf:

    hf.visit(print)

filename = f'{synthesizer_dir}{snapshot}/eagle_subfind_photometry_{snapshot}.0.hdf5'

with h5py.File(filename) as hf:

    hf.visit(print)

    print(hf['Galaxies/Lines/IDs'])