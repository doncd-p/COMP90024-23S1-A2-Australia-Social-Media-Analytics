# Purpose: Read the instance_addresses.ini file and configure the inventory file
#         with the IP addresses of the instances to determine deployment
ip_addresses = []

# Flag to check if we're in the [all] section
in_all_section = False

# Open the file and read lines
with open('instance_addresses.ini', 'r') as file:
    for line in file:
        line = line.strip()  # Remove whitespace
        
        # If this line is the desired section header
        if line.startswith('[') and line.endswith(']'):
            # Update in_all_section flag
            in_all_section = line == '[all]'
        # If this line is not a section header and we're in the [all] section
        elif in_all_section:
            ip_addresses.append(line)

# Open the file in append mode and write the IP addresses for hosts of 
# applications
with open('instance_addresses.ini', 'a') as file:
    
    file.write('\n[COUCHDB_INSTANCES]\n') 
    for ip in ip_addresses[:3]:
        file.write(ip + '\n') 
        
    # FRONTEND_INSTANCE and BACKEND_INSTANCE are the same on the same VM
    file.write('\n[FRONTEND_INSTANCE]\n') 
    file.write(ip_addresses[-1] + '\n') 
    file.write('\n[BACKEND_INSTANCE]\n') 
    file.write(ip_addresses[-1] + '\n') 