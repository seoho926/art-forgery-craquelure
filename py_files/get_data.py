"""Module with function for importing and unzipping data file from AWS s3 bucket"""
import zipfile
import boto3
import os

def get_zipfile(bucket_name, file_name, dl_name):
    """Downloading zipfile from s3 bucket to repo"""
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_name, dl_name)

def unzip(file_name):
    """Unzipping zipfile to data folder"""
    dest = os.path.dirname("data/Cracks")
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(dest)