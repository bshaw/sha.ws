# sha.ws

A personal website built with [Pelican](https://github.com/getpelican/pelican) and the [pelican-bootstrap3 theme](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3).

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

## Content License

[![CC BY 4.0][cc-by-shield]][cc-by]

Site content licensed under a [Creative Commons Attribution 4.0 International
License][cc-by], except where indicated otherwise.

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
