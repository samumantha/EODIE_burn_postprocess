"""

script to collect all hyytiala data from Puhti

"""

datadirs = ["/scratch/project_2005334/EODIE_process_akivimaki/2020","/scratch/project_2005334/EODIE_process_akivimaki/2021", "/scratch/project_2005334/EODIE_process_forest/EODIE_2021_results"]
startdate = 20200401
enddate = 20210930
tile = '34VFN'
id = '1'
datasets = ["B08","B8A","B11"]

#list all data with needed metadata
oklist = []
for datadir in datadirs:
    for afile in os.listdir(datadir):
        afilesplit = afile.split('_')
        date = afilesplit[1]
        filetile = afilesplit[2]
        fileid = afilesplit[5]
        filedataset = afilesplit[0]
        if fileid == id:
            for dataset in datasets:
                if filedataset == dataset:
                    if date > startdate and date < enddate:
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
