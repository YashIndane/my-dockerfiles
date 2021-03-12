FROM centos:latest

RUN yum install python3 -y

RUN pip3 install flask

RUN pip3 install keras

RUN yum install gcc-c++ -y

RUN yum install python3-devel -y

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir tensorflow==2.4.1
