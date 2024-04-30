
import os
import boto3
import time

session = boto3.Session(profile_name = "default")
s3 = session.client('s3')

#boto client는 low-levle interface, service description 에 의해 만들어짐
#모든 aws서비스 api 와 1:1매칭


s3.download_file('jiyeonawsbucket', os.path.basename('2.jpg'), "./"+os.path.basename("2.jpg"))
