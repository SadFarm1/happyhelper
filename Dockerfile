FROM ubuntu


ENV TZ America/Indiana/Indianapolis

COPY ./.env /.env


RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3.8 python3-pip git -y

ARG CACHEBUST=1 
RUN git clone http://209.141.54.217:3000/SadFarm/HappyHelper /HappyHelper
RUN pip3 install -r /HappyHelper/requirements.txt




WORKDIR /HappyHelper
CMD ["python3", "launcher.py"]