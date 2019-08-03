We run 6 experiments comparing MAPO with FSPP, and EW. We model one component based application, mental health care, in terms of number of CPU instructions, memory, storage and bandwidth that they require.
For real-world testbed, we exploit four Raspberry pi devices as the Mobile Edge devices (MEs) and one higher capacity devices as a CDC. 
As a CDC device, we use a virtual machine running in a private Cloud with an eight-core Intel$^\circledR$ Core$^{(TM)}$ i7-7700 CPU at 3.60GHz and 15.6GHz of RAM, running Ubuntu 16.04 LTS. 
The testbed components were interconnected with a dedicated Gigabit Ethernet switch and secured using the SSH protocol.
We assumed that the IoT devices are close to the MEs with an average latency of 1ms. The latency between ME and GW is 10ms, and between GW and CDC of 70ms, obtained using the Global Ping Statistics in WonderNetwork. 
For emulating the latency between devices, we created artificial network delays using the Linux tc{https://linux.die.net/man/8/tc} command. 
We used the nc command for data communication between containerized application components running on different devices.
We installed Raspbian GNU/Linux 9.8 (stretch) {https://www.raspberrypi.org/downloads/raspbian/} 
and Docker version 18.09{https://www.docker.com/} on all RPis and deployed a containerized virtualization environment.
We instantiate a Docker image on the CDC and the Fog devices by starting an Ubuntu:14.04 base image.
We installed SysBench through the system package manager on the containerized devices. 
We utilize SysBench to emulate the execution of application components with stressing the CPU and MEM by calculating the prime numbers in the set of MaxPrime={400,800,1500,3000}. 
While executing this command in a single loop with a limit of one thousand, we calculate the amount of CPU utilization with Linux top command.
We emulate the data transferred between application components by generating and sending data-files with various sizes. 
Every device just runs one container to execute the components assigned to it.