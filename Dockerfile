FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y sysbench
ADD Data.txt /Data.txt
ADD cdc /cdc
CMD ./cdc
