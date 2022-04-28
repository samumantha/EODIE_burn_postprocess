"""

input: finalkeepers.txt
output: merged geotiffs files that need to be merged 

"""


import os
from rasterio.merge import merge
import rasterio
import shutil

nbrdir = '/u/58/wittkes3/unix/Documents/EODIE_complete_nbr/tifs'

outdir = '/u/58/wittkes3/unix/Documents/EODIE_complete_nbr/tifs/prepped_fixed/'
"""
with open('./finalkeepers.txt') as f:
    lines = f.readlines()
for file in lines:
    file = file.strip()
    name = os.path.split(file)[-1]
    fileid = file.split('_')[-1].split('.')[0]
    print(fileid)
    # copy all files that have not been merged and that are good(non empty)
    if fileid != '213' and fileid != '214' and fileid != '2753' and fileid != '2854':
        shutil.copyfile(file,os.path.join(outdir,name))
"""


# then copy all 'good'  and the merged files to prepped, see above 

def mymerge(one,two):
    with open('./finalkeepers.txt') as f:
        lines = f.readlines()
    for file in lines:
        file = file.strip()
        name = os.path.split(file)[-1]
        fileid = file.split('_')[-1].split('.')[0]
        if fileid == one:
            date = file.split('_')[-5]
            #print(date)
            print('here')
            otherfile = file.replace(one,two).strip()
            print(otherfile)
            if os.path.exists(otherfile):
                print('sec')
                with rasterio.open(file.strip()) as yks:
                    with rasterio.open(otherfile) as kaks:
                        merged, transform = merge([yks,kaks],method= 'max')
                        merged[merged==0] = -99999
                        meta = yks.meta.copy()
                        meta.update({
                            "driver": "GTiff",
                            "height": merged.shape[1],
                            "width": merged.shape[2],
                            "transform": transform,
                        })

                name = os.path.split(file)[-1]
                print(type(nbrdir))
                print(type(name))
                print(type(one))
                print(type(two))
                output_path = os.path.join(nbrdir,'merged_fixed',name.replace(one,'merged_'+ one +'_' + two).strip())
                with rasterio.open(output_path, 'w', **meta) as m:
                    m.write(merged)


mymerge('213','214')
mymerge('2753','2854')