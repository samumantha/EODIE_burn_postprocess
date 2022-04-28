 
import rasterio
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

lims = {'kndvi': [0,1], 'ndvi': [0,1], 'B08':[0,0.5], 'B8A': [0,0.3], 'B11': [0,0.3]}

for afile in glob.glob('./*.tif'):
    thetype = os.path.split(afile)[-1].split('_')[0]
    date = os.path.split(afile)[-1].split('_')[1]
    with rasterio.open(afile.strip()) as af:
        ar = af.read(1) 
        ar[(ar < -1) | (ar > 1)] = np.nan
        print(np.nanmin(ar))
        print(np.nanmax(ar))
        plt.imshow(ar)
        plt.colorbar()
        plt.title(date)
        plt.clim(lims[thetype][0], lims[thetype][1])
        plt.savefig(thetype + '_' + date + '_clip.png')
        plt.clf()