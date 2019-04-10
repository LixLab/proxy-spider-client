# Proxy Spider Client 
Proxy Spider Client is a docker image which can deliver to you list of proxy to local txt file from ProxySpider Api.
List of proxy will be delivered and updated to txt file every minute.

### Installation guide
- Clone ProxySpider app:
```
cd ~
git clone https://github.com/LixLab/proxy-spider-client.git
```

- Build docker image:
```
cd proxy-spider-client
docker build -t proxy-spider-client .
```

- Create directory for storing proxy.txt
```
mkdir ~/FOLDER_NAME_HERE
```

- Run docker container in background with your volume information:
```
docker run -v ~/FOLDER_NAME_HERE:/opt/app/shared --restart always -itd proxy-spider-client
```

- Now you can see in ```~/FOLDER_NAME_HERE/proxy.txt``` list of proxy like:
```
111.111.111.111
111.111.111.222
111.111.111.444
111.111.111.999
```

- Enjoy!