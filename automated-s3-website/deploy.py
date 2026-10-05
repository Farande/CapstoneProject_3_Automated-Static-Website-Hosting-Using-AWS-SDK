import boto3
import json
import mimetypes
import os

# -----------------------------
# Configuration
# -----------------------------

REGION = "ap-south-1"
BUCKET_NAME = "automated-static-website-2026-neha"
WEBSITE_FOLDER = "website"
IMAGE_FOLDER = "images"

# -----------------------------
# Create S3 client
# -----------------------------

s3 = boto3.client(
    "s3",
    region_name=REGION,
)


# -----------------------------
# Create bucket
# -----------------------------

def create_bucket():
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket already exists: {BUCKET_NAME}")
    except Exception:
        print(f"Creating bucket: {BUCKET_NAME}")

        create_bucket_config = {}
        if REGION != "us-east-1":
            create_bucket_config["CreateBucketConfiguration"] = {
                "LocationConstraint": REGION
            }

        s3.create_bucket(
            Bucket=BUCKET_NAME,
            **create_bucket_config,
        )

        print("Bucket created successfully.")


def configure_public_access():
    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": False,
            "RestrictPublicBuckets": False,
        },
    )
    print("S3 Block Public Access settings updated.")


def configure_bucket_policy():
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*",
            }
        ],
    }

    s3.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=json.dumps(policy),
    )
    print("Public read bucket policy configured.")


# -----------------------------
# Upload files
# -----------------------------

def upload_directory(directory_path, destination_prefix=""):
    print(f"\nUploading files from: {directory_path}\n")

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(local_path, directory_path)
            s3_key = os.path.join(destination_prefix, relative_path).replace("\\", "/")
            s3_key = s3_key.lstrip("/")

            content_type, _ = mimetypes.guess_type(local_path)
            if content_type is None:
                content_type = "application/octet-stream"

            print(f"Uploading: {s3_key} ({content_type})")

            s3.upload_file(
                local_path,
                BUCKET_NAME,
                s3_key,
                ExtraArgs={"ContentType": content_type},
            )

    print(f"\nAll files uploaded from {directory_path}.")


def upload_website():
    upload_directory(WEBSITE_FOLDER)


def upload_images():
    if os.path.exists(IMAGE_FOLDER):
        upload_directory(IMAGE_FOLDER, IMAGE_FOLDER)


# -----------------------------
# Configure static website
# -----------------------------

def configure_website():
    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            "IndexDocument": {"Suffix": "index.html"},
            "ErrorDocument": {"Key": "index.html"},
        },
    )
    print("Static website hosting configured.")


# -----------------------------
# Main
# -----------------------------

def main():
    print("====================================")
    print(" S3 STATIC WEBSITE DEPLOYMENT")
    print("====================================")

    create_bucket()
    configure_public_access()
    configure_bucket_policy()

    upload_website()
    upload_images()
    configure_website()

    website_endpoint = (
        f"http://{BUCKET_NAME}.s3-website-"
        f"{REGION}.amazonaws.com"
    )

    print("\n====================================")
    print(" DEPLOYMENT COMPLETED")
    print("====================================")

    print(f"Bucket: {BUCKET_NAME}")
    print(f"Website Endpoint: {website_endpoint}")


if __name__ == "__main__":
    main()