"""checkes if the ip segment is valid w/o leading zeros"""
def is_valid_part(part):
    try:
        i_part = int(part)
        if part != str(i_part):  # Prevents leading zeros
            return False
        return 0 <= i_part < 256
    except ValueError:
        return False

"""checks if ip is valid """
def is_valid_ip(ip: str):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    return all(is_valid_part(part) for part in parts)

"""converts decimal to 8bit binary"""
def decimal_to_binary(n):
    """Converts a decimal number to an 8-bit binary string using recursion."""
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    next_value, digit = divmod(n, 2)
    return decimal_to_binary(next_value) + str(digit)

"""Converts  binary to a decimal number"""
def binary_to_decimal(b: str):
    if not b:
        return 0
    place = len(b) - 1
    return (2 ** place) * int(b[0]) + binary_to_decimal(b[1:])

"""Converts decimal IP address to binary"""
def ip_to_binary(ip: str):
    if not is_valid_ip(ip):
        return "Invalid IP Address"

    parts = ip.split('.')
    binary_parts = [decimal_to_binary(int(part)).zfill(8) for part in parts]
    return '.'.join(binary_parts) #puts a . between the parts

"""Converts  binary IP back to decimal"""
def binary_to_ip(binary_ip: str):
    parts = binary_ip.split('.')
    if len(parts) != 4 or any(len(part) != 8 or not set(part).issubset({'0', '1'}) for part in parts):
        return "Invalid Binary IP"

    decimal_parts = [str(binary_to_decimal(part)) for part in parts]
    return '.'.join(decimal_parts)

"""Detects the type of IP input (decimal or binary) & converts it"""
def ip_convert(ip: str):
    if is_valid_ip(ip):
        return ip_to_binary(ip)
    elif all(len(part) == 8 and set(part).issubset({'0', '1'}) for part in ip.split('.')):
        return binary_to_ip(ip)  #the all in front of lens makes all conditions have to be true
    else:
        return "Invalid IP Format"


# Test Cases
print(ip_to_binary("192.168.1.1"))  # Expected: "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # Expected: "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # Expected: "Invalid IP Address"

print(binary_to_ip("11000000.10101000.00000001.00000001"))  # Expected: "192.168.1.1"
print(binary_to_ip("11111111.11111111.11111111.00000000"))  # Expected: "255.255.255.0"

print(ip_convert("192.168.1.1"))  # Expected: "11000000.10101000.00000001.00000001"
print(ip_convert("11000000.10101000.00000001.00000001"))  # Expected: "192.168.1.1"
print(ip_convert("256.1.1.1"))  # Expected: "Invalid IP Format"
print(ip_convert("11000000.10101000.00000001"))  # Expected: "Invalid IP Format"