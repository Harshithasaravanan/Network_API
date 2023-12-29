import paramiko

# ALL THE 4 FUNCTIONS ARE CONNECTED OVER SSH AND FOR TCPDUMP ALONE WIRESHARK IS USED, ENSURING THAT ALL 6 REQUIREMENTS ARE SATISIFIED


#Function for tcpdump + wireshark

def perform_tcpdump(ssh, file_tcp):

    command_for_tcp = 'sudo tcpdump -c 5 -i ens33 192.168.3.21 -w capture.pcap'
    
    stdin, stdout, stderr = ssh.exec_command(command_for_tcp)

    local_file = open(file_tcp, 'w')

    for line in str(stdout):
        local_file.write(line)

    print(f"\nOutput of TCPDUMP is successfully written to {file_tcp} as a wirshark file!\n")


#Function for nslookup

def perform_nslookup(ssh,file_ns):

    command_for_ns = "nslookup google.com"

    stdin, stdout, stderr = ssh.exec_command(command_for_ns)

    output = stdout.read().decode()

    with open(file_ns, 'w') as file:
        file.write(output)
    
    print(f"Output of NSLOOKUP is successfully written to {file_ns} as a text file!\n")


#Function for Traceroute
    
def perform_traceroute(ssh,file_tr):

    command_for_tr = "traceroute google.com"

    stdin, stdout, stderr = ssh.exec_command(command_for_tr)

    output = stdout.read().decode()

    with open(file_tr, 'w') as file:
        file.write(output)
    
    print(f"Output of TRACEROUTE is successfully written to {file_tr} as a text file!\n")


#Function for Port Mapping

def perform_nmap(ssh,file_nmap):

    command_for_nmap = "nmap 127.0.0.53"

    stdin, stdout, stderr = ssh.exec_command(command_for_nmap)

    output = stdout.read().decode()

    with open(file_nmap, 'w') as file:
        file.write(output)
    
    print(f"Output of NMAP is successfully written to {file_nmap} as a text file!\n")

    ssh.close() #close the ssh connection

# Define the SSH credentials and remote server details
ssh_host = '192.168.52.21'
ssh_port = 22
ssh_username = 'hs'
ssh_password = 'cse'

# Define the local file paths to save the captured data
tcp_file = 'C:/Users/acer/captured_packets.pcap'
ns_file = 'C:/Users/acer/output_ns.txt'
traceroute_file = 'C:/Users/acer/output_traceroute.txt'
port_scan_file = 'C:/Users/acer/output_nmap.txt'

# Create SSH client and connect to the remote server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_host, ssh_port, ssh_username, ssh_password)

# Perform the functionalities and save the captured packets locally in the PC
perform_tcpdump(ssh, tcp_file)
perform_nslookup(ssh,ns_file)
perform_traceroute(ssh, traceroute_file)
perform_nmap(ssh,port_scan_file)

print("****************************************************************************************")
print("\nperformed all the networking functions!\n")
print("****************************************************************************************")