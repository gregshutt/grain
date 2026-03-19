import os

from distutils.util import strtobool

SECRET_KEY = os.environ["SECRET_KEY"]

SERVER_NAME = os.getenv(
    "SERVER_NAME", "localhost:{0}".format(os.getenv("PORT", "8000"))
)

MINIO_HOST = os.environ["MINIO_HOST"]
MINIO_ACCESS_KEY = os.environ["MINIO_ACCESS_KEY"]
MINIO_SECRET_KEY = os.environ["MINIO_SECRET_KEY"]
MINIO_BUCKET = os.environ["MINIO_BUCKET"]