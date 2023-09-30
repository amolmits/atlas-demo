FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN python3 -m pip install pymongo
RUN python3 -m pip install pymongo==3.11

COPY . /opt/atlas_starter_python/

WORKDIR /opt/atlas_starter_python/

CMD ["/bin/bash"]
