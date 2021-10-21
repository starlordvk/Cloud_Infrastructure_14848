import boto3
import csv

s3 = boto3.resource('s3',
                    aws_access_key_id = 'AKIAUE2HQJLIQSADFCWP',
                    aws_secret_access_key = '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')

# try:
#     bucket = s3.Bucket("varunhw3bucket")
#     bucket.Acl().put(ACL='public-read')
#     body = open('exp1.csv', 'rb')
#     o = s3.Object('varunhw3bucket', 'exp1').put(Body=body)
#     s3.Object('varunhw3bucket', 'exp1').Acl().put(ACL='public-read')

#     body = open('exp2.csv', 'rb')
#     o = s3.Object('varunhw3bucket', 'exp2').put(Body=body)
#     s3.Object('varunhw3bucket', 'exp2').Acl().put(ACL='public-read')

#     body = open('exp3.csv', 'rb')
#     o = s3.Object('varunhw3bucket', 'exp3').put(Body=body)
#     s3.Object('varunhw3bucket', 'exp3').Acl().put(ACL='public-read')

# except Exception as e:
#     print(e)


dyndb = boto3.resource('dynamodb',
                        region_name='us-west-2',
                        aws_access_key_id='AKIAUE2HQJLIQSADFCWP',
                        aws_secret_access_key='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'
                        )
                        
try:
    table = dyndb.create_table(
    TableName='DataTable',
    KeySchema=[
    {
    'AttributeName': 'PartitionKey',
    'KeyType': 'HASH'
    },
    {
    'AttributeName': 'RowKey',
    'KeyType': 'RANGE'
    }
    ],
    AttributeDefinitions=[
    {
    'AttributeName': 'PartitionKey',
    'AttributeType': 'S'
    },
    {
    'AttributeName': 'RowKey',
    'AttributeType': 'S'
    },
    ],
    ProvisionedThroughput={
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
    }
    )
except Exception as e:
    print (e)
    #if there is an exception, the table may already exist. if so...
    table = dyndb.Table("DataTable")
    #wait for the table to be created
    table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')
    print(table.item_count)


with open('experiments.csv') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
    item = next(csvf)
    for item in csvf:
        print(item)
        body = open(item[4], 'rb')
        s3.Object('varunhw3bucket', item[4]).put(Body=body )
        md = s3.Object('varunhw3bucket', item[4]).Acl().put(ACL='public-read')

        url = " https://s3-us-west-2.amazonaws.com/varunhw3bucket/"+item[4]
        metadata_item = {'PartitionKey': item[0], 'RowKey': item[1],
        'description' : item[4], 'date' : item[2], 'url':url}
        try:
            table.put_item(Item=metadata_item)
        except:
            print("item may already be there or another failure")

response = table.get_item(Key={'PartitionKey': '1','RowKey': '-1'})
item = response["Item"]
print(item)

response = table.get_item(Key={'PartitionKey': '2','RowKey': '-2'})
item = response["Item"]
print(item)

response = table.get_item(Key={'PartitionKey': '3','RowKey': '-2.93'})
item = response["Item"]
print(item)






