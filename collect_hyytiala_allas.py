import boto3

s3 = boto3.client("s3", endpoint_url='https://a3s.fi')
for dataset in datasets:
    for key in s3.list_objects_v2(Bucket='EODIE-Results/2020/tif/'+dataset)['Contents']:
        if (key['Key'].endswith('.tif')):

            filePath = '/vsis3/EODIE-Results/2020/tif/'+ dataset + '/' + key['Key']
            print(filePath)