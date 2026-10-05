# Automated Static Website Hosting Using AWS SDK

## Project Overview

This project automates the deployment of a static HTML, CSS, and JavaScript website to Amazon S3 using Python and boto3.

Instead of manually creating an S3 bucket and uploading website files through the AWS Management Console, the Python script automates the deployment process.

The script can create or identify an S3 bucket, upload the complete website folder, automatically detect file content types, configure static website hosting, and display the website endpoint.

## Objective

The main objective of this project is to automate static website deployment to Amazon S3 using the AWS SDK for Python.

The project demonstrates how Python can be used to interact with AWS services and automate common cloud deployment tasks.

## AWS Services and Technologies

* Amazon S3
* Python
* boto3
* HTML
* CSS
* JavaScript
* AWS CLI
* Git
* GitHub

## Architecture


Developer
    |
    v
Website Folder
    |
    | Python + boto3
    v
Amazon S3 Bucket
    |
    | Static Website Hosting
    v
Website Endpoint
    |
    v
Web Browser


## Project Structure

automated-static-website-s3/
|
├── deploy.py
├── requirements.txt
├── .gitignore
├── README.md
|
└── website/
    ├── index.html
    ├── style.css
    ├── app.js
    |
    └── images/
        └── logo.png


## Features

* Automatically creates an S3 bucket if required
* Checks whether the bucket already exists
* Uploads the complete website folder
* Supports HTML, CSS, JavaScript, and image files
* Recursively uploads files from subdirectories
* Automatically detects MIME types
* Configures S3 static website hosting
* Configures the website index document
* Configures the error document
* Displays the website endpoint after deployment

## How the Project Works

The deployment process follows these steps:


1. Run the Python deployment script
             |
             v
2. Connect to AWS using boto3
             |
             v
3. Create or identify the S3 bucket
             |
             v
4. Configure bucket access
             |
             v
5. Scan the website folder
             |
             v
6. Detect file content types
             |
             v
7. Upload website files to S3
             |
             v
8. Configure static website hosting
             |
             v
9. Display the website endpoint


## Prerequisites

Before running the project, install the following:

* Python 3.x
* AWS CLI
* An AWS account
* An IAM user or role with appropriate Amazon S3 permissions
* Git

Check the Python installation:


python --version


Check the AWS CLI installation:


aws --version


## Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/automated-static-website-s3.git


Move into the project directory:


cd automated-static-website-s3


Install the required Python package:


pip install -r requirements.txt


## AWS Configuration

Configure AWS CLI using:


aws configure


Provide your AWS credentials and region:


AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: ap-south-1
Default output format: json


The project uses the `ap-south-1` AWS region.

Do not store AWS access keys or secret keys directly inside the Python source code.

## S3 Bucket Configuration

The bucket name is defined in `deploy.py`.

Example:


BUCKET_NAME = "automated-static-website-2026-neha"


S3 bucket names must be globally unique.

If the bucket name is already in use, change it to another unique name.

For example:


BUCKET_NAME = "my-static-website-2026-12345"


## Website Files

The website files are stored inside the `website` directory.

Example:


website/
|
├── index.html
├── style.css
├── app.js
|
└── images/
    ├── logo.png
    ├── banner.jpg
    └── photo.jpeg


The deployment script automatically scans this directory and uploads all files.

## Automatic File Upload

The project uses Python's `os.walk()` function to recursively scan the website directory.

Example:


for root, directories, files in os.walk(WEBSITE_FOLDER):


This allows the script to upload files from nested directories without manually specifying each file.

For example:


website/
├── index.html
├── style.css
├── app.js
├── images/
│   ├── logo.png
│   └── banner.jpg
└── css/
    └── responsive.css


All files will be uploaded automatically.

## Content Type Detection

The script automatically determines the MIME type of each file.

Examples:

| File Type  | Content Type    |
| ---------- | --------------- |
| HTML       | text/html       |
| CSS        | text/css        |
| JavaScript | text/javascript |
| PNG        | image/png       |
| JPG        | image/jpeg      |
| JPEG       | image/jpeg      |

This ensures that files are served correctly by the S3 website endpoint.

## Static Website Hosting

The script configures S3 static website hosting with:


Index Document: index.html
Error Document: index.html

After deployment, the script displays the website endpoint.

Example:


http://your-bucket-name.s3-website-ap-south-1.amazonaws.com


The exact endpoint depends on the S3 bucket name and AWS region.

## Running the Project

Run the deployment script from the project directory:


python deploy.py


The script will automatically:


Create or identify the S3 bucket
        |
        v
Configure bucket access
        |
        v
Scan the website folder
        |
        v
Detect content types
        |
        v
Upload website files
        |
        v
Configure static website hosting
        |
        v
Display the website endpoint


## Expected Output

Example output:


====================================
 S3 STATIC WEBSITE DEPLOYMENT
====================================

Bucket already exists: automated-static-website-2026-neha

Uploading website files...

Uploading: index.html (text/html)
Uploading: style.css (text/css)
Uploading: app.js (text/javascript)
Uploading: images/logo.png (image/png)

All website files uploaded.

Static website hosting configured.

====================================
 DEPLOYMENT COMPLETED
====================================

Bucket: automated-static-website-2026-neha

Website Endpoint:
http://automated-static-website-2026-neha.s3-website-ap-south-1.amazonaws.com


## IAM Permissions

The AWS identity used by the script requires appropriate permissions to perform S3 operations.

Typical permissions include:


s3:CreateBucket
s3:ListBucket
s3:PutObject
s3:PutBucketWebsite
s3:PutBucketPolicy
s3:GetBucketWebsite


For production environments, permissions should be restricted according to the principle of least privilege.

## Security Considerations

AWS credentials should never be stored directly in the source code.

Do not commit files containing:


AWS Access Key
AWS Secret Access Key
Passwords
Private Keys


Use AWS CLI configuration, IAM roles, environment variables, or another secure credential management method.

The project includes a `.gitignore` file to help prevent sensitive files from being committed accidentally.

## requirements.txt

The project requires boto3.


boto3


Install it using:


pip install -r requirements.txt


## .gitignore

Example `.gitignore`:


__pycache__/
*.pyc
.venv/
venv/
.env
.aws/


## Screenshots

The following screenshots can be added to the GitHub repository to demonstrate the project:

1. Project folder structure
2. Python deployment script
3. AWS S3 bucket
4. Uploaded website files in S3
5. S3 static website hosting configuration
6. S3 bucket permissions
7. Python deployment output
8. Running website in the browser
9. AWS S3 bucket properties

Screenshots can be stored in a separate directory:



 s3-bucket
 <img width="1366" height="768" alt="Screenshot (721)" src="https://github.com/user-attachments/assets/248b2ed7-7e10-44f1-98bb-9b71dda17da1" />


uploaded-files.png

<img width="1366" height="768" alt="Screenshot (719)" src="https://github.com/user-attachments/assets/ce42cc67-4128-4e5b-ad6c-900024e6ac6d" />

 
 deployment-output.png
 <img width="1366" height="768" alt="Screenshot (718)" src="https://github.com/user-attachments/assets/7821bf7b-e7a8-4514-970d-d0357f9a0b1b" />

 running-website.png
 <img width="1366" height="768" alt="Screenshot (720)" src="https://github.com/user-attachments/assets/232bb72c-a2bc-4b9a-9138-8f401dce2fd7" />




The project provides practical experience with Python, AWS S3, boto3, IAM, AWS CLI, Git, and GitHub.
