import os
from importlib.metadata import version
from flask import Blueprint, render_template
from config import settings, storage

page = Blueprint("page", __name__, template_folder="templates")

@page.get("/")
def home():
    # load up all the images
    client = storage.get_minio_client()

    objects = client.list_objects(bucket_name=settings.MINIO_BUCKET)
    for obj in objects:
        print(obj)

    context = {

    }
    return render_template(
        "page/home.html", **context
    )