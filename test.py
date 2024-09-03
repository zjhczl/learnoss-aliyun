# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录RAM控制台创建RAM账号。
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# Endpoint以杭州为例，其它Region请按实际情况填写。
# 填写Bucket名称，例如examplebucket。
bucket = oss2.Bucket(
    auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'breton-oss')

# 填写Object完整路径，完整路径中不包含Bucket名称，例如testfolder/exampleobject.txt。
# 下载Object到本地文件，并保存到指定的本地路径D:\\localpath\\examplefile.txt。如果指定的本地文件存在会覆盖，不存在则新建。
bucket.get_object_to_file('c0319cef-f93e-4d83-aebb-5689e159241f/2ef3778b-b2bc-4955-a1a5-102232ad49e6/DJI_202407051228_006_2ef3778b-b2bc-4955-a1a5-102232ad49e6/DJI_20240705123004_0002_V.jpeg',
                          './1.png')
