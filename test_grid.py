import rasterio
import os

prepdir = '/u/58/wittkes3/unix/Documents/EODIE_complete_nbr/tifs/prepped'

idlist = [269,2854,190,214,130]

for id in idlist:
    print(id)
    previous = 'v'
    for file in os.listdir(prepdir):
        idfile = file.split('_')[-1].split('.')[0]
        if id == int(idfile):

            with rasterio.open(os.path.join(prepdir,file)) as f:
                t=  f.transform
                print(t == previous)
                previous = t
