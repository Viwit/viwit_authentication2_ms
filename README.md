# Authentication2

for init docker is necesary use this command\n

sudo usermod -aG docker ${USER} (SO's user)\n
su - ${USER}\n
docker system prune -a (optional for deleted all dockers) \n
docker build -t archit  {Folder where is the project}\n
docker run archit\n
