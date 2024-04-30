import boto3

session = boto3.Session(profile_name= 'default')#설정상태를 저장, client 혹은 resource서비스를 생성하기 위한 권한을 부여하기 위해사용
s3= session.resource('s3')#s3에 대한 권한 및 상태를 s3 변수에 저장

for bucket in s3.buckets.all():
    print(bucket.name)



