![Build and push to ghcr](https://github.com/bshaw/sha.ws/workflows/Build%20and%20push%20to%20ghcr/badge.svg)

## Hosting

The site is packaged as a container and can be run from any properly configured container runtime environment.

Images are pushed to the [Github Container Registry](https://ghcr.io) - See [Working with the Container registry
](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) for more details.

## Secrets

The GitHub Actions workflow depends on the following secrets, which must be configured for the repo - See [Creating and storing encrypted secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets):

| Secret Name | Description |
| :---------- | :---------- |
| CR_PAT      | PAT (personal access token) for pushing images to the Github Container Registry |
