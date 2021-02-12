FROM centos:latest

RUN yum install openssh-server -y

RUN ssh-keygen -A

RUN yum install passwd -y

RUN echo "bottle" | passwd root --stdin

CMD /usr/sbin/sshd -D

