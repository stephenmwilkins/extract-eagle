

import h5py
import os
import numpy as np
from pathlib import Path


synthesizer_dir = '/cosma7/data/dp004/dc-payy1/my_files/synthesizer/synthesizer-pipeline/Eagle/L0100N1504'
subfind_dir = '/cosma7/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/REFERENCE/data'


snapshots = ['008_z005p037']

lines = ['H 1 6562.80A']


for snapshot in snapshots:

    # determine 

    subfind_snapshot_dir = f'{subfind_dir}/groups_{snapshot}'

    folder = Path(subfind_snapshot_dir)

    # Count only files
    N = sum(1 for f in folder.iterdir() if f.is_file())

    print(f"Number of files: {N}")


    # arr_list = []

    # for i in range(N):

    #     filename = f'{base_data_dir}/photometry_{snapshot}/eagle_subfind_photometry_{snapshot}.{i}.hdf5'

    #     with h5py.File(filename) as hf:

    #         # hf.visit(print)

    #         arr_list.append(hf[f'Lines/intrinsic/{line}/Luminosities'][:])


    # Ha = np.concatenate(arr_list)
    # print(Ha.shape)





