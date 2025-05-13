import hashlib
import os

class Exploit:
    name = "Hash Cracker"
    description = "Attempts to crack a hash using a wordlist (MD5, SHA1, SHA256, SHA512)"
    options = {
        "HASH": "",
        "TYPE": "md5",  # md5, sha1, sha256, sha512
        "WORDLIST": "wordlist.txt"
    }

    def run(self):
        target_hash = self.options["HASH"].strip().lower()
        hash_type = self.options["TYPE"].strip().lower()
        wordlist = self.options["WORDLIST"]

        if not os.path.exists(wordlist):
            print(f"[!] Wordlist not found: {wordlist}")
            return

        hash_func = None
        if hash_type == "md5":
            hash_func = hashlib.md5
        elif hash_type == "sha1":
            hash_func = hashlib.sha1
        elif hash_type == "sha256":
            hash_func = hashlib.sha256
        elif hash_type == "sha512":
            hash_func = hashlib.sha512
        else:
            print(f"[!] Unsupported hash type: {hash_type}")
            return

        print(f"[*] Cracking {hash_type.upper()} hash: {target_hash}")
        print(f"[*] Using wordlist: {wordlist}")

        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                hashed = hash_func(word.encode()).hexdigest()

                if hashed == target_hash:
                    print(f"[+] Hash cracked! Password is: {word}")
                    return

        print("[!] Password not found in wordlist.")
