# Modify Configuration File

##### Step 1 : _Download the docker compose file_

Download the **docker-compose.yaml** file

```Shell
wget https://raw.githubusercontent.com/kioydiolabs/ciscapps_suite/main/Docker/docker-compose.yaml
```

##### Step 2 : _Modify the docker compose file_

The **docker-compose.yaml** file looks like this :

```yaml
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

1) Edit the `fullHostname` variable so that it begins with `http://` or `https://`. This can either be an IP address or a domain. 
   Example : `https://ciscapps.com` or `http://192.168.1.100`
2) Edit the `hostname` variable to the domain or IP address of the server **without** `http://` or `https://` in front.
   Example : `ciscapps.com` or `192.168.1.100`
3) Edit the `alphavantageKey` variable to your AlphaVantage™ API key. You can get one from AlphaVantage's website.
   If you don't want to use the stocks app, leave that as `XXXXXXXXXX`
4) If you wish to change the default port (port 80) change the `serverPort` variable to that port. Make sure to change
   the port number in the `ports:` section too, but **don't** change the number 80 after the `:`. Example : to use port
   8056, set the ports to `8056:80` and change the `serverPort` variable to `8056`.

**Make sure to save the file!**