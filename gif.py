
import glob


sorteddates =  ['20200422', '20200505', '20200522', '20200614', '20200616', '20200626', '20200706', '20200716', '20200731', '20200808', '20200818', '20200820', '20200927', '20201002', '20210512', '20210606', '20210704', '20210927']


for atype in ["B08","B8A","B11","ndvi","kndvi"]:
    filenames = []
    for date in sorteddates:
        filename = atype + '_'+ date +'_clip.png'
        filenames.append(filename)
    command = 'convert ' + ' '.join(filenames) +  ' ' + atype + '.gif'
    print(command)

