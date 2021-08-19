# Authentication2

```sudo usermod -aG docker ${USER} (SO's user)```

```su - ${USER}```

```docker system prune -a (optional for deleted all dockers)```


# for init docker is necesary use this command
# Building the image 
docker build -t authentication2 .
# Running the image

ever run in port 8080
docker run --network='host' -p 8080:8080 authentication2

