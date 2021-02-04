FROM centos:latest

RUN yum install git -y

RUN yum install python3 -y

RUN pip3 install joblib

RUN pip3 install numpy

RUN pip3 install pandas

RUN pip3 install -U scikit-learn

RUN mkdir /ml_folder

COPY random_forest_classification.py /ml_folder

ENTRYPOINT python3 /ml_folder/random_forest_classification.py


