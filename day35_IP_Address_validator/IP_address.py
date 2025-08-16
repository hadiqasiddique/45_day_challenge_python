import re

def is_valid_ip(ip):
    """Check if the given IP address is valid.
    Args:
        ip (str): IPv4 address as a string.
    
    Returns:
        bool: True if valid, False otherwise."""
    # Define regex pattern for IPv4 address
    pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    
    # Check if format matches
    if pattern.match(ip):
        parts = ip.split('.')
        for part in parts:
            # Each part must be between 0 and 255
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    return False


def main():
    while True:
        ip = input("Enter an IP address to validate or type 'exit' to quit: ").strip()
        
        if ip.lower() == 'exit':
            print("Program terminated.")
            break
        
        if is_valid_ip(ip):
            print(f"{ip} is a valid IP address.\n")
        else:
            print(f"{ip} is an invalid IP address.\n")


if __name__ == "__main__":
    main()
