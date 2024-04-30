
import os
import boto3
import time

session = boto3.Session(profile_name = "default")
s3 = session.client('s3')

#boto client는 low-levle interface, service description 에 의해 만들어짐
#모든 aws서비스 api 와 1:1매칭
file_name = "2.jpg"
local_file_path = os.getcwd() + "/" + file_name
bucketname = 'jiyeonawsbucket'
target_file_name = "temp_2.jpg"

#s3.upload_file(local_file_path, bucketname, target_file_name)

s3.put_object_acl(ACL = "public-read", Bucket = bucketname, Key = target_file_name)

