import requests

class Exploit:
    name = "IPinfo Lookup"
    description = "Retrieves detailed information about an IP address using IPinfo.io API"
    options = {
        "RHOST": "8.8.8.8",
        "TOKEN": "token"  # Optional: Your IPinfo.io API token
    }

    def run(self):
        ip = self.options["RHOST"]
        token = self.options["TOKEN"]
        url = f"https://ipinfo.io/{ip}/json"
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()

            print(f"\n[+] IP Information for {ip}:\n")
            for key, value in data.items():
                print(f"{key.capitalize()}: {value}")
        except requests.RequestException as e:
            print(f"[!] Error fetching data: {e}")
