---
Title: Run the .NET Core SDK and Runtime from a Docker container
Date: 2020-07-08 21:40
Modified: 2020-07-24 23:37
Tags: dotnet, docker
Category: Docker
Slug: run-dotnet-in-docker-container
Author: Brian Shaw
Summary: Run the .NET Core SDK and Runtime from a Docker container
Status: published
---

## Overview

I run a lot of my tooling straight from Docker containers instead of installing them on my system.
Doing so helps me ensure I'm using the desired version(s) straight from the official maintainers, helps me keep my system tidy, and guarantees a consistent environment across machines.

I've started getting my feet wet with .NET Core in preparation for an upcoming project and noticed that neither Microsoft's documentation nor their [Docker Hub page for .NET Core](https://hub.docker.com/_/microsoft-dotnet-core) mention running the SDK or runtimes straight from the published images, so I've put together a simple wrapper to run the .NET Core SDK and Runtime from a Docker container:

[https://github.com/bshaw/dotnet-docker/](https://github.com/bshaw/dotnet-docker/).

The script uses the official [Microsoft .NET Core SDK image](https://hub.docker.com/_/microsoft-dotnet-core-sdk/) using the `3.1` tag (Debian 10).
It is based on (effectively forked from) the Docker Compose [Run docker-compose in a container](https://github.com/docker/compose/blob/1.25.4/script/run/run.sh) script, which properly handles volume mappings and various options based on the environment.

## Installation

Place the wrapper script in your path and made it executable:

```bash
sudo curl -L --fail https://raw.githubusercontent.com/bshaw/dotnet-docker/master/run.sh -o /usr/local/bin/dotnet
sudo chmod +x /usr/local/bin/dotnet
```

## Usage

Use the dotnet command as you would if it were installed locally:

```bash
❯ dotnet --info
.NET Core SDK (reflecting any global.json):
 Version:   3.1.301
 Commit:    7feb845744

Runtime Environment:
 OS Name:     debian
 OS Version:  10
 OS Platform: Linux
 RID:         debian.10-x64
 Base Path:   /usr/share/dotnet/sdk/3.1.301/

Host (useful for support):
  Version: 3.1.5
  Commit:  65cd789777

.NET Core SDKs installed:
  3.1.301 [/usr/share/dotnet/sdk]

.NET Core runtimes installed:
  Microsoft.AspNetCore.App 3.1.5 [/usr/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 3.1.5 [/usr/share/dotnet/shared/Microsoft.NETCore.App]

To install additional .NET Core runtimes or SDKs:
  https://aka.ms/dotnet-download
```

### TODO: Multi version support

The dotnet version is specified as a variable in the script - you can easily update the file on your system depending on your requirements.
I may also update the script to support multiple versions.
Feel free to send a pull request if you get to it before I do.
