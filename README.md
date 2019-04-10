1) Clone the repository of ProxySpider app :
```
cd ~
git clone https://github.com/LixLab/proxy-spider-client.git
```
2) Build docker image:
```
cd proxy-spider-client
docker build -t proxy-spider-client .
```
3) Run docker container in background with mount parameters:
```
docker run -v ~/code/proxy.txt/proxy.txt:/opt/app/shared/proxy.txt --restart always -itd proxy-spider-client
```