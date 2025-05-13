import time
import os
import sys
from colorama import init, Fore

init(autoreset=True)

def type_out(text, color=Fore.YELLOW, delay=0.002):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)

def show_banner():
    banner = r"""
 ██████╗ ██╗   ██╗███████╗██████╗ ███████╗██████╗ ██╗      ██████╗ ██╗███╗   ██╗
██╔════╝ ██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██║████╗  ██║
██║  ███╗██║   ██║█████╗  ██████╔╝█████╗  ██████╔╝██║     ██║   ██║██║██╔██╗ ██║
██║   ██║██║   ██║██╔══╝  ██╔═══╝ ██╔══╝  ██╔═══╝ ██║     ██║   ██║██║██║╚██╗██║
╚██████╔╝╚██████╔╝███████╗██║     ███████╗██║     ███████╗╚██████╔╝██║██║ ╚████║
 ╚═════╝  ╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
                               O V E R S P L O I T
"""
    type_out(banner, color=Fore.LIGHTRED_EX, delay=0.0009)

def launch():
    show_banner()
    time.sleep(0.5)
    os.system("python3 oversploit.py")

if __name__ == "__main__":
    launch()
