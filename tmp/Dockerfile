FROM centos:centos8

WORKDIR /app

COPY . .

RUN dnf -y install python3
RUN yum -y install wget
RUN wget https://bintray.com/ookla/rhel/rpm -O bintray-ookla-rhel.repo
RUN mv bintray-ookla-rhel.repo /etc/yum.repos.d/
RUN yum -y install speedtest

CMD [ "python3", "./speedtest.py" ]