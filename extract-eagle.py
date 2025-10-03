

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

    folder = Path(f'{synthesizer_dir}{snapshot}')

    # Count only files
    N = sum(1 for f in folder.iterdir() if f.is_file())

    print(f"{snapshot} {N}")


    # get quantities

    sfr_list = []
    stellar_mass_list = []
    bh_mass_list = []

    for i in range(N):

        filename = f'{subfind_snapshot_dir}/groups_{snapshot}/eagle_subfind_tab_{snapshot}.{i}.hdf5'

        with h5py.File(filename) as hf:

            bh_mass_list.append(hf['Subhalo/ApertureMeasurements/Mass/030kpc'][:,4])
            stellar_mass_list.append(hf['Subhalo/ApertureMeasurements/Mass/030kpc'][:,3])
            sfr_list.append(hf['Subhalo/ApertureMeasurements/SFR/030kpc'][:])


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
                intrinsic_line_ews_list[line].append(hf[f'Lines/intrinsic/{line}/EWs'][:])
                los_line_ews_list[line].append(hf[f'Lines/intrinsic/{line}/EWs'][:])


    with h5py.File(f'outputs/{snapshot}.h5', 'w') as hf:

        hf[f'mstar'] = np.concatenate(stellar_mass_list)
        hf[f'mbh'] = np.concatenate(bh_mass_list)
        hf[f'sfr'] = np.concatenate(sfr_list)

        for line in lines:

            hf[f'lines/intrinsic/{line}/Luminosities'] = np.concatenate(intrinsic_line_luminosities_list[line])
            hf[f'lines/los/{line}/Luminosities'] = np.concatenate(los_line_luminosities_list[line])

            hf[f'lines/intrinsic/{line}/EWs'] = np.concatenate(intrinsic_line_ews_list[line])
            hf[f'lines/los/{line}/EWs'] = np.concatenate(los_line_ews_list[line])

