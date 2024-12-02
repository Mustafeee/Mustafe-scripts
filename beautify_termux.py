import os
import time

# Magacaaga ku dar
username = "YahaY Mustafe"

def print_banner():
    os.system("clear")  # Nadiifi shaashadda
    print(f"Welcome to Termux, {username}!")
    print("=" * 40)
    print("This is a simple Python script to beautify Termux.")
    print("=" * 40)

def print_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")

def main():
    print_banner()
    print_time()

if __name__ == "__main__":
    main()
