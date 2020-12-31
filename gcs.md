![Status - Build and Deploy to Goolge Cloud Storage](https://github.com/bshaw/sha.ws/workflows/Build%20and%20Deploy%20to%20Google%20Cloud%20Storage/badge.svg)

## Hosting

The site is hosted via [Google Cloud Storage](https://cloud.google.com/storage) - See [Hosting a static website](https://cloud.google.com/storage/docs/hosting-static-website) for more details.

## GitHub Actions

The site is automatically built and deployed via GitHub Actions.

### Service Account

A service account with appropriate permissions on the Cloud Storage bucket is required for GitHub Actions to deploy the site - See [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts)

### Secrets

The GitHub Actions workflow depends on the following secrets, which must be configured for the repo - See [Creating and storing encrypted secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets):

| Secret Name | Description |
| :---------- | :---------- |
| GCS_PROJECT | The name of the CGP project containing the Cloud Storage Bucket |
| GCS_BUCKET | The name of the Cloud Storage bucket to deploy the site |
| GCS_SA_KEY | The base64 encoded authentication key for the service account with privileges to deploy the site - See [Creating and managing service account keys]((https://cloud.google.com/iam/docs/creating-managing-service-account-keys)) |

### Testing

The GitHub Actions workflow can be tested locally using [act](https://github.com/nektos/act).

To supply secret values for testing you must export them as environment variables - The required variables are shown (as secrets) in `.actrc`.
