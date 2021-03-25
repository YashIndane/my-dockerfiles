FROM centos:latest

RUN yum install git -y

COPY jdk-8u171-linux-x64.rpm /

RUN rpm -i /jdk-8u171-linux-x64.rpm

COPY apache-maven-3.6.3-bin.tar.gz /

RUN tar -xvzf /apache-maven-3.6.3-bin.tar.gz

RUN mkdir /mavenhome 

RUN mv /apache-maven-3.6.3 /mavenhome

RUN echo "export MAVEN_HOME=/mavenhome" >> /root/.bashrc

RUN echo "export PATH=/mavenhome/apache-maven-3.6.3/bin/:$PATH" >> /root/.bashrc

RUN echo "export JAVA_HOME=/" >> /root/.bashrc
