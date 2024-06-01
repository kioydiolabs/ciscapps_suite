> [!CAUTION]
> **This guide is no longer being maintained. For the latest updated CISCAPPS documentation visit [https://ciscapps.kioydiolabs.org](https://ciscapps.kioydiolabs.org).**


## How to configure CISCAPPS
Configuring CISCAPPS is really simple. Just use the **Docker Compose** to
pull the image from **Docker Hub** and deploy a container.

All you need to do is make sure you have the **docker** and **docker-compose**
packages installed on your server, download the **_docker-compose.yaml_** file
and edit it to configure the options, then use the command **docker-compose up -d**
to pull and deploy the image.

### Step 1 : Install docker and docker-compose on your server
Run the following command to install docker and docker-compose : 
```
sudo apt update && sudo apt install docker.io docker-compose -y
```

### Step 2 : Download the example docker-compose.yaml file
Run the following command to download the docker-compose.yaml file :
```
wget https://raw.githubusercontent.com/kioydiolabs/ciscapps_suite/main/Docker/docker-compose.yaml
```

_Note : If you get an error that wget is not installed, run the command ```sudo apt install wget```_

### Step 3 : Edit the docker-compose.yaml file
You can edit the file by running :
```
sudo nano docker-compose.yaml
```

Then edit the `fullHostname`, `hostname`, `alphavantageKey`, `serverPort` according to the
instructions.
If you decide to edit the port, **Only edit the port number before the `:` and make sure to change the `serverPort` variable to the same
number.**

You can also copy the docker-compose.yaml file below and paste it into a text editor instead of
downloading it if you prefer that.

```
version: '3'
services:
  ciscapps:
    image: sthivaios/ciscapps:latest
    environment:
      fullHostname: "" # full hostname with http/https here. eg. : https://ciscapps.com or http://192.168.1.150
      hostname: "" # the ip or domain of the server
      alphavantageKey: "XXXXXXXXXX" # your AlphaVantage API key
      serverPort: "80"
    ports:
      - 80:80
```

### Step 4 : Deploy the container
Finally, deploy the container by running this command

```
sudo docker-compose up -d
```
