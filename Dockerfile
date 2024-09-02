FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip systemd htop git sudo curl gdb gcc \
    ssh x11-utils wmctrl pciutils nano
RUN apt-get install -y passwd
RUN useradd -m re && \
    usermod -aG sudo re
RUN echo 're:crackme@123' | chpasswd
RUN sed -i 's|/bin/sh|/bin/bash|' /etc/passwd
RUN echo 're ALL=(ALL) ALL'>> /etc/sudoers
COPY /scripts/entry.sh /root/entry.sh
RUN chmod +x /root/entry.sh
RUN /root/entry.sh
COPY /scripts/root.sh /root/.bashrc
COPY /scripts/user.sh /home/re/.bashrc
USER re
RUN git clone --depth=1 https://github.com/ohmybash/oh-my-bash.git ~/.oh-my-bash
WORKDIR /home/re
