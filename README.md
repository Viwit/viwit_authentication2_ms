# Authentication2

for init docker is necesary use this command

###```sudo usermod -aG docker ${USER} (SO's user)```

###```su - ${USER}```
```docker system prune -a (optional for deleted all dockers)```
# Building the image
```docker build -t authentication2  {Folder where is the project}```
# Running the image
```docker run --network='host' -p {puerto}:{puerto} authentication2```

