
import os
import boto3
from time import * 
import sys

get_input = sys.argv
print(get_input)

session = boto3.Session(profile_name = "default")
s3 = session.client('s3')

#boto client는 low-levle interface, service description 에 의해 만들어짐
#모든 aws서비스 api 와 1:1매칭
file_name = get_input[1]
local_file_path = os.getcwd() + "/" + file_name
bucketname = 'jiyeonawsbucket'
target_file_name = strftime("%Y", gmtime()) + "/" + strftime("%d", gmtime()) + "/" +file_name

s3.upload_file(file_name, bucketname, target_file_name)

#s3.put_object_acl(ACL = "public-read", Bucket = bucketname, Key = target_file_name)

