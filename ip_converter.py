# The purpose of this program is to output the network address, the broadcast
# address, the first and the last usable network addresses based on the IP 
# address and prefix length.

# returns the binary ip string from the original IP address
def get_binary_ip(ip):
    # split the IP by octets
    ip_octets = ip.split('.')
    binary_ip = ''
    for octet in ip_octets:
        binary_ip += f'{int(octet):08b}'
    return binary_ip

# returns the decimal ip string from the binary ip string
def get_decimal_ip(binary_ip):
    # get the decimal IP string
    decimal_ip = f"{int(binary_ip[0:8], 2)}.{int(binary_ip[8:16], 2)}.\
{int(binary_ip[16:24], 2)}.{int(binary_ip[24:32], 2)}"
    return decimal_ip

# returns you the binary subnet mask based on the prefix length
def get_subnet_mask(prefix_length):
    # initialize subnet_mask string
    subnet_mask = ''
    # add 1 for prefix length bits and 0 for the rest
    for number in range(prefix_length):
        subnet_mask += '1'
    for number in range(prefix_length, 32):
        subnet_mask += '0' 
    # return the mask
    return subnet_mask

# get network address from the binary IP address and subnet mask
def get_network_address_by_mask(binary_ip, subnet_mask):
    network_address = ''
    # iterate through every bit
    for bit in range(32):
        # get the network bit based on the value of current IP and subnet bits
        network_bit = int(int(binary_ip[bit]) and int(subnet_mask[bit]))
        # add the network bit 
        network_address += str(mask_bit)
    return network_address

# get network address from the binary IP address and prefix length
def get_network_address(binary_ip, prefix_length):
    network_address = binary_ip[:prefix_length]\
                      + (32 - prefix_length) * '0'
    return network_address

# get broadcast address from the binary IP address and prefix length
def get_broadcast_address(binary_ip, prefix_length):
    broadcast_address = binary_ip[:prefix_length]\
                        + (32 - prefix_length) * '1'
    return broadcast_address

# get first usable address from the binary IP address and prefix length
def get_first_usable_address(binary_ip, prefix_length):
    first_usable_address = binary_ip[:prefix_length]\
                           + (32 - prefix_length - 1) * '0' + '1'
    return first_usable_address

# get last usable address from the binary IP address and prefix length
def get_last_usable_address(binary_ip, prefix_length):
    last_usable_address = binary_ip[:prefix_length]\
                          + (32 - prefix_length - 1) * '1' + '0'
    return last_usable_address

# main 
ip = input("Enter the IP address: ")
binary_ip = get_binary_ip(ip)
prefix_length = int(input("Enter the prefix length: "))

print(f"""
#######################################
Network Address:        {get_decimal_ip(get_network_address(binary_ip, prefix_length))}
Broadcast Address:      {get_decimal_ip(get_broadcast_address(binary_ip, prefix_length))}
First Usable Address:   {get_decimal_ip(get_first_usable_address(binary_ip, prefix_length))}
Last Usable Address:    {get_decimal_ip(get_last_usable_address(binary_ip, prefix_length))}
Subnet Mask:            {get_decimal_ip(get_subnet_mask(prefix_length))}
#######################################
""")
