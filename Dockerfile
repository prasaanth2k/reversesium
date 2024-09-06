FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip systemd htop git sudo curl gdb gcc \
    ssh x11-utils wmctrl pciutils nano
RUN apt-get install -y passwd default-jre binwalk
COPY /dependfiles/radare2 /usr/bin/radare2
RUN /usr/bin/radare2/sys/install.sh
RUN apt-get -y install strace ltrace hping3 inetutils-ping
COPY /scripts/entry.sh /usr/local/bin/script.sh
RUN chmod +x /usr/local/bin/script.sh
COPY /scripts/usermanagement.sh /usr/local/bin/usermanagement.sh
RUN chmod +x /usr/local/bin/usermanagement.sh
COPY /scripts/root.sh /root/.bashrc
COPY /scripts/re.sh /usr/bin/re
RUN chmod +x /usr/bin/re
COPY /scripts/apktoolinstaller.sh /usr/local/bin/apktool
RUN chmod +x /usr/local/bin/apktool
COPY /dependfiles/apktool.jar /usr/local/bin/apktool.jar
COPY /scripts/pythonpackes.sh /usr/local/bin/pythonpackes
RUN chmod +x /usr/local/bin/pythonpackes
RUN /usr/local/bin/pythonpackes
RUN apt-get install -y openssh-server bsdmainutils xxd checksec build-essential dumb-init
EXPOSE 4326
EXPOSE 22
ENTRYPOINT [ "/usr/local/bin/script.sh" ]