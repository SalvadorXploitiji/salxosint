import os
import time
import signal

# Menangani keyboard interruption (Ctrl+C)
def signal_handler(signal, frame):
    clear_screen()
    display_logo()
    print('\033[1;m [\033[1;31mX\033[1;m] Anda menekan Ctrl+C!')
    time.sleep(2)
    exit()
signal.signal(signal.SIGINT, signal_handler)

# Membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan logo utama
def display_logo():
    clear_screen()
    print("""
\033[1;31m   ██████  █████  ██      ██   ██     ██████  ███████ ███    ██ ██ ████████ 
\033[1;31m  ██       ██   ██ ██      ██   ██     ██   ██ ██      ████   ██ ██    ██    
\033[1;31m  ██   ███ ███████ ██      ███████     ██   ██ █████   ██ ██  ██ ██    ██    
\033[1;31m  ██    ██ ██   ██ ██      ██   ██     ██   ██ ██      ██  ██ ██ ██    ██    
\033[1;31m   ██████  ██   ██ ███████ ██   ██     ██████  ███████ ██   ████ ██    ██    
\033[1;35m          OSINT TOOL BY SALX | Version 1.0
     """)

# Menampilkan menu utama
def main_menu():
    display_logo()
    time.sleep(1) 
    print("""
\033[1;33m      1. Cari Nama
\033[1;33m      2. Cari Nomor Telepon
\033[1;33m      3. Cari IP
\033[1;36m      99. Tentang SALX OSINT
    """)
    
    option = input("\033[1;35m  Pilih opsi:\033[1;m ")
    menu_actions = {
        "1": search_by_name,
        "2": search_by_phone,
        "3": search_by_ip,
        "99": lambda: print("\n\033[1;34mTentang SALX OSINT: https://github.com/SalvadorXploitiji\033[1;m\n")
    }
    
    if option in menu_actions:
        menu_actions[option]()
    else:
        print("\033[1;31m[ERROR]\033[1;m Pilihan tidak valid!")
        time.sleep(2)
        main_menu()

# Fungsi untuk menampilkan link di terminal
def show_link(url):
    print(f"\n\033[1;34m[INFO] Buka link ini di browser:\n {url}\033[1;m\n")
    input("\033[1;32mTekan Enter untuk kembali ke menu utama...\033[1;m")
    main_menu()

# Fungsi untuk pencarian nama
def search_by_name():
    clear_screen()
    display_logo()  
    time.sleep(1)
    name = input(" Nama:\033[1;m ")
    f_name = input("\033[1;35m Nama Belakang:\033[1;m ")
    
    search_sites = {
        "1": f"https://pipl.com/search/?q={name}+{f_name}",
        "2": f"https://www.facebook.com/search/top/?init=quick&q={name} {f_name}",
        "3": f"https://www.spokeo.com/{name}-{f_name}",
        "4": f"https://www.peekyou.com/{name}_{f_name}",
        "5": f"https://twitter.com/search?f=users&vertical=default&q={name} {f_name}"
    }
    
    print("""
 1. Pipl  
 2. Facebook  
 3. Spokeo  
 4. Peekyou  
 5. Twitter  
    """)
    
    choice = input("\033[1;35m Pilih opsi:\033[1;m ")
    
    if choice in search_sites:
        show_link(search_sites[choice])
    else:
        print("\033[1;31m[ERROR]\033[1;m Pilihan tidak valid!")
        time.sleep(2)
        search_by_name()

# Fungsi untuk pencarian nomor telepon
def search_by_phone():
    clear_screen()
    display_logo()  
    time.sleep(1)
    phone_number = input(" Nomor Telepon:\033[1;m ")

    search_sites = {
        "1": f"http://www.okcaller.com/{phone_number}",
        "2": f"https://www.facebook.com/search/top/?init=quick&q={phone_number}",
        "3": f"https://www.truecaller.com/search/global/{phone_number}",
        "4": f"https://www.whitepages.com/phone/{phone_number}",
        "5": f"https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={phone_number}"
    }

    print("""
 1. Okcaller  
 2. Facebook  
 3. TrueCaller  
 4. Whitepages  
 5. PagesJaunes  
    """)
    
    choice = input("\033[1;35m Pilih opsi:\033[1;m ")
    
    if choice in search_sites:
        show_link(search_sites[choice])
    else:
        print("\033[1;31m[ERROR]\033[1;m Pilihan tidak valid!")
        time.sleep(2)
        search_by_phone()

# Fungsi pencarian IP
def search_by_ip():
    clear_screen()
    display_logo()  
    time.sleep(1)
    ip_address = input(" IP Address:\033[1;m ")

    search_sites = {
        "1": f"https://ipinfo.io/{ip_address}",
        "2": f"https://whatismyipaddress.com/ip/{ip_address}",
        "3": f"https://www.shodan.io/host/{ip_address}",
        "4": f"https://www.virustotal.com/gui/ip-address/{ip_address}",
        "5": f"https://who.is/whois-ip/ip-address/{ip_address}"
    }

    print("""
 1. IPInfo  
 2. WhatIsMyIPAddress  
 3. Shodan  
 4. VirusTotal  
 5. Whois Lookup  
    """)
    
    choice = input("\033[1;35m Pilih opsi:\033[1;m ")
    
    if choice in search_sites:
        show_link(search_sites[choice])
    else:
        print("\033[1;31m[ERROR]\033[1;m Pilihan tidak valid!")
        time.sleep(2)
        search_by_ip()

# Jalankan program
if __name__ == "__main__":
    main_menu()