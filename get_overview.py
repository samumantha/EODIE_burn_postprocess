
"""

input: directory with tifs from EODIE (--geotif_out) for burnt area project
output: finalkeepers.txt : list of paths to files to keep (not fully cloudcovered, not unnecesary ids and only from certain tiles)

"""

import os
import numpy as np
import rasterio

# this includes fully cloudcovered files 
nbrdir = '/u/58/wittkes3/unix/Documents/EODIE_complete_nbr/tifs'

# all ids
#idlist = [1,2,269,2753,2854,190,214,213,130,131,132]
idlist = [1]

nbrcontent = os.listdir(nbrdir)

#get all tiles per id
idtiledict = {}

for id in idlist:
    tilelist =[]
    for file in nbrcontent:
        fileid = file.split('_')[-1].split('.')[0]
        if str(id) == fileid:
            tile = file.split('_')[2]
            if not tile in tilelist:
                tilelist.append(tile)
    print(id)
    print(tilelist)
    idtiledict[id] = tilelist
print(idtiledict)

# create list with all filepaths of files that are not empty
listtoremove = []
listtokeep = []
all = 0
for file in nbrcontent:
    if file.endswith('.tif'):
        all += 1
        with rasterio.open(os.path.join(nbrdir,file)) as src:
            srcarray = src.read(1)
            unique = np.unique(srcarray)
            # files with less than 3 different values are empty and can be removed
            if len(unique) < 3:
                filetoremove = os.path.join(nbrdir,file)
                listtoremove.append(filetoremove)
            else:
                listtokeep.append(os.path.join(nbrdir,file))
"""
with open('tokeep.txt', 'w') as f:
    for file in listtokeep:
        f.write("%s\n" % file)
"""
print(all)
print(len(listtoremove))


# remove not needed ids, keep only data from certain tiles 
finalkeepers = []
for file in listtokeep:
    id = file.split('_')[-1].split('.')[0]
    if id == '1' and 'VFP' in file:
        finalkeepers.append(file)
    """
    if id != '2753' and id != '2854':
        if idtiledict[int(id)][0] in file:
            # Noora does not need the following, 131 and 132 overlap with 130 and 1 and 2 are evo and hyytiala, ie there was no burn
            if id !='131' and id != '132' and id != '1' and id != '2':
                finalkeepers.append(file)
    else:
        # 2753 and 2854 are located in 3 tiles of which we only want one
        if '35VLG' in file:
            finalkeepers.append(file)
            print(file)
    """        
print(len(finalkeepers))

with open('finalkeepers_hyytiala.txt', 'w') as f:
    for file in finalkeepers:
        f.write("%s\n" % file)



# data info
"""
kohdetunnus = id; name
269 ; Tervalamminsuo -> Pernunmäki
2753 ; Nuuksio -> Ruoholampi
2854; Nuuksio -> Ruoholampi
190; Jäppilä -> Ahveninen
214; Pyhä-Häki
213; Pyhä-Häki
130; Seitseminen
131; Seitseminen
132; Seitseminen

+ Evo (id 2) and Hyytiala (id 1) hand drawn polygons based on plots/tree measurements
EPSG 3067
"""