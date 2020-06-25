# gocd

A local docker stack for playing with gocd.

execute init.sh in the root directory and then execute source venv/bin/activate to setup your python virtual environment.


## Start it up

```bash
docker-compose up
```
This will create a gocd server, a gocd agent and an nginx reverse proxy.

## Nginx and SSL

Nginx is being used as a proxy a wildcard cert and private key are provided.

GoCD can be accessed one of two ways.

```bash
http://localhost:8153
```

or if you dnsmasq to point the domain dev.local to your localhost:

```bash
https://gocd.dev.local
```

## gocd agent

The gocd agent will attempt to register itself with the gocd server.

You will need to edit the docker-compose.yml file and update this line with the current auto register key.

```bash
 AGENT_AUTO_REGISTER_KEY: 9561ba37-fbe9-41df-9013-d0b45c51dc4e
 ```
You can get the current auto register key by running the `create_pipeline.py` script.

This produces to xml files, a before an after of the gocd configuration.

Either of these two files will have the auto register key of your gocd server instance in the agentAutoRegisterKey attribute of the server tag.


## Create a pipeline

The script `create_pipeline.py` will create a simple pipeline for this repo.

This repo will be checked out and the files listed.

## Local DNS

I am using NetworkManager and dnsmasq that allows me to use wildcard hostnames in the domain name `dev.local`

Basically any hostname in this domain points to localhost.

## Requirements

You will of course need the docker engine installed.

Having wildcard DNS resolution for the domain `dev.local` would also be nice but you could get by without it.

[Would you like know more about dnsmasq?](https://fedoramagazine.org/using-the-networkmanagers-dnsmasq-plugin/)



