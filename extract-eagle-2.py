

import h5py
import os
import numpy as np
from pathlib import Path


# synthesizer_dir = '/cosma7/data/dp004/dc-payy1/my_files/synthesizer/synthesizer-pipeline/Eagle/L0100N1504/PE/REFERENCE/data/photometry_'

synthesizer_dir = '/cosma7/data/dp004/dc-payy1/my_files/synthesizer-project/recipes/Eagle/L0100N1504/PE/REFERENCE/data/photometry_'

subfind_dir = '/cosma7/data/Eagle/ScienceRuns/Planck1/L0100N1504/PE/REFERENCE/data'





snapshots = [
    '002_z009p993',
    '003_z008p988',
    '004_z008p075',
    '005_z007p050',
    '006_z005p971',
    # '007_z005p487',
    '008_z005p037',
    # '009_z004p485',
    # '010_z003p984',
    # # '011_z003p528',
    # '012_z003p017',
    # # '013_z002p478',
    # # '014_z002p237',
    # '015_z002p012',
    # # '016_z001p737',
    # '017_z001p487',
    # # '018_z001p259',
    # '019_z001p004',
    # # '020_z000p865',
    # # '021_z000p736',
    # # '022_z000p615',
    # '023_z000p503',
    # # '024_z000p366',
    # # '025_z000p271',
    # # '026_z000p183',
    # # '027_z000p101',
    # '028_z000p000',
    ]


for snapshot in snapshots:

    # determine 

    folder = Path(f'{synthesizer_dir}{snapshot}')

    # Count only files
    N = sum(1 for f in folder.iterdir() if f.is_file())
    print(f"{snapshot} {N}")

    # # get quantities

    # sfr_list = []
    # stellar_mass_list = []
    # bh_mass_list = []

    # for i in range(N):

    #     filename = f'{subfind_dir}/groups_{snapshot}/eagle_subfind_tab_{snapshot}.{i}.hdf5'

    #     with h5py.File(filename) as hf:

    #         bh_mass_list.append(hf['Subhalo/ApertureMeasurements/Mass/030kpc'][:,5])
    #         stellar_mass_list.append(hf['Subhalo/ApertureMeasurements/Mass/030kpc'][:,4])
    #         sfr_list.append(hf['Subhalo/ApertureMeasurements/SFR/030kpc'][:])


    # get lines
    line_luminosities_reprocessed = []
    line_luminosities_total = []
    continuum_reprocessed = []
    continuum_total = []
    stellar_masses = []


    for i in range(N):

        filename = f'{synthesizer_dir}{snapshot}/eagle_subfind_photometry_{snapshot}.{i}.hdf5'

        with h5py.File(filename) as hf:

            if i == 0:
                line_ids = hf['Galaxies/Lines/IDs'][:]
                line_wavelengths = hf['Galaxies/Lines/Wavelengths'][:]

            stellar_masses.append(hf[f'Galaxies/Mstar'][:])
            line_luminosities_reprocessed.append(hf[f'Galaxies/Stars/Lines/Luminosity/stellar_reprocessed'][:])
            line_luminosities_total.append(hf[f'Galaxies/Stars/Lines/Luminosity/stellar_total'][:])
            continuum_reprocessed.append(hf[f'Galaxies/Stars/Lines/Continuum/stellar_reprocessed'][:])
            continuum_total.append(hf[f'Galaxies/Stars/Lines/Continuum/stellar_total'][:])

    # print(line_ids)

    with h5py.File(f'outputs/{snapshot}.h5', 'w') as hf:

        hf[f'mstar'] = np.concatenate(stellar_masses)
        # hf[f'mbh'] = np.concatenate(bh_mass_list)
        # hf[f'sfr'] = np.concatenate(sfr_list)

        hf[f'lines/ids'] = line_ids
        hf[f'lines/Wavelengths'] = line_wavelengths
        hf[f'lines/reprocessed/Luminosities'] = np.concatenate(line_luminosities_reprocessed)
        hf[f'lines/total/Luminosities'] = np.concatenate(line_luminosities_total)
        hf[f'lines/reprocessed/Continuum'] = np.concatenate(continuum_reprocessed)
        hf[f'lines/total/Continuum'] = np.concatenate(continuum_total)


