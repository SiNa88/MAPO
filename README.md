This tutorial is just for devices running Debian based OS.
    
## Experiments

We run 6 experiments comparing MAPO with FSPP, and EW. We model one component based application, mental health care, in terms of number of CPU instructions, memory, storage and bandwidth that they require.

## Testbed devices

For real-world testbed, we exploit four Raspberry Pi 3 model B+ devices as the Mobile Edge devices (MEs) and one higher capacity devices as a CDC.
As a CDC device, we use a virtual machine running in a private Cloud with an eight-core Intel Core i7-7700 CPU at 3.60GHz and 15.6GHz of RAM, running Ubuntu 16.04 LTS.
The testbed components were interconnected with a dedicated Gigabit Ethernet switch and secured using the SSH protocol.

## Emulation of latency between devices

For emulating the latency between devices, we created artificial network delays using the Linux tc (traffic control) {https://linux.die.net/man/8/tc} command.
We assumed that the IoT devices are close to the MEs with an average latency of 1ms. The latency between ME and GW is 10ms, and between GW and CDC of 70ms, obtained using the Global Ping Statistics in WonderNetwork. 

## Raspbian Operating System for Raspberry Pi devices

We used the nc command for data communication between containerized application components running on different devices.
We installed Raspbian GNU/Linux 9.8 (stretch) {https://www.raspberrypi.org/downloads/raspbian/}.


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
    

## Docker base image and the application

We instantiate a Docker image by starting an Ubuntu:14.04 base image.
We installed SysBench through the system package manager on the containerized devices. 
```sudo apt-get install sysbench```
To emulate the behaviour of applications, we utilize SysBench to emulate the execution of application components with stressing the CPU and MEM by calculating the prime numbers in the set of MaxPrime={400,800,1500,3000}.
 
We emulate the data transferred between application components by generating and sending data-files with various sizes as mentioned in our paper.
Every device just runs one container to execute the components assigned to it.
