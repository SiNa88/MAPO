#!/bin/bash

date +"%s.%3N" && \
nc -q 0 -l <your_desired_port> > out.txt && \
#sysbench --test=cpu --num-threads=4 --cpu-max-prime=400 run && \
sysbench --test=cpu --num-threads=8 --cpu-max-prime=400 run && \
sysbench --test=cpu --num-threads=8 --cpu-max-prime=400 run && \
sysbench --test=cpu --num-threads=8 --cpu-max-prime=400 run  && \
sysbench --test=cpu --num-threads=8 --cpu-max-prime=400 run  && \
#sysbench --test=cpu --num-threads=4 --cpu-max-prime=400 run && \
#sysbench --test=cpu --num-threads=4 --cpu-max-prime=800 run && \
#sysbench --test=cpu --num-threads=4 --cpu-max-prime=1500 run && \
#sysbench --test=cpu --num-threads=4 --cpu-max-prime=3000 run && \
nc -n  <your_ip_address> <your_desired_port> < Data.txt && \
date +"%s.%3N" &&  \
exit
