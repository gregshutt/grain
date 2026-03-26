import os
import uuid
from flask import Blueprint, request, redirect, url_for, flash
from config import settings, storage

up = Blueprint("up", __name__, template_folder="templates", url_prefix="/up")


@up.get("/")
def index():
    return redirect(url_for("page.home"))


@up.post("/upload")
def upload():
    if "image" not in request.files:
        flash("No image provided")
        return redirect(url_for("page.home"))

    file = request.files["image"]
    text = request.form.get("text", "")

    if file.filename == "":
        flash("No image selected")
        return redirect(url_for("page.home"))

    if file:
        ext = os.path.splitext(file.filename)[1].lower()
        filename = f"{uuid.uuid4()}{ext}"

        client = storage.get_minio_client()

        client.put_object(
            bucket_name=settings.MINIO_BUCKET,
            object_name=filename,
            data=file,
            length=-1,
            part_size=5 * 1024 * 1024,
            metadata={"text": text},
        )

        flash("Upload successful")

    return redirect(url_for("page.home"))
