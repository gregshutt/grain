from minio import Minio
from config import settings

def get_minio_client():
  client = Minio(
      settings.MINIO_HOST, 
      access_key = settings.MINIO_ACCESS_KEY, 
      secret_key = settings.MINIO_SECRET_KEY,
      cert_check = False
  )

  return client