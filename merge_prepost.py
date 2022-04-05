"""

input: pre and post burn shapefiles
output: one merged and dissolved shapefile per area

"""

import geopandas
import pandas
import os

shpdir = '/u/58/wittkes3/unix/Documents/UEF_burnt_area/original_shp_burnt_area'
outdir = '/u/58/wittkes3/unix/Documents/UEF_burnt_area/prepost'

def merge(filename):
    summerfile = filename
    fallfile = filename.replace('summer','fall')
    summerdf = geopandas.read_file(os.path.join(shpdir,summerfile))
    falldf = geopandas.read_file(os.path.join(shpdir,fallfile))
    prepostdf = geopandas.GeoDataFrame(pandas.concat([summerdf, falldf]))
    disdf = prepostdf.dissolve()
    print(disdf)
    outname = filename.replace('summer','prepost')
    disdf.to_file(os.path.join(outdir,outname))

for file in os.listdir(shpdir):
    if file.endswith('.shp'):
        if 'Ahveninen' in file and 'summer' in file:
            merge(file)

        elif 'Pernunmaki' in file and 'summer' in file:
            merge(file)

        elif 'PyhaHakki' in file and 'summer' in file:
            merge(file)
        
        elif 'Seitseminen' in file and 'summer' in file:
            merge(file)




