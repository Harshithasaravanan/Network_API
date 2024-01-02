# Network_API
Simulation of network connection in GNS3 and executing all the commands for network troubleshooting using python

AIM : 

To automate the troubleshooting process for a system using python scripts and GNS3 emulation software on a Linux Machine (VM)

STEPS :

PART 1 – GNS3

•	Create a Virtual Machine in any virtualization software (preferably VMware Workstation Player for free version) and install the Linux OS in it

•	Navigate to the Virtual machine settings (Edit Virtual Machine Settings) and check what is the network adapter assigned to the VM by clicking on the adapter option. Ensure that you don’t change it. Ensure it has 4 cores 

•	Open GNS3 and first configure the GNS3VM and make sure it is running along with your local CPU

•	Add a cisco router, a switch, a cloud to connect the router to the internet and the Linux VM you created in a new GNS3 topology as shown below

 ![WhatsApp Image 2024-01-02 at 18 20 45](https://github.com/Harshithasaravanan/Network_API/assets/129355754/a6c3e210-b6e4-4cee-89fe-732643bff58c)


•	First configure the router to act as a DHCP server

    o	Open the router’s console in GNS3
    o	Type conf t under FastEthernet0/0
    o	Type ip address dhcp
    o	Save it by typing do wr

•	After typing these commands, the router is assigned a dhcp address by the gateway router

•	Next, Connect the router to the switch and the switch to the VM. Also connect the router to the cloud. The cloud acts as the gateway router to provide internet access to your entire topology

•	Now set up a static ip address for the router so that it can communicate with the VM. Note that the ip address should correspond to the network adapter subnet of the VM which was configured upon VM creation

    o	Open conf t under FastEthernet0/1

    o Type ip address 192.168.3.14 255.255.255.0(the ip you want to give)

    o	Type no sh

    o	Save it

•	Go to the VM and configure the static ip address for the VM. For example, let us assume the static ip of the VM is 192.168.3.21. The network adapter that was assigned to the VM has a subnet of 192.168.3.0 with the subnet mask of 255.255.255.0

    o	In Linux, follow the given points to setup a static ip
    o	Type cd /etc/netplan
    o	Type ls
    o	You will get a file name with .yaml extension
    o	Then type sudo nano file_name_obtained
    o	If prompted for password enter it and the file will open
    
    o	Navigate to the bottom of the file and position below renderer and type ethernets followed by the static address details along with the dns servers and default gateway as shown below
    
    o	After writing it press ctrl+X and press Y when prompted for saving the file and then hit Enter
    
    o	Now type sudo netplan try to try the configurations. A couple of warnings will come. Ignore it and hit enter when prompted for it
    
    o	Then type sudo netplan apply and it should now configure your system. Again, the warnings that will be shown are to be ignored
     
•	Now open a terminal in your VM and try to ping 192.168.3.14 which is the cisco router. It should successfully ping. Ping the VM from the router by opening a console in GNS3

•	If we try to ping 8.8.8.8 it says that the network is unreachable. This is because the Local address of the VM and the router is not translated to a global address which is in the subnet of the gateway router

    o	Open the router console again and type
    
    o	Conf t
    o	Int FastEthernet0/0
    o	Ip nat outside
    o	Exit
    o	Do wr
    o	Int FastEthernet0/1
    o	Ip nat inside
    o	Exit
    o	Do wr
    o	Exit
    
    o	Ip address inside source static 192.168.3.21 192.168.0.22. Here, the second address given is an address which is part of the gateway router subnet. In my machine, The gateway’s router subnet was 192.168.0.0
    
    o	Wr
    o	Ip domain-lookup
    
    o	Ip name-server 127.0.0.53. This was the name server of my Linux VM which was discovered when I typed cat /etc/resolv.conf in my Linux VM terminal

•	Now if we ping 8.8.8.8 from the VM we can see a successful ping. Commands like nslookup, traceroute, tcpdump, port scanning work successfully

•	Note that your linux vm should have installed openssh-server, nmap, traceroute and net-tools in order to execute all these commands

•	Add another network adapter in your VM by navigating to the virtual machine settings and clicking add -> network adapter -> finish 

•	Set a static ip for the system for the second adapter as shown below. Note the subnet of this adapter. Use the same steps as before to configure the static ip for this NIC as well

![WhatsApp Image 2024-01-02 at 18 20 45-2](https://github.com/Harshithasaravanan/Network_API/assets/129355754/310d9298-49b2-40d3-9c75-afbb345ad360)


PART 2 – VSCODE

•	Open a python file where the scripts for automating all the commands will be written in your Local PC

•	Use ssh to connect to the linux VM from your Local PC and perform all the tasks.

•	Write the functions for tcpdump, nslookup, traceroute and port-scanning in one code and store the data generated in the linux vm in a local file in your PC

•	Run the scripts. Remember to ssh into the linux vm using the second static ip address but perform the networking commands for the first ip address configured for the VM

•	After the files are generated, use Wireshark to read the contents of the tcpdump file because the rest of the files will be a text file and are not readable by Wireshark.

RESULT:

Thus, the troubleshooting process was automated using Python and GNS3 along with VMware Workstation Player.
  



