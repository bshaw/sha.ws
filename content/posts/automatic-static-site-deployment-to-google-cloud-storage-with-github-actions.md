+++
title = 'Automatic upload to Google Cloud Storage with GitHub Actions'
date = '2020-06-24T10:51:00+00:00'
tags = ['cloud', 'devops', 'automation', 'gcp']
categories = ['Cloud']
slug = 'automatic-upload-to-google-cloud-storage-with-github-actions'
description = 'GitHub Actions workflow example for automated upload to Google Cloud Storage'
published = true
aliases = ['/automatic-upload-to-google-cloud-storage-with-github-actions.html']
+++

## Overview

[GitHub Actions](https://github.com/features/actions) enable simple workflow automation and CI/CD right from GitHub repos.

Uploading your content, whether a static website or any other artifact can be easily managed with an Actions workflow.

This article walks through everything required to successfully set up your workflow.

The examples are based on the _this_ static website ([sha.ws](https://sha.ws)), which is uploaded to Google Cloud Storage for hosting.
The workflow is available in the git repo for the site: [https://github.com/bshaw/sha.ws/blob/master/.github/workflows/google-cloud-storage.yml](https://github.com/bshaw/sha.ws/blob/master/.github/workflows/google-cloud-storage.yml)

__Note:__ _Most_ of these instructions use the GCP web console - you can just as easily use gcloud cli or your favourite language.

## Role

We will be giving the GitHub Actions workflow runner access to our GCP project, so we must ensure to use a role which has only the absolutely necessary privileges.

### Create a new role

1. Navigate to: `IAM & Admin > Roles > +Create Role`
1. Enter a title for the role - I like to preface custom roles with `Custom -` so they're easy to list later on
1. (Optional) Enter a description
1. Set `Role launch stage` to `General Availability`
1. Assign permissions:

    * resourcemanager.projects.get
    * storage.buckets.get
    * storage.buckets.list
    * storage.objects.create
    * storage.objects.delete
    * storage.objects.get
    * storage.objects.list
    * storage.objects.update

See the GCP documentation for [Creating and managing custom roles](https://cloud.google.com/iam/docs/creating-custom-roles) for more details.

## Service Account

A service account with the previously created rule will be used by the workflow to connect to Cloud Storage and upload files.

### Create a new service account

1. Navigate to: IAM & Admin > Service Accounts > +Create Service Account
1. Enter a name for the account - I like to preface service accounts with `sa -`
1. Accept the recommended service account id
1. (Optional) Enter a description
1. Click Create
1. On the second page, select the custom role created in the previous step - this will assign permissions to the account
1. Select all other defaults to finish creating the account

See the GCP documentation page for [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for more details.

### Create a service account key

__Note:__ We will use the gcloud cli for this step even though the rest of the examples use the web console.
A key created in the console differs slightly from one created with gcloud - since our workflow uses gcloud, we need a correctly formatted key.

```bash
gcloud iam service-accounts keys create ~/key.json \
  --iam-account sa-name@project-id.iam.gserviceaccount.com
```

The key file will be created at `~/key.json`.
__Keep this file private - do no not store it in your repo - it contains everything needed to authenticate to your GCP project as the service account user.__

See the GCP documentation page for [Creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-gcloud) for more details.

### Secrets

The workflow uses the `gsutil` command line utility (included with gcloud) to interact to Cloud Storage.
gsutil needs the project, service account key, and Cloud Storage bucket supplied in order to connect and manage files.
We will store these as secrets in our GitHub repo and access them as variables in the workflow.

#### GCS_PROJECT

The name of the CGP project containing the Cloud Storage Bucket.

#### GCS_BUCKET

The name of the Cloud Storage bucket to deploy the site.

#### GCS_SA_KEY

The base64 encoded authentication key for the service account.

Base64 encode the key:

```bash
cat ~/key.json |base64
```

See the GitHub documentation page for [Creating and storing encrypted secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) for more details.

## Workflow

The workflow is created in your repo at `.github/workflows/workflow.yml`

Google provides some actions which can be imported to simplify your workflow, as well as some good examples in their [github-actions](https://github.com/GoogleCloudPlatform/github-actions) repo.

### Trigger the workflow

Since my workflow is for a personal website, I trigger when I push to master:

```yaml
on:
  push:
    branches:
    - master
```

### Set environment variables for the workflow runner

You can set environment variables for the workflow runner to use when it runs steps.
In this example we pull in the Cloud Storage bucket name from our GitHub secrets:

```yaml
env:
  GCS_BUCKET: ${{ secrets.GCS_BUCKET }}
```

### Install and configure gcloud (and gsutil)

Use the [setup-gcloud](https://github.com/GoogleCloudPlatform/github-actions/tree/master/setup-gcloud) action to install and configure the gcloud and gsutil command line tools.
Notice how we pull in the service account key and project id from our secrets:

```yaml
steps:
- name: Checkout
    uses: actions/checkout@v2

- name: Setup - gcloud / gsutil
  uses: GoogleCloudPlatform/github-actions/setup-gcloud@master
  with:
    service_account_key: ${{ secrets.GCS_SA_KEY }}
    project_id: ${{ secrets.GCS_PROJECT }}
    export_default_credentials: true
```

### Upload to Cloud Storage

Use the gsutil command line to upload your files to the Cloud Storage bucket.
In this example, we are uploading the generated static website, stored in the `content` subdirectory - specify whatever source path you require.
Notice how we pull in the bucket name from the environment variable we created in the workflow:

```yaml
- name: Deploy
  run: |-
    gsutil -m rsync -R output gs://$GCS_BUCKET
```

### Run workflow and check status

The results and output of the workflow can be seen in the `/actions` url of your repo in GitHub.
There's also an Actions link at the top of the page (where you select between code, issues, pull requests, etc.).

This output can be helpful when troubleshooting a broken workflow.

### Status badge

You can add a workflow status badge to your README.
Simply reference the workflow name (the `name` parameter in the workflow yml file) in the badge path:

```markdown
![{{alt text}}](https://github.com/{{github user}}/{{github repo}}/workflows/{{workflow%20name}}/badge.svg)
```

See the GitHub documentation for [Adding a workflow status badge to your repository](https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow#adding-a-workflow-status-badge-to-your-repository) for more details.

## Final thoughts

That's all there is to it!
Despite all of the steps, it probably takes about 10 to 15 minutes to get this configured (plus any trial and error to get the workflow behaving).
