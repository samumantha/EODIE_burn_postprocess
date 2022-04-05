"""

input: directory with merged shapefiles, directory with prepped geotiffs
output: directory with cut and prepped geotiffs

"""


import glob
import rasterio.mask
import rasterio
import fiona
import geopandas
import os




iddict = {'214':'PyhaHakki','269':'Pernunmaki','190':'Ahveninen', '2854':'Ruoholampi','130':'Seitseminen'}
shpdir = '/u/58/wittkes3/unix/Documents/UEF_burnt_area/prepost'
outdir = '/u/58/wittkes3/unix/Documents/UEF_burnt_area/prepost_tifs_nd'
indir = '/u/58/wittkes3/unix/Documents/EODIE_complete_nbr/tifs/prepped'


for file in glob.glob(indir+'/*'):
    id = file.split('.')[0].split('_')[-1]
    name = iddict[id]
    print(name)
    # id 130 has different epsg than others
    if id == '130':
        epsgc = 32634
    else:
        epsgc = 32635
    shpname = glob.glob(shpdir + '/*' + name +'*.shp')[0]
    data = geopandas.read_file(shpname)
    data = data.to_crs(epsg=epsgc)
    newname = shpname.split('.')[0]+ 'repr_32635'+ shpname.split('.')[-1]
    data.to_file(newname)
    with fiona.open(newname, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]
    with rasterio.open(file) as src:
        # cut full burnt area tifs with merged and reprojected shapefile
        out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True, nodata=-99999)
        out_meta = src.meta
        out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})
    newname = os.path.join(outdir, file.split('/')[-1].split('.')[0] + '_prepost.' + file.split('.')[-1])
    with rasterio.open(newname, "w", **out_meta) as dest:
        dest.write(out_image)


    