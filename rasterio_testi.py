import rasterio

#onefile = "/u/58/wittkes3/unix/Downloads/test6.tif"
onefile  ="/u/58/wittkes3/unix/Documents/UEF_burnt_area/prepost_tifs_nd_fixed/nbr_20210608_35VNK_array_id_190_prepost_fixed.tif"
#otherfile = "/u/58/wittkes3/unix/Downloads/200406_100502_R_georef_TESTE.tiff"
otherfile = "/u/58/wittkes3/unix/Downloads/ahveninen_1_p99_repr.tif"

with rasterio.open(onefile) as yks:
    with rasterio.open(otherfile) as kaks:
        eka = yks.read(1)
        kako = kaks.read(1)

        print(yks.crs)
        print(yks.transform)
        print(yks.bounds)

        print(kaks.crs)
        print(kaks.transform)
        print(kaks.bounds)


        print(eka.shape)
        print(kako.shape)

