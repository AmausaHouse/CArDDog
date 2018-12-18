FROM python:3.6
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN apt-get update 
RUN apt install -y apt-utils
RUN apt-get install -y cmake
RUN  git clone https://github.com/opencv/opencv /usr/share/opencv
RUN pip install -r requirements.txt
