"""from bs4 import BeautifulSoup
import re
tickets = [
    "  LOGIN ERROR!!!  ",
    "<p>VPN is NOT working properly</p>",
    "Printer     is     not responding!!!",
    "  PASSWORD RESET   REQUIRED  "
]
for ticket in tickets:
    cleaned = ticket.lower().strip()
    soup =BeautifulSoup(cleaned, "html.parser")
    cleaned = soup.get_text()
    cleaned = re.sub(r'[^a-z0-9\s]', '', cleaned)
    print(cleaned) """

text = "  vpN ERROR!!!  "

text = text.lower()

if any(word in text for word in ["login", "password", "authentication"]):
    print("Access")

elif any(word in text for word in ["vpn", "wifi", "internet", "network"]):
    print("Network")

elif any(word in text for word in ["printer", "keyboard", "laptop"]):
    print("Hardware")

elif any(word in text for word in ["application", "software", "installation"]):
    print("Software")

print("Other")