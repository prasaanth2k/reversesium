FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y 
RUN apt install -y python3 python3-pip systemd htop git
RUN useradd -m -s /bin/bash reversesium
RUN echo 'reversesium:crackme@123' | chpasswd
CMD [ "tail","-f","/dev/null" ]
