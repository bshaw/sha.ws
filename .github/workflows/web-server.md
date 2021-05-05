[![Build and deploy to web server](https://github.com/bshaw/sha.ws/actions/workflows/web-server.yml/badge.svg)](https://github.com/bshaw/sha.ws/actions/workflows/web-server.yml)

## Hosting

The site is hosted on a private web server.

Static files are pushed to the server via rsync over ssh.

## Secrets

The GitHub Actions workflow depends on the following secrets, which must be configured for the repo - See [Creating and storing encrypted secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets):

| Secret Name     | Description |
| :-------------- | :---------- |
| SSH_HOST        | Host where the files will be copied |
| SSH_USER        | User to connect to the host |
| SSH_KEY         | Private key for $SSH_USER to connect to $SSH_HOST |
| SSH_KNOWN_HOSTS | SSH known_hosts file for secure host checking |
| SERVER_PATH     | Files system path on $SSH_HOST where to copy the files |
