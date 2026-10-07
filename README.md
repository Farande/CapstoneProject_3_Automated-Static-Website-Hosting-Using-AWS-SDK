# Automated Static Website Hosting Using AWS SDK

## 1. Project Title and Objective

**Project Title:** Automated Static Website Hosting Using AWS SDK (Python and Boto3)

**Objective:**
This project automates the deployment of a static HTML, CSS and JavaScript website to **Amazon S3** using Python and **boto3**, the AWS SDK for Python. Instead of creating a bucket and uploading files by hand in the AWS Management Console, a single script does the whole job: it creates or identifies the bucket, uploads the complete website folder, detects each file's content type, configures static website hosting, and prints the website endpoint.

The project shows how Python can interact with AWS services to automate common cloud deployment tasks.

### Features

- Creates an S3 bucket if required and checks whether it already exists
- Recursively uploads the complete website folder, including subdirectories
- Supports HTML, CSS, JavaScript and image files
- Detects MIME types automatically
- Configures S3 static website hosting with an index and error document
- Displays the website endpoint after deployment

---

## 2. AWS Services Used

| Service / Tool | Purpose |
|---|---|
| **Amazon S3** | Stores the website files and serves them through static website hosting |
| **AWS IAM** | Grants the deployment identity the S3 permissions it needs |
| **AWS CLI** | Stores credentials and region (`aws configure`) used by boto3 |
| **Boto3 (AWS SDK for Python)** | Automates bucket creation, uploads and website configuration |

**Other technologies:** Python, HTML, CSS, JavaScript, Git, GitHub

---

## 3. Architecture / Workflow

### Architecture

```
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
```

### Deployment Workflow

```
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
```

### Project Structure

```
CapstoneProject_3_Automated-Static-Website-Hosting-Using-AWS-SDK/
│
├── Screenshot/              # Project screenshots
├── automated-s3-website/    # Deployment script and website files
│   ├── deploy.py
│   ├── requirements.txt
│   └── website/
│       ├── index.html
│       ├── style.css
│       ├── app.js
│       └── images/
└── README.md
```

---

## 4. Implementation Steps

1. **Prepare the website** – Create the HTML, CSS, JavaScript and image files inside a `website/` folder.
2. **Set up the environment** – Install Python, the AWS CLI and boto3 (`pip install -r requirements.txt`).
3. **Create an IAM identity** with the S3 permissions listed below, and run `aws configure` with region `ap-south-1`.
4. **Write `deploy.py`:**
   - Define a globally unique `BUCKET_NAME`.
   - Check whether the bucket exists, and create it if it does not.
   - Configure bucket access so the website can be served.
   - Walk the `website/` folder with `os.walk()` so every file in every subdirectory is found.
   - Detect each file's MIME type and upload it with the correct `ContentType`.
   - Configure static website hosting with `index.html` as the index and error document.
   - Print the website endpoint.
5. **Run the script** with `python deploy.py` and read the deployment output.
6. **Verify** the uploaded files in the S3 console, check the hosting configuration, and open the endpoint in a browser.

### Content Type Detection

| File type | Content type |
|---|---|
| HTML | `text/html` |
| CSS | `text/css` |
| JavaScript | `text/javascript` |
| PNG | `image/png` |
| JPG / JPEG | `image/jpeg` |

Correct content types make sure the browser renders pages and styles instead of downloading the files.

### IAM Permissions

```
s3:CreateBucket
s3:ListBucket
s3:PutObject
s3:PutBucketWebsite
s3:PutBucketPolicy
s3:GetBucketWebsite
```

For production, restrict these permissions to the specific bucket (least privilege).

---

## 5. Screenshots

### Automated Deployment Script Output
![Automated Deployment Script Output](Screenshot/Automated%20Deployment%20Script%20Output.png)

### S3 Bucket (Uploaded Website Files)
![S3 Bucket Uploaded Website Files](Screenshot/S3%20Bucket%20%28Uploaded%20Website%20Files%29.png)

### S3 Static Website Hosting Configuration
![S3 Static Website Hosting Configuration](Screenshot/S3%20Static%20Website%20Hosting%20Configuration.png)

### Website Live on the S3 URL
![Landing page on the S3 URL](Screenshot/Capstron%20Cloud%20landing%20page%20on%20the%20S3%20URL.png)

---

## 6. How to Run or Deploy the Project

### Prerequisites

- Python 3.x
- AWS CLI
- An AWS account
- An IAM user or role with Amazon S3 permissions
- Git

```bash
python --version
aws --version
```

### Installation

```bash
git clone https://github.com/Farande/CapstoneProject_3_Automated-Static-Website-Hosting-Using-AWS-SDK.git
cd CapstoneProject_3_Automated-Static-Website-Hosting-Using-AWS-SDK/automated-s3-website
pip install -r requirements.txt
```

`requirements.txt` contains `boto3`.

### AWS Configuration

```bash
aws configure
```

```
AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: ap-south-1
Default output format: json
```

Verify the configuration:

```bash
aws sts get-caller-identity
```

### Set the Bucket Name

Open `deploy.py` and set a **globally unique** bucket name:

```python
BUCKET_NAME = "my-static-website-2026-12345"
```

If the name is already taken, S3 returns an error and you need to pick another one.

### Run the Deployment

```bash
python deploy.py
```

Expected output:

```
====================================
 S3 STATIC WEBSITE DEPLOYMENT
====================================

Bucket already exists: <your-bucket-name>

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

Website Endpoint:
http://<your-bucket-name>.s3-website-ap-south-1.amazonaws.com
```

The exact endpoint depends on the bucket name and region. Open it in a browser to see the site.

### Updating the Website

Edit the files in `website/` and run `python deploy.py` again. The script re-uploads every file and the site is updated.

### Security Notes

- Never put AWS access keys or secret keys in the Python code.
- Do not commit credentials, passwords, private keys or `.env` files.
- Use the AWS CLI configuration, an IAM role or environment variables for credentials.
- S3 website endpoints serve **public** content over HTTP only. Do not upload anything private to this bucket.

Recommended `.gitignore`:

```
__pycache__/
*.pyc
.venv/
venv/
.env
.aws/
```

---

## 7. Key Learnings

- **Infrastructure automation with boto3:** A short Python script can replace many manual console steps and make deployments repeatable.
- **Idempotent scripts:** Checking whether the bucket exists before creating it lets the same script be run again safely.
- **S3 static website hosting:** Hosting needs an index document, an error document and appropriate public read access, and the website endpoint is different from the normal S3 object URL.
- **Content types matter:** Uploading with the correct `ContentType` ensures browsers render HTML and CSS and display images instead of downloading them.
- **Recursive file handling:** `os.walk()` lets the script upload nested folders without listing each file by hand.
- **Global bucket names:** S3 bucket names must be unique across all of AWS.
- **IAM and credentials:** Credentials stay in the AWS CLI configuration, and the identity should have only the S3 permissions it needs.
- **Limits of S3-only hosting:** The website endpoint supports HTTP only, so a production site should add CloudFront for HTTPS and keep the bucket private.

---

