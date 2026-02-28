import socket
import requests
import os
import colorama
import ssl
from urllib.parse import urlparse
from requests.exceptions import RequestException
import concurrent.futures
from bs4 import BeautifulSoup
from pystyle import Center, Colorate, Colors, Anime
import colorama
import os

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
 /$$$$$$$  /$$$$$$$$ /$$       /$$   /$$  /$$$$$$   /$$$$$$ 
| $$__  $$| $$_____/| $$      | $$  | $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$      | $$      | $$  | $$| $$  \__/| $$  \ $$
| $$$$$$$ | $$$$$   | $$      | $$  | $$| $$ /$$$$| $$$$$$$$
| $$__  $$| $$__/   | $$      | $$  | $$| $$|_  $$| $$__  $$
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$| $$  | $$
| $$$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$
|_______/ |________/|________/ \______/  \______/ |__/  |__/

                ┏━━━━━━━━━━━━━━━━━━━━━┓
                ┃  Author : Ego/xhe   ┃
                ┃ Discord: .gg/xxxx   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))

def WebsiteFoundUrl(url):
    website_url = f"https://{url}" if not urlparse(url).scheme else url
    print(colorama.Fore.WHITE + f"Website: {website_url}")
    return website_url

def WebsiteDomain(website_url):
    domain = urlparse(website_url).netloc
    print(colorama.Fore.WHITE + f"Domain: {domain}")
    return domain

def WebsiteIp(domain):
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        ip = "None"
    if ip != "None":
        print(colorama.Fore.WHITE + f"IP: {ip}")
    return ip

def IpType(ip):
    if ':' in ip:
        type = "ipv6" 
    elif '.' in ip:
        type = "ipv4"
    else:
        return
    print(colorama.Fore.WHITE + f"IP Type: {type}")

def WebsiteSecure(website_url):
    print(colorama.Fore.WHITE + f"Secure: {website_url.startswith('https://')}")

def WebsiteStatus(website_url):
    try:
        status_code = requests.get(website_url, timeout=5).status_code
    except RequestException:
        status_code = 404
    print(colorama.Fore.WHITE + f"Status Code: {status_code}")

def IpInfo(ip):
    try:
        api = requests.get(f"https://ipinfo.io/{ip}/json").json()
    except RequestException:
        api = {}
    for key in ['country', 'hostname', 'isp', 'org', 'asn']:
        if key in api:
            print(colorama.Fore.WHITE + f"Host {key.capitalize()}: {api[key]}")

def IpDns(ip):
    try:
        dns = socket.gethostbyaddr(ip)[0]
    except:
        dns = "None"
    if dns != "None":
        print(colorama.Fore.WHITE + f"Host DNS: {dns}")

def WebsitePort(ip):
    ports = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }

    def ScanPort(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                if sock.connect_ex((ip, port)) == 0:
                    print(colorama.Fore.WHITE + f"Port: {port} Status: Open Protocol: {port_protocol_map.get(port, 'Unknown')}")
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: ScanPort(ip, p), ports)

def HttpHeaders(website_url):
    try:
        headers = requests.get(website_url, timeout=5).headers
        for header, value in headers.items():
            print(colorama.Fore.WHITE + f"HTTP Header: {header} Value: {value}")
    except RequestException:
        pass

def CheckSslCertificate(website_url):
    try:
        with ssl.create_default_context().wrap_socket(socket.socket(), server_hostname=urlparse(website_url).hostname) as sock:
            sock.settimeout(5)
            sock.connect((urlparse(website_url).hostname, 443))
            cert = sock.getpeercert()
        for key, value in cert.items():
            print(colorama.Fore.WHITE + f"SSL Certificate Key: {key} Value: {value}")
    except:
        pass

def CheckSecurityHeaders(website_url):
    headers = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
    try:
        response_headers = requests.get(website_url, timeout=5).headers
        for header in headers:
            print(colorama.Fore.WHITE + f"{'Missing' if header not in response_headers else 'Security'} Header: {header}")
    except RequestException:
        pass

def AnalyzeCookies(website_url):
    try:
        cookies = requests.get(website_url, timeout=5).cookies
        for cookie in cookies:
            secure = 'Secure' if cookie.secure else 'Not Secure'
            httponly = 'HttpOnly' if cookie.has_nonstandard_attr('HttpOnly') else 'Not HttpOnly'
            print(colorama.Fore.WHITE + f"Cookie: {cookie.name} Secure: {secure} HttpOnly: {httponly}")
    except RequestException:
        pass

def DetectTechnologies(website_url):
    try:
        response = requests.get(website_url, timeout=5)
        headers = response.headers
        soup = BeautifulSoup(response.content, 'html.parser')
        techs = []
        if 'x-powered-by' in headers:
            techs.append(f"X-Powered-By: {headers['x-powered-by']}")
        if 'server' in headers:
            techs.append(f"Server: {headers['server']}")
        for script in soup.find_all('script', src=True):
            if 'jquery' in script['src']:
                techs.append("jQuery")
            if 'bootstrap' in script['src']:
                techs.append("Bootstrap")
        for tech in techs:
            print(colorama.Fore.WHITE + f"Detected Technology: {tech}")
    except:
        pass

# Main logic
url = input(colorama.Fore.YELLOW + "Website URL -> ")
website_url = WebsiteFoundUrl(url)
domain = WebsiteDomain(website_url)
ip = WebsiteIp(domain)
IpType(ip)
WebsiteSecure(website_url)
WebsiteStatus(website_url)
IpInfo(ip)
IpDns(ip)
WebsitePort(ip)
HttpHeaders(website_url)
CheckSslCertificate(website_url)
CheckSecurityHeaders(website_url)
AnalyzeCookies(website_url)
DetectTechnologies(website_url)
