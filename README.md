# MAPO
multi-objective IoT application placement

## Paper Citation
This project is related to our recent paper available on:
https://dl.acm.org/citation.cfm?id=3365892

## Contributors
	1.Narges Mehran (PhD Student, Alpen-Adria Universitat Klagenfurt, Austria)
	2.Dragi Kimovski (PostDoc, Alpen-Adria Universitat Klagenfurt, Austria)
	Contact: narges(at)itec.aau.at ; dragi.kimovski(at)aau.at



This tutorial is just for devices running Debian based OS.
## Inputs for Multi-objective optimization algorithm
Two python codes are provided which prepare the JSON files for the resource configurations and component-based application requirements. These JSON files are as input arguements for NSGA-II algorithm executed in jMetal (a framework for multi-objective optimization with metaheuristics).

## Experiments

We had 6 experiments comparing MAPOwith FSPP, and EW. We model one component based application, mental health care, in terms of number of CPU instructions, memory, storage and bandwidth that they require.

## Testbed devices

For real-world testbed, we exploit four Raspberry Pi 3 model B+ devices as the Mobile Edge devices (MEs) and one higher capacity devices as a CDC.
As a CDC device, we use a virtual machine running in a private Cloud with an eight-core Intel Core i7-7700 CPU at 3.60GHz and 15.6GHz of RAM, running Ubuntu 16.04 LTS.
The testbed components are interconnected with a dedicated Gigabit Ethernet switch and secured using the SSH protocol.

## Emulation of latency between devices

For emulating the latency between devices, we created artificial network delays using the Linux tc (traffic control) https://linux.die.net/man/8/tc command.
We assume that the IoT devices are close to the MEs with an average latency of 1ms. The latency between ME and GW is 10ms, and between GW and CDC of 70ms, obtained using the Global Ping Statistics in WonderNetwork. 
* to add the latency, run the following command
	```sudo tc qdisc add dev <Device-ID> root netem delay 70ms```
* to delete the latency, run the following command
	```sudo tc qdisc del dev <Device-ID> root netem delay 70ms```


## Raspbian Operating System for Raspberry Pi devices

We use the nc command for data communication between containerized application components running on different devices.
We install Raspbian GNU/Linux 9.8 (stretch) https://www.raspberrypi.org/downloads/raspbian/


## Installation

We install Docker engine on the CDC and the Fog devices to prepare containerized application components.
To install the latest version of Docker Engine, please refer to the following URL:
https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Run Docker as daemon

* check if installed
    ```which docker```
* run daemon
    ```systemctl start docker```
* check status
    ```systemctl status docker```
    

## Base image of Docker and the application

We instantiate our Docker image by using an Ubuntu:14.04 base image.
To model the behaviour of applications, we utilize SysBench and installed SysBench through the system package manager on the containerized devices: ```sudo apt-get install sysbench```.
We emulate the execution of application components with stressing the CPU and MEM by calculating the prime numbers in the set of MaxPrime={400,800,1500,3000}.
 
The data transferred between application components is generated by a few data-files with various sizes as mentioned in our paper.
Every device just runs one container to execute the components assigned to it.

## Build Docker image
    docker build -t MAPO:latest .
## Run the Docker container
    docker run -it MAPO:latest

## Cost calculations

In CostByRunningAppOnTestbed section, we provide scripts of calculating economic costs based on resources and application executed on them.
