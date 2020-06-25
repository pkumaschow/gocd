# gocd

execute init.sh in the root directory and then execute source venv/bin/activate

## Start it up

```bash
docker-compose up
```

## Create a pipeline

The script `create_pipeline.py` will create a simple pipeline for this repo.

This repo will be checked out and the files listed.

## Local DNS

I am using NetworkManager and dnsmasq that allows me to use wildcard hostnames in the domain name `dev.local`

Basically any hostname in this domain points to localhost.

## Nginx and SSL

Nginx is being used as a proxy a wildcard cert and private key are provided.

GoCD can be accessed one of two ways.

```bash
http://localhost:8153
```

or 

```bash
https://gocd.dev.local
```








