
import boto3


client = boto3.client(
    's3',
    aws_access_key_id='AKyy',
    aws_secret_access_key='Zit',
    region_name='ap-south-1'
)

bucketname = "onlinefiles-list"
destinationbucket = 'online-file-destination-bucket'


def copy_to_destination_bucket(fname):
    response = client.copy_object(Bucket='{}'.format(destinationbucket), CopySource='/{}/{}'.format(bucketname, fname),
                                  Key='{}'.format(fname),
                                  )


def delect_source_bucket(fname):  # deleting the file source bucket
    response = client.delete_object(Bucket='{}'.format(bucketname), Key='{}'.format(fname),
                                    )


def main():
    response = client.list_objects(Bucket='{}'.format(bucketname))
    for file in response['Contents']:
        filename = (file['Key'])
        print("{}".format(filename, destinationbucket))
        copy_to_destination_bucket(filename)
        print("{}".format(filename, bucketname))
        delect_source_bucket(filename)
    print("done")
if __name__=='__main__':
    main()