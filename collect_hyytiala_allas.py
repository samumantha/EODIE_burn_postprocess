import boto3


datasets = ["B08","B8A","B11","ndvi","kndvi"]

s3 = boto3.client("s3", endpoint_url='https://a3s.fi')

print(s3.list_objects_v2(Bucket='EODIE-Results'))

for key in s3.list_objects_v2(Bucket='EODIE-Results')['Contents']:
    print(key)
    if (key['Key'].endswith('.tif')):
        #print(key)
        filename = key['Key']
        print(filename)
        filenamesplit = filename.split('/')
        if filenamesplit[0] == '2020':
            print('one')
            if filenamesplit[2] in datasets:
                print('two')
                if int(filenamesplit[-1].split('_')[1]) > 20200401:
                    print('three')
                    if 'id_1.' in filename:
                        filePath = '/vsis3/EODIE-Results/'+filename
                        print(filePath)
