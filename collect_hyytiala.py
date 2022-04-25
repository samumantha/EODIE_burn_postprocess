"""

script to collect all hyytiala data from Puhti

"""

import os 
import rasterio


datadirs = ["/scratch/project_2005334/EODIE_process_akivimaki/Results/2020/tif","/scratch/project_2005334/EODIE_process_akivimaki/Results/2021/tif", "/scratch/project_2005334/EODIE_process_forest/EODIE_2021_results/tif"]
startdate = 20200401
enddate = 20210930
tile = '34VFN'
id = '1'
datasets = ["B08","B8A","B11"]

#list all data with needed metadata
oklist = []
for datadir in datadirs:
    print(datadir)
    for afile in os.listdir(datadir):
        print(afile)
        if afile.endswith('.tif'):
            print(afile)
            afilesplit = afile.split('_')
            date = afilesplit[1]
            filetile = afilesplit[2]
            fileid = afilesplit[5]
            filedataset = afilesplit[0]
            if fileid == id:
                print('id')
                if filedataset in datasets:
                    print('dataset')
                    if date > startdate and date < enddate:
                        print(date)
                        afilepath = os.path.join(datadir,afile)
                        if not afilepath in oklist:
                            oklist.append(afilepath)

print(len(oklist))

# get all data with content

listtokeep = []
for okfile in oklist:
    with rasterio.open(okfile) as src:
        srcarray = src.read(1)
        unique = np.unique(srcarray)
        # files with less than 3 different values are empty and can be removed
        if len(unique) > 3:
            listtokeep.append(os.path.join(nbrdir,file))

print(len(listtokeep))

with open('finalkeepers_hyytiala_all.txt', 'w') as f:
    for yeafile in listtokeep:
        f.write("%s\n" % yeafile)



