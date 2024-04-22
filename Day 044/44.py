import requests
import socket
import whois

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def print_ip_info(ip_info):
    print("IP Address:", ip_info["ip"])
    print("Hostname:", ip_info["hostname"])
    print("City:", ip_info["city"])
    print("Region:", ip_info["region"])
    print("Country:", ip_info["country"])
    print("Location:", ip_info["loc"])
    print("Organization:", ip_info["org"])
    print("Postal Code:", ip_info["postal"])
    print("Timezone:", ip_info["timezone"])
    print("ASN:", ip_info["asn"])

def reverse_dns_lookup(ip_address):
    try:
        host = socket.gethostbyaddr(ip_address)
        return host[0]
    except socket.herror:
        return "N/A"

def whois_lookup(ip_address):
    try:
        w = whois.whois(ip_address)
        return w
    except whois.parser.PywhoisError:
        return "N/A"

def main():
    ip_address = input("Enter the IP address you want to look up: ")
    ip_info = get_ip_info(ip_address)
    print("\n=== IP Information ===")
    print_ip_info(ip_info)
    
    print("\n=== Reverse DNS Lookup ===")
    reverse_dns = reverse_dns_lookup(ip_address)
    print("Reverse DNS:", reverse_dns)
    
    print("\n=== WHOIS Information ===")
    whois_info = whois_lookup(ip_address)
    print(whois_info)

if __name__ == "__main__":
    main()
