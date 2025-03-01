def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and not i_part == 0: return False
        return 0 <= i_part < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part): return False
    return True

def decimal_to_binary(n):
    if n == 0: return '0'
    if n == 1: return '1'
    next, digit = divmod(n, 2)
    return decimal_to_binary(next) + str(digit)

def binary_to_decimal(b:str):
    if b == '': return 0
    place = len(b) - 1
    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))


#Convert ip address to binary
def ip_to_binary(ip: str): #two parameters, ip and string
    if not is_valid_ip(ip): # pulls up is valid function
        return "Invalid IP Address" #if is valid is false, returns invalid ip

    parts = ip.split('.') #seperates ip by .
    binary_parts = [decimal_to_binary(int(part)).zfill(8) for part in parts]
    return '.'.join(binary_parts) #zfill makes sure its 8 digits

print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"
#print(is_valid_part('127'),
     # is_valid_part('AAA'),
      #is_valid_part('-255'),
     # is_valid_part('01'),
    #  is_valid_part('0'),
     #