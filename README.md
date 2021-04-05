# Authentication2

for init docker is necesary use this command

```sudo usermod -aG docker ${USER} (SO's user)```
```su - ${USER}```
```docker system prune -a (optional for deleted all dockers)```
```docker build -t archit  {Folder where is the project}```
```docker run archit```
