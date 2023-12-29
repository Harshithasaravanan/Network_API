# Network_API
Simulation of network connection in GNS3 and executing all the commands for network troubleshooting using python 

The Steps : 

    1. Set up the GNS3 environment consisting of a cloud to connect the router to the gateway router (a.k.a the local Ethernet)
    2. Configure the Router to act as a DHCP server and it will be assigned an IP address by the gateway router
    3. Assign it a static ip in addition to the DHCP address in order to interact with the VM in your topology 
    4. Test if it pings the VM. The VM and Router can ping each other but the VM cannot ping external DNS servers such as 8.8.8.8 
    5. For this, configure static NAT in the router and map the IP address of the VM to an IP address which is in the subnet of the Gateway Router in the ROuter console in GNS3
    6. Try to ping 8.8.8.8 from your VM and it should work
    7. Execute all the troubleshooting options possible
    8. Develop a Python script using Paramiko Library to remotely control the VM from the local PC
