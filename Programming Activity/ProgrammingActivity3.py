import ipaddress

subnetMask = 20
network = ipaddress.IPv4Network(f'10.0.0.0/{subnetMask}', strict=False)
num_subnets = 2 ** (network.max_prefixlen - network.prefixlen)
num_usable_ips = len(list(network.hosts()))

# Display the address range
print(f"Address range: {network.network_address} - {network.broadcast_address}")

# Display the bits
print(f"Network bits: {network.prefixlen}")
print(f"Host bits: {32 - network.prefixlen}")

# Calculate and display the number of usable IP addresses
print(f"Number of usable IP addresses: {num_usable_ips}")

# Calculate and display the number of subnets
print(f"Number of IP Address/Subnets: {num_subnets}")



#Basically the formula to for the number of remaining bits is 2^n - 2 where n is the number of bits that are left after the subnet mask
subnetMask = 24
num_subnets = 2 ** (32 - subnetMask)
num_usable_ips = len(list())
num_remaining_bits = num_subnets - 2
print(f"Number of usable IP addresses: {num_usable_ips}")
print(f"Host bits: {32 - subnetMask}")
print(f"Number of IP Address/Subnets: {num_subnets}")
print(f"Number of remaining bits: {num_remaining_bits}")