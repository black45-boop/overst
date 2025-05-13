import requests
import os

class Exploit:
    name = "Folder Cracker"
    description = "Finds valid folders on a web server using a wordlist"
    options = {
        "RHOST": "http://example.com",
        "WORDLIST": "folders.txt"
    }

    def run(self):
        base_url = self.options["RHOST"].rstrip("/")
        wordlist_path = self.options["WORDLIST"]

        if not os.path.exists(wordlist_path):
            print(f"[!] Wordlist file not found: {wordlist_path}")
            return

        print(f"[*] Scanning {base_url} with {wordlist_path}")

        try:
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    folder = line.strip()
                    url = f"{base_url}/{folder}"
                    try:
                        response = requests.get(url, timeout=3, allow_redirects=False)
                        if response.status_code in [200, 301, 302, 403]:
                            print(f"[+] Found: {url} (Status: {response.status_code})")
                        else:
                            print(f"[-] {url} (Status: {response.status_code})")
                    except requests.RequestException as e:
                        print(f"[!] Error with {url}: {e}")
        except Exception as e:
            print(f"[!] Could not read wordlist: {e}")
