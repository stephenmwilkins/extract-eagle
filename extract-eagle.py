

import h5py
import os
import numpy as np
from pathlib import Path


synthesizer_dir = '/cosma7/data/dp004/dc-payy1/my_files/synthesizer/synthesizer-pipeline/Eagle/L0100N1504/PE/REFERENCE/data/photometry_'
subfind_dir = '/cosma7/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/REFERENCE/data'


snapshots = ['008_z005p037']

lines = ['H 1 6562.80A', 'H 1 4861.32A', 'H 1 1.87510m']


for snapshot in snapshots:

    # determine 

    subfind_snapshot_dir = f'{subfind_dir}/groups_{snapshot}'

    folder = Path(subfind_snapshot_dir)

    # Count only files
    N = sum(1 for f in folder.iterdir() if f.is_file())

    print(f"Number of files: {N}")

    # get lines
    intrinsic_line_luminosities_list = {line: [] for line in lines}
    los_line_luminosities_list = {line: [] for line in lines}
    intrinsic_line_ews_list = {line: [] for line in lines}
    los_line_ews_list = {line: [] for line in lines}

    for i in range(N):

        filename = f'{synthesizer_dir}{snapshot}/eagle_subfind_photometry_{snapshot}.{i}.hdf5'

        with h5py.File(filename) as hf:

            for line in lines:
                intrinsic_line_luminosities_list[line].append(hf[f'Lines/intrinsic/{line}/Luminosities'][:])
                los_line_luminosities_list[line].append(hf[f'Lines/intrinsic/{line}/Luminosities'][:])
                intrinsic_line_ews_list[line].append(hf[f'Lines/intrinsic/{line}/EW'][:])
                los_line_ews_list[line].append(hf[f'Lines/intrinsic/{line}/EW'][:])

    intrinsic_line_luminosities = {}
    los_line_luminosities = {}
    intrinsic_line_ews = {}
    los_line_ews = {}

    for line in lines:
        intrinsic_line_luminosities[line] = np.concatenate(intrinsic_line_luminosities_list[list])
        los_line_luminosities[line] = np.concatenate(los_line_luminosities_list[list])
        intrinsic_line_ews[line] = np.concatenate(intrinsic_line_ews_list[list])
        los_line_ews[line] = np.concatenate(los_line_ews_list[list])

    print(los_line_ews[line].shape)



