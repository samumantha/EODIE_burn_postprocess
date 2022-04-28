# Postprocessing burnt area monitoring results from EODIE

## Process

1. get_overview.py
input: directory with tifs from EODIE (--geotif_out) for burnt area project
output: finalkeepers.txt : list of paths to files to keep (not fully cloudcovered, not unnecesary ids and only from certain tiles)

2. merge_geotiffs.py
input: finalkeepers.txt
output: merged geotiffs files that need to be merged -> prepped

3. merge_prepost.py
input: pre and post burn shapefiles
output: one merged and dissolved shapefile per area

4. test_grid.py (test all dates for grid (transform) consistency)

5. clip.py
input: directory with merged shapefiles from 3, directory with prepped geotiffs from 2
output: directory with cut and prepped geotiffs

6. create_hdf.py
input: directory with prepped and merged geotiffs
output: one hdf file with id as groups and dates as dataset names, dataset is array

read_hdf.py to test read the created hdf


--- 

> gdalwarp -cutline xx.shp -of GTiff -tap -tr 10 10 -crop_to_cutline -dstnodata -99999 in.tif out.tif

---

rasterio_testi.py: check two rasterfiles shape, transform and crs

---

collect_hyytiala.py:

---

collect_hyytiala_allas.py: not used, as boto cannot list all objects