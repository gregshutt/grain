import os
from importlib.metadata import version
from flask import Blueprint, render_template, redirect
from config import settings, storage

page = Blueprint("page", __name__, template_folder="templates")


@page.get("/image/<path:filename>")
def serve_image(filename):
    client = storage.get_minio_client()
    url = client.presigned_get_object(settings.MINIO_BUCKET, filename)
    return redirect(url)

@page.get("/upload")
def upload_image():
    return render_template("page/upload.html")


@page.get("/")
def home():
    client = storage.get_minio_client()

    items = []
    objects = client.list_objects(bucket_name=settings.MINIO_BUCKET, prefix='dataset/')
    for obj in objects:
        stat = client.stat_object(settings.MINIO_BUCKET, obj.object_name)
        items.append(
            {
                "name": obj.object_name,
                "last_modified": obj.last_modified,
            }
        )

    items.sort(key=lambda x: x["last_modified"], reverse=True)

    context = {"items": items}
    return render_template("page/home.html", **context)
