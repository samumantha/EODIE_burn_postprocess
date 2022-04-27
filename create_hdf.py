"""

input: directory with prepped and merged geotiffs
output: one hdf file with id as groups and dates as dataset names, dataset is array

"""

import numpy as np
import h5py
import rasterio
import os
import glob

#fulldir = '/u/58/wittkes3/unix/Documents/EODIE_complete_nbr/tifs/prepped'
fulldir = '/u/58/wittkes3/unix/Documents/UEF_burnt_area/prepost_tifs_nd_fixed'

idlist = [269,2854,190,214,130]


# to remove \n from filename ins zsh: autoload zmv, and then  zmv -v $'(**/)(*[\n\u2029]*)(#qD)' $'$1${2//[\u2029\n]}'

for mf in glob.glob(fulldir + '/*'):
    print(mf)
    #id = mf.split('_')[-1].split('.')[0]
    id = mf.split('_')[-3]
    name = os.path.split(mf)[-1]
    date = name.split('_')[1]
    print(date)
    with rasterio.open(mf) as src:
        srcarray = src.read(1)


    with h5py.File('burnt_area_clipped_nd_fixed.h5', 'a') as hf:
        print(list(hf.keys()))
        if not str(id) in hf.keys():
            print('a')
            idgrp = hf.create_group(str(id))
            print(idgrp)
        else:
            idgrp = hf[str(id)]
        print(idgrp)

        idgrp.create_dataset(date, data=srcarray)
