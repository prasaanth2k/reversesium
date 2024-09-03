FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip systemd htop git sudo curl gdb gcc \
    ssh x11-utils wmctrl pciutils nano
RUN apt-get install -y passwd default-jre binwalk
COPY /dependfiles/radare2 /usr/bin/radare2
RUN /usr/bin/radare2/sys/install.sh
RUN apt-get -y install strace ltrace
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
COPY /scripts/re.sh /usr/bin/re
RUN chmod +x /usr/bin/re
COPY /scripts/apktoolinstaller.sh /usr/local/bin/apktool
RUN chmod +x /usr/local/bin/apktool
COPY /dependfiles/apktool.jar /usr/local/bin/apktool.jar
USER re
WORKDIR /home/re
